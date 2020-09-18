import requests

def findMatchedLines():

    response = requests.get("https://raw.githubusercontent.com/commaai/opendbc/master/ESR.dbc", stream=True)


    with open("input2.txt", 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)

    stringToMatch = "CAN_TX_TRACK"
    with open('input2.txt', 'r') as file:
        for line in file:
            if stringToMatch in line:
                matchedLine = line
                print(matchedLine)

if __name__=='__main__':
    findMatchedLines()