from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import webbrowser
import os
from backend import Backend
from tkinter import filedialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.path.join("assets"))

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

entryImage1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    650.4999999999999,
    167.5,
    image=entryImage1
)
entry1 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)

# def delete_text1(event):
#     if entry1.get() == "First Page":
#         entry1.delete(0, "end")
#     else:
#         entry1.insert(0, "First Page")

entry1.insert(0, "First Page")
# entry1.bind("<Button-1>", delete_text1)
entry1.bind("<Button-1>", lambda event: entry1.delete(0, "end"))

entry1.place(
    x=489.9999999999999,
    y=137.0,
    width=321.0,
    height=59.0
)
# entry1.configure(font=("Roboto", 14 * -1))

entryImage2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    650.4999999999999,
    248.5,
    image=entryImage2
)
entry2 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)

# def delete_text2(event):
#     entry2.delete(0, "end")

entry2.insert(0, "Last Page")
# entry2.bind("<Button-1>", delete_text2)
entry2.bind("<Button-1>", lambda event: entry2.delete(0, "end"))

entry2.place(
    x=489.9999999999999,
    y=218.0,
    width=321.0,
    height=59.0
)

entryImage3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    650.4999999999999,
    329.5,
    image=entryImage3
)
entry3 = Entry(
    bd=0,
    bg="#80D7FE",
    fg="#000716",
    highlightthickness=0,
    font=("Bahnschrift SemiLight", 13 * -1)
)


def onClick():
    worker = Backend(int(entry1.get()), int(entry2.get()))
    worker.set_file(filename if filename else "rapid.pdf")
    worker.Print()


buttonImage1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=buttonImage1,
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
    try:
        filename = filedialog.askopenfilename(initialdir="Desktop", title="Select A File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
        entry3.insert(0, filename)
    except:
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
        entry3.insert(0, filename)

browseImage = PhotoImage(
    file=relative_to_assets("pick2.png")
)
browse = Button(
    image=browseImage,
    borderwidth=0,
    highlightthickness=0,

    command=browse,
    relief="flat"
)

browse.place(
    x=760,
    y=305.5,
)

# def delete_text3(event):
#     entry3.delete(0, "end")

entry3.insert(0, "Choose File")
# entry3.bind("<Button-1>", delete_text3)
entry3.bind("<Button-1>", lambda event: entry3.delete(0, "end"))

entry3.place(
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
