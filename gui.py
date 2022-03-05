from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def main():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def declare(btn):
        names = ['Gastroenterology', 'Ear, Nose, Throat', 'Internal Medicine', 'Dermatology', 'Gynecology', 'Ophthalmoloy', 'Pediatrics', 'Orthopedics']
        department = names[btn-1]
        f = open("department.txt", "w")
        f.write(department)
        f.close()
        window.destroy()


    window = Tk()

    window.geometry("663x622")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 622,
        width = 663,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(1),
        relief="flat"
    )
    button_1.place(
        x=104.0,
        y=92.0,
        width=465.0,
        height=45.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(2),
        relief="flat"
    )
    button_2.place(
        x=104.0,
        y=158.0,
        width=465.0,
        height=45.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(3),
        relief="flat"
    )
    button_3.place(
        x=104.0,
        y=224.0,
        width=465.0,
        height=45.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(4),
        relief="flat"
    )
    button_4.place(
        x=104.0,
        y=290.0,
        width=465.0,
        height=45.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(5),
        relief="flat"
    )
    button_5.place(
        x=105.0,
        y=356.0,
        width=464.0,
        height=45.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(6),
        relief="flat"
    )
    button_6.place(
        x=104.0,
        y=422.0,
        width=466.0,
        height=45.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(7),
        relief="flat"
    )
    button_7.place(
        x=104.0,
        y=488.0,
        width=466.0,
        height=45.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: declare(8),
        relief="flat"
    )
    button_8.place(
        x=105.0,
        y=554.0,
        width=463.0,
        height=49.906982421875
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=144.0,
        y=12.0,
        width=378.25,
        height=44.0
    )
    window.title("Select Department")
    window.resizable(False, False)
    window.mainloop()
