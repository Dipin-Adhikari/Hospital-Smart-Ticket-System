from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import csv
import pandas as pd
import pyqrcode
import png


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets1")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def details():
    name = entry_1.get()
    sex = entry_2.get()
    dob = entry_3.get()
    address = entry_4.get()
    
    data = pd.read_csv('data.csv')
    if len(data) == 0:
        id = 1
    else:
        id = data['ID'][len(data)-1] + 1
    
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([id, name, dob, sex, address])

    qrcode = pyqrcode.create(id-1)
    filename = 'qrcodes/' + str(id) + '.png'
    qrcode.png(filename, scale = 10)

window = Tk()

window.geometry("603x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 603,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    322.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    110.0,
    161.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    113.0,
    253.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    116.0,
    345.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    116.0,
    436.0,
    image=image_image_5
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: details(),
    relief="flat"
)
button_1.place(
    x=229.0,
    y=504.0,
    width=146.0,
    height=62.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    392.0,
    158.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=236.0,
    y=128.0,
    width=312.0,
    height=58.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    392.0,
    250.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=236.0,
    y=220.0,
    width=312.0,
    height=58.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    392.0,
    346.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=236.0,
    y=316.0,
    width=312.0,
    height=58.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    392.0,
    437.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=236.0,
    y=407.0,
    width=312.0,
    height=58.0
)
window.title("Form")
window.resizable(False, False)
window.mainloop()
