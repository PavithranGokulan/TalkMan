from kivymd.app import MDApp
from kivy.lang import Builder

import speech_recognition as s
import pyttsx3 as p

r=s.Recognizer()

def talk(text):
    p.speak(text)

code="""
MDScreen:

        ScrollView:
                MDList:
                        id:list

        MDIconButton:
                icon:"microphone-outline"
                md_bg_color:(1,0,0,.9)
                pos_hint:{"center_x":0.9,"center_y":0.1}
                on_release:app.Talkbot()
"""

class PaviApp(MDApp):
    def build(self):
        return Builder.load_string(code)

    def Talkbot(self):
        while True:
            with s.Microphone() as source:
                print("Listening...")
                audio=r.listen(source)
                txt=r.recognize_google(audio)
                txt=txt.lower()
                p.speak(txt)


if __name__=="__main__":
        PaviApp().run()


            
