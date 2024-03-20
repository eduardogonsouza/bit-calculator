from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def BitCalculator():
    initialbit = float(input("Qual o valor de entrada ? "))
    bitType = ""
    bitAccumulator = initialbit

    trasformationByte = inquirer.select(
        message="Selecione a o tipo de byte inserido acima:",
        choices=[
            Choice(value=0, name="Byte"),
            Choice(value=1, name="KB"),
            Choice(value=2, name="MB"),
            Choice(value=3, name="GB"),
        ],
        default=None,
    ).execute()

    trasformationBit = inquirer.select(
        message="Selecione o bit para qual deseja transformar:",
        choices=[
            Choice(value=0, name="Bit"),
            Choice(value=1, name="Kb"),
            Choice(value=2, name="Mb"),
            Choice(value=3, name="Gb"),
        ],
        default=None,
    ).execute()

    increaseNumber = trasformationByte
    decreaseNumber = trasformationBit

    if trasformationByte == 1:
        bitType = "K"
    elif trasformationByte == 2:
        bitType = "M"
    elif trasformationByte == 3:
        bitType = "G"

    for i in range(1, (increaseNumber - decreaseNumber) + 1):
        bitAccumulator = bitAccumulator * 1024

    if trasformationBit == 0:
        return print(f"{bitAccumulator * 8}bit/s")

    print(f"{bitAccumulator} {bitType}B")
    print(f"{bitAccumulator * 8} {bitType}bit/s")


BitCalculator()
