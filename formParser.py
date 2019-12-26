# parse text to table by a list of items provided.import inputExample1
import codecs


def parser(filePath):

    with codecs.open(filePath, encoding="utf-8") as f:
        content = f.read()
        lines = content.split("\n\r")
        middle = [[] for i in range(len(lines))]
        i = 0
        for line in lines:
            middle[i] = list((word.replace("\r", "").replace("\n", "")
                              for word in line.split(":")))
            i += 1

        output = [[] for i in range(len(middle))]
        i = 0

        for item in middle:

            if len(item) > 1:
                output[i] = [item[0]]
                tempDataInput = ""
                for index in range(len(item)):
                    if index != 0:
                        tempDataInput += item[index]

                output[i].append(tempDataInput)
                tempDataInput = ""
                i += 1

    output = list(filter(None, output))
    return output
