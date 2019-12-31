from gtts import gTTS

import os

a ='Ta'

f = open("kural.txt", encoding="utf8")

m = f.read()

c=gTTS(lang=a, text=m, slow=False)

c.save("Thirukkural.mp3")

os.system("mpv Thirukkural.mp3")
