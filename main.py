from enum import IntEnum
import json

class ValType(IntEnum):
    NAME = 0
    ADDRESS = 1
    PHONE = 2
    INFORMATION = 3

def fieldName(valType):
    if valType == ValType.NAME:
        return "Name"
    elif valType == ValType.ADDRESS:
        return "Address"
    elif valType == ValType.PHONE:
        return "Phone"
    elif valType == ValType.INFORMATION:
        return "Information"
    else:
        return "Additional Information"


parsedData = []
with open("data/oxygenSuppliers.txt", encoding="utf8") as infoTextFile:
    foodData = infoTextFile.read().split("\n\n")
    for info in foodData:
        lines = info.split("\n")
        jsonData = {}
        for i in range(len(lines)):
            jsonData[fieldName(i)] = lines[i]
        parsedData.append(jsonData)

    with open("data/oxygenSuppliers.json", "w", encoding="utf8") as infoJsonFile:
        json.dump(parsedData, infoJsonFile, ensure_ascii=False, indent=4)

parsedData = []
with open("data/foodProviders.txt", encoding="utf8") as foodProvidersTextFile:
    foodData = foodProvidersTextFile.read().split("\n\n")
    for info in foodData:
        lines = info.split("\n")
        jsonData = {}
        for i in range(len(lines)):
            jsonData[fieldName(i)] = lines[i]
        parsedData.append(jsonData)

    with open("data/foodProviders.json", "w", encoding="utf8") as foodProvidersJsonFile:
        json.dump(parsedData, foodProvidersJsonFile, ensure_ascii=False, indent=4)

parsedData = []
with open("data/vaccineProviders.txt", encoding="utf8") as vaccineProvidersTextFile:
    foodData = vaccineProvidersTextFile.read().split("\n\n")
    for info in foodData:
        lines = info.split("\n")
        jsonData = {}
        for i in range(len(lines)):
            jsonData[fieldName(i)] = lines[i]
        parsedData.append(jsonData)

    with open("data/vaccineProviders.json", "w", encoding="utf8") as vaccineProvidersJsonFile:
        json.dump(parsedData, vaccineProvidersJsonFile, ensure_ascii=False, indent=4)
