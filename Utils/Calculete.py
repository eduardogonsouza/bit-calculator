import Utils.Variables as vr


def BitCalculator(
    initialBitType=0,
    initialBitValue="",
    initialVelocityType=0,
    initialVelocityValue="",
):

    if initialBitValue == "":
        vr.errorResult = "Preencha as Informações Corretante!"
        vr.isErro = True
        vr.resultBit = ""
        vr.resultByte = ""
        vr.resultMinutes = ""
        vr.resultSegunds = ""
    else:
        vr.errorResult = ""
        vr.isErro = False
        bitType = ""

        vr.resultSegunds = 0
        vr.resultMinutes = 0

        increaseNumber = initialBitType
        decreaseNumber = initialVelocityType

        bitAccumulator = float(initialBitValue)

        if initialVelocityType == 1:
            bitType = "K"
        elif initialVelocityType == 2:
            bitType = "M"
        elif initialVelocityType == 3:
            bitType = "G"

        if decreaseNumber <= increaseNumber:
            for i in range(1, (increaseNumber - decreaseNumber) + 1):
                bitAccumulator = bitAccumulator * 1024
        else:
            for i in range(1, (increaseNumber - decreaseNumber) + 1):
                bitAccumulator = bitAccumulator / 1024

        vr.resultByte = f"S = {bitAccumulator} {bitType}B"

        if initialBitValue == 0:
            vr.resultBit = f"{bitAccumulator * 8} bit"

        vr.resultBit = f"{bitAccumulator * 8} {bitType}bit"
        bitComplete = (bitAccumulator * 8) / float(initialVelocityValue)
        vr.resultSegunds = "{:.2f} Segundos".format(bitComplete)
        vr.resultMinutes = "{:.2f} Minutos".format(bitComplete / 60)
