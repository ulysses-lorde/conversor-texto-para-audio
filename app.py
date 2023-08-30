from flask import Flask, render_template, Response
from gtts import gTTS


app = Flask(__name__)

def gerar_arquivo_audio(language='pt-br'):
    '''Gera arquivo de áudio em português'''
    my_obj = gTTS(text='oi', lang=language, slow=False)
    my_obj.save('static/test.mp3')

@app.route('/')
def play_audio():
    gerar_arquivo_audio()  # Gera o arquivo de áudio
    return render_template('play_audio.html')

@app.route('/audio/<filename>')
def stream_audio(filename):
    def generate():
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                yield chunk
    return Response(generate(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)

