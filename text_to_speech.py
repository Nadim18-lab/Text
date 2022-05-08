from gtts import gTTS
import os

myText="Hola y bienvenidos a Europa"

language='es'

output = gTTS(text=myText,lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")