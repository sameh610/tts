from gtts import gTTS
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/tts/<text>')
def tts(text):
    tts = gTTS(text)
    tts.save('output.mp3')
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000)

