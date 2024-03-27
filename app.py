from tkinter import *
import os
from customtkinter import *

basedir = os.path.dirname(__file__)


window = CTk()
window.geometry("500x550")
window.title("Bit-Calculator")
window.resizable(False, False)
window.iconbitmap(os.path.join(basedir, "./Assets/icon.ico"))

initialBitType = IntVar(value=0)
initialBitValue = StringVar()
initialVelocityType = IntVar(value=0)
initialVelocityValue = StringVar()


resultByte = DoubleVar()
resultBit = DoubleVar()
resultSegunds = DoubleVar()
resultMinutes = DoubleVar()
errorResult = StringVar()
isErro = BooleanVar()


def BitCalculator():
    if initialBitValue.get() == "":
        errorResult.set("Preencha as Informações Corretante!")
        isErro.set(True)
        resultFrame()
        ErrorFrame()

    else:

        isErro.set(False)
        errorResult.set("")
        ErrorFrame()
        bitType = ""

        VelocityTypeGet = initialVelocityType.get()
        VelocityValueGet = float(initialVelocityValue.get())

        resultSegunds.set(0)
        resultMinutes.set(0)

        resultFrame()

        increaseNumber = initialBitType.get()
        decreaseNumber = VelocityTypeGet

        bitAccumulator = float(initialBitValue.get())

        if VelocityTypeGet == 1:
            bitType = "K"
        elif VelocityTypeGet == 2:
            bitType = "M"
        elif VelocityTypeGet == 3:
            bitType = "G"

        if decreaseNumber <= increaseNumber:
            for i in range(1, (increaseNumber - decreaseNumber) + 1):
                bitAccumulator = bitAccumulator * 1024
        else:
            for i in range(1, (increaseNumber - decreaseNumber) + 1):
                bitAccumulator = bitAccumulator / 1024

        resultByte.set(f"S = {bitAccumulator} {bitType}B")

        if initialBitValue.get() == 0:
            return resultBit.set(f"S = {bitAccumulator * 8} bit")
        else:
            resultBit.set(f"{bitAccumulator * 8} {bitType}bit")

        bitComplete = (bitAccumulator * 8) / VelocityValueGet

        resultSegunds.set(("{:.2f} Segundos".format(bitComplete)))
        resultMinutes.set("{:.2f} Minutos".format(bitComplete / 60))


frameWeight = CTkFrame(
    window,
    fg_color="#697268",
    bg_color="#dddddd",
    border_width=0.6,
    height=170,
    corner_radius=0,
).pack(fill=BOTH)

CTkLabel(
    frameWeight,
    width=300,
    text="Coloque as Informações do Tamanho do Arquivo",
    corner_radius=0,
    fg_color="#697268",
).place(x=100, y=7)

CTkEntry(
    frameWeight,
    width=390,
    height=35,
    textvariable=initialBitValue,
    text_color="#000000",
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=1,
).place(x=55, y=55)


Radiobutton(
    frameWeight,
    text="Byte",
    value=0,
    width=5,
    variable=initialBitType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=75, y=125)

Radiobutton(
    frameWeight,
    text="KB",
    value=1,
    width=5,
    variable=initialBitType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=175, y=125)

Radiobutton(
    frameWeight,
    text="MB",
    value=2,
    width=5,
    variable=initialBitType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=275, y=125)

Radiobutton(
    frameWeight,
    text="GB",
    value=3,
    width=5,
    variable=initialBitType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=375, y=125)


# ----------------------------------------------------------------------------------------------------------------------------------------


frameVelocity = CTkFrame(
    window,
    fg_color="#697268",
    bg_color="#dddddd",
    border_width=0.6,
    height=170,
    corner_radius=0,
).pack(fill=BOTH)


CTkLabel(
    frameVelocity,
    width=300,
    text="Coloque a Velocidade de Download",
    corner_radius=0,
    fg_color="#697268",
).place(x=100, y=178)

CTkEntry(
    frameVelocity,
    width=390,
    height=35,
    textvariable=initialVelocityValue,
    text_color="#000000",
    fg_color="#FFFFFF",
    corner_radius=0,
    border_width=1,
).place(x=55, y=225)


Radiobutton(
    frameVelocity,
    text="Bit",
    value=0,
    width=5,
    variable=initialVelocityType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=75, y=295)

Radiobutton(
    frameVelocity,
    text="Kb",
    value=1,
    width=5,
    variable=initialVelocityType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=175, y=295)

Radiobutton(
    frameVelocity,
    text="Mb",
    value=2,
    width=5,
    variable=initialVelocityType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=275, y=295)

Radiobutton(
    frameVelocity,
    text="Gb",
    value=3,
    width=5,
    variable=initialVelocityType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=375, y=295)


# --------------------------------------------------------------------------------------------------

frameResult = CTkFrame(
    window,
    fg_color="#1c1c1c",
    bg_color="#dddddd",
    border_width=0.6,
    height=170,
).pack(fill=BOTH, side=BOTTOM)

CTkLabel(
    frameResult, text="Resultados:", font=("Roboto", 25), fg_color="#1c1c1c"
).place(x=185, y=400)


def resultFrame():
    if isErro.get():
        resultBit.set("")
        resultByte.set("")
        resultMinutes.set("")
        resultSegunds.set("")
    else:
        CTkLabel(
            frameResult,
            textvariable=resultBit,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=55, y=440)
        CTkLabel(
            frameResult,
            textvariable=resultByte,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=305, y=440)
        CTkLabel(
            frameResult,
            textvariable=resultSegunds,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=55, y=480)
        CTkLabel(
            frameResult,
            textvariable=resultMinutes,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=305, y=480)


def ErrorFrame():
    if isErro.get():
        CTkLabel(
            frameResult,
            textvariable=errorResult,
            text_color="#FF0000",
            bg_color="#1c1c1c",
            font=("Roboto", 27, "bold"),
        ).place(x=10, y=450)


CTkButton(
    window,
    command=BitCalculator,
    text="Calcular",
    width=500,
    height=50,
    text_color="#000000",
    fg_color="#1C3144",
    corner_radius=0,
    border_width=0,
    font=("Hervetica", 30),
).place(y=337)


window.mainloop()
