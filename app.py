from tkinter import *
import os
from customtkinter import *
from Utils.Calculete import *
import Utils.Variables as vr

basedir = os.path.dirname(__file__)


window = CTk()
window.geometry("500x550")
window.title("Bit-Calculator")
window.resizable(False, False)
window.iconbitmap(os.path.join(basedir, "Assets/icon.ico"))

initialBitType = IntVar(value=0)
initialBitValue = StringVar()
initialVelocityType = IntVar(value=0)
initialVelocityValue = StringVar()


def passData():
    BitCalculator(
        initialBitType.get(),
        initialBitValue.get(),
        initialVelocityType.get(),
        initialVelocityValue.get(),
    )

    if vr.isErro != False:
        bitText.set(vr.resultBit)
        byteText.set(vr.resultByte)
        secondsText.set(vr.resultSegunds)
        minutesText.set(vr.resultMinutes)
        errorText.set(vr.errorResult)
        ErrorFrame()
        resultFrame()

    else:
        bitText.set(vr.resultBit)
        byteText.set(vr.resultByte)
        secondsText.set(vr.resultSegunds)
        minutesText.set(vr.resultMinutes)
        errorText.set(vr.errorResult)
        resultFrame()
        ErrorFrame()


errorText = StringVar()
bitText = IntVar()
byteText = IntVar()
secondsText = DoubleVar()
minutesText = DoubleVar()

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
).place(x=50, y=125)

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
).place(x=140, y=125)

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
).place(x=230, y=125)

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
).place(x=320, y=125)


Radiobutton(
    frameWeight,
    text="TB",
    value=4,
    width=5,
    variable=initialBitType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=410, y=125)


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
).place(x=50, y=295)

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
).place(x=140, y=295)

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
).place(x=230, y=295)

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
).place(x=320, y=295)


Radiobutton(
    frameVelocity,
    text="Tb",
    value=4,
    width=5,
    variable=initialVelocityType,
    background="#9CA69B",
    highlightbackground="#9CA69B",
    highlightcolor="#9CA69B",
    borderwidth=3,
    indicatoron=0,
).place(x=405, y=295)


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
    if vr.isErro == False:
        # bitText.set("")
        # byteText.set("")
        # secondsText.set("")
        # minutesText.set("")
        CTkLabel(
            frameResult,
            textvariable=bitText,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=55, y=440)
        CTkLabel(
            frameResult,
            textvariable=byteText,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=305, y=440)
        CTkLabel(
            frameResult,
            textvariable=secondsText,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=55, y=480)
        CTkLabel(
            frameResult,
            textvariable=minutesText,
            fg_color="#1c1c1c",
            bg_color="#1c1c1c",
            font=("Roboto", 25),
        ).place(x=305, y=480)


def ErrorFrame():
    if vr.isErro:
        CTkLabel(
            frameResult,
            textvariable=errorText,
            text_color="#FF0000",
            bg_color="#1c1c1c",
            font=("Roboto", 27, "bold"),
        ).place(x=10, y=450)


CTkButton(
    window,
    command=passData,
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
