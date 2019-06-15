from flask import Flask, request, jsonify
import time
import speech_recognition as sr
from pydub import AudioSegment
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "GET":
        return "Please use a post request!"
    if request.method == "POST":
        data = request.data.decode("utf-8")
        print("The url is : " + data)
        sound_file = urllib.request.URLopener()
        sound_file.retrieve(data, "transcript.mp3")
        response = jsonify({'answer': recognize()})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


def recognize():

    # convert mp3 file to wav
    sound = AudioSegment.from_mp3("transcript.mp3")
    sound.export("transcript.wav", format="wav")

    # transcribe audio file
    AUDIO_FILE = "transcript.wav"

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
        final_text = r.recognize_google(audio)
        print("Transcription: " + final_text)
        return final_text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=False)