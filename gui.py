from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import webbrowser
import os
from backend import Backend
from tkinter import filedialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.path.join("assets", 'frame0'))

if not os.path.exists("temp"):
    os.mkdir(os.getcwd() + "\\temp")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg="#FFFFFF")
window.iconbitmap(relative_to_assets("logo.ico"))


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    1.1368683772161603e-13,
    7.105427357601002e-15,
    431.0000000000001,
    519.0,
    fill="#00AFFD",
    outline="")


canvas.create_text(
    119.99999999999989,
    327.0,
    anchor="nw",
    text="Rapid Print",
    fill="#FCFCFC",
    font=("RobotoRoman ExtraBold", 36 * -1, 'bold')
)

canvas.create_text(
    488.9999999999999,
    69.0,
    anchor="nw",
    text="Welcome to Rapid Print",
    fill="#505485",
    font=("Roboto Bold", 29 * -1)
)

canvas.create_rectangle(
    147.9999999999999,
    376.0,
    270.9999999999999,
    378.0,
    fill="#FCFCFC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)

# def delete_text1(event):
#     if entry_1.get() == "First Page":
#         entry_1.delete(0, "end")
#     else:
#         entry_1.insert(0, "First Page")

entry_1.insert(0, "First Page")
# entry_1.bind("<Button-1>", delete_text1)
entry_1.bind("<Button-1>", lambda event: entry_1.delete(0, "end"))

entry_1.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)
# entry_1.configure(font=("Roboto", 14 * -1))

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    248.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)

# def delete_text2(event):
#     entry_2.delete(0, "end")

entry_2.insert(0, "Last Page")
# entry_2.bind("<Button-1>", delete_text2)
entry_2.bind("<Button-1>", lambda event: entry_2.delete(0, "end"))

entry_2.place(
    x=489.9999999999999,
    y=218.0,
    width=321.0,
    height=59.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    650.4999999999999,
    329.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)


def onClick():
    worker = Backend(int(entry_1.get()), int(entry_2.get()))
    worker.set_file(filename if filename else "pages.pdf")
    worker.Print()


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,

    command=onClick,
    relief="flat"
)

button_1.place(
    x=556.9999999999999,
    y=401.0,
    width=180.0,
    height=55.0
)


def browse():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    print(filename)
browse_image_1 = PhotoImage(
    file=relative_to_assets("pick.png")
)
browse_1 = Button(
    image=browse_image_1,
    borderwidth=0,
    highlightthickness=0,

    command=browse,
    relief="flat"
)

browse_1.place(
    x=750,
    y=401.0,
    width=100,
    height=55.0
)

# def delete_text3(event):
#     entry_3.delete(0, "end")

entry_3.insert(0, "Skip Page (optional)")
# entry_3.bind("<Button-1>", delete_text3)
entry_3.bind("<Button-1>", lambda event: entry_3.delete(0, "end"))

entry_3.place(
    x=489.9999999999999,
    y=299.0,
    width=321.0,
    height=59.0
)


def callback(url):
    webbrowser.open_new(url)


link1 = Label(window, cursor="hand2", text="made by cocomo with ❤️",
              bg="#00AFFD", font=("Inter Medium", 14 * -1), fg="white")
# # link1['bg'] = li.master['bg']
# # link1.wm_attributes('-transparentcolor','black')
link1.place(x=121.99999999999989, y=456.0, anchor="nw")
link1.bind("<Button-1>", lambda e: callback("github.com/cocomo29"))

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    208.9999999999999,
    226.0,
    image=image_image_1
)


if __name__ == "__main__":
    window.title("Rapid Print")
    window.resizable(False, False)
    window.mainloop()
