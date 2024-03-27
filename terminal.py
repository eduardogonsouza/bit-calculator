from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def BitCalculator():
    bitType = ""
    calculationComplete = False

    asYes = inquirer.select(
        message="Deseja calcular toda atividade ?",
        choices=[
            Choice(value=True, name="Yes"),
            Choice(value=False, name="No"),
        ],
        default=None,
    ).execute()

    calculationComplete = asYes

    if calculationComplete == False:
        initialbit = float(input("(Somente Números) Qual o 'Tamanho' do arquivo: "))
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

    elif calculationComplete:
        initialbit = float(input("(Somente Números) Qual o 'Tamanho' do arquivo: "))
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

        bitVelocity = float(input("(Somente Números) Qual o valor da 'Velocidade': "))

        trasformationBit = inquirer.select(
            message="Selecione a o tipo de bit inserido acima:",
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
    bitAccumulator = initialbit

    if trasformationBit == 1:
        bitType = "K"
    elif trasformationBit == 2:
        bitType = "M"
    elif trasformationBit == 3:
        bitType = "G"

    for i in range(1, (increaseNumber - decreaseNumber) + 1):
        bitAccumulator = bitAccumulator * 1024

    if trasformationBit == 0:
        return print(f"{bitAccumulator * 8}bit/s")

    print(f"{bitAccumulator} {bitType}B")
    print(f"{bitAccumulator * 8} {bitType}bit/s")

    if calculationComplete:
        bitComplete = (bitAccumulator * 8) / bitVelocity
        print("{:.2f} Segundos".format(bitComplete))
        print("{:.2f} Minutos".format(bitComplete / 60))


BitCalculator()
