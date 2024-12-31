from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os
from datetime import datetime
import speech_recognition as sr

app = Flask(__name__)

# Ensure the 'static/audio' directory exists
os.makedirs('static/audio', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    text = request.form.get('text', '').strip()
    
    if not text:
        return redirect(url_for('index'))
    
    tts = gTTS(text=text, lang='en')
    output_path = 'static/audio/output.mp3'
    tts.save(output_path)
    
    return render_template('index.html', audio_path=f"{output_path}?t={datetime.now().timestamp()}", text=text)

if __name__ == '__main__':
    app.run(debug=True)
