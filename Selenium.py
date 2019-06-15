from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import speech_recognition as sr
from pydub import AudioSegment
import urllib


opts = Options()
opts.add_argument("disable-infobars")
d = webdriver.Chrome(options=opts)

def solve():
    d.get("https://www.google.com/recaptcha/api2/demo")
    time.sleep(3)
    # Press Checkbox
    d.execute_script("document.querySelector('[role=\"presentation\"]').contentWindow.document.getElementById(\"recaptcha-anchor\").click()")
    # Switch To audio
    d.execute_script("var button = document.querySelector('[title=\"recaptcha challenge\"]').contentWindow.document.getElementById(\"recaptcha-audio-button\");button.dispatchEvent(new MouseEvent('mouseover'));button.dispatchEvent(new MouseEvent('mouseover'));button.dispatchEvent(new MouseEvent('mouseenter'));button.click(); ")
    # Get the audio file
    url = d.execute_script("window.document.querySelector('[title=\"recaptcha challenge\"]').contentWindow.document.getElementsByClassName(\"rc-audiochallenge-tdownload-link\")[0].href;")
    print("The url is : " + url)
    sound_file = urllib.URLopener()
    sound_file.retrieve(url, "transcript.mp3")
    #Solve Audio Challenge
    d.execute_script("document.querySelector('[title=\"recaptcha challenge\"]').contentWindow.document.getElementById('audio-response').value = " + recognize())
    #Press Verify
    d.execute_script("window.document.querySelector('[title=\"recaptcha challenge\"]').contentWindow.document.getElementById(\"recaptcha-verify-button\").click();")

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

        print("Transcription: " + r.recognize_google(audio))

    return r.recognize_google(audio)


    return input("Type enter to exit >")

if __name__ == '__main__':
    solve()
    d.close()