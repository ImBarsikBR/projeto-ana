from flask import Flask, render_template, request
from gtts import gTTS
import os
import time

app = Flask(__name__)

# Função para gerar áudio
def gerar_audio(texto, timestamp):
    audio_filename = f"fala_{timestamp}.mp3"
    tts = gTTS(text=texto, lang='pt')
    tts.save(f"static/{audio_filename}")
    return audio_filename

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        if texto.strip() != "":
            timestamp = int(time.time())
            audio_filename = gerar_audio(texto, timestamp)  # Gerar áudio
            return render_template("index.html", tocando=True, audio_file=audio_filename)

    return render_template("index.html", tocando=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000))) 