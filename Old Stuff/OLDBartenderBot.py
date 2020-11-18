from guizero import App, TextBox, PushButton, Text, Picture
import time

def update_text():
    label.value = name.value

app = App(height=320, width=480, bg="#5f6a6a", layout="grid")
label = Text(app, text="What's your name?", grid=[0,1])
name = TextBox(app, grid=[1,1])
button = PushButton(app, image="settings.gif", grid=[2,2], command=update_text)
#picture = Picture(app, image="settings.gif")#height=128, width=128)

app.display()
