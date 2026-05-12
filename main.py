import utils
def printMenu():
    print("Wählen Sie eine Funktion aus:")
    print("1:\t Neue Vokabeln hinzufügen")
    print("2:\t Vokabeln üben")
    print("3:\t Vokabeln anzeigen")
    print("4:\t Vokabeln entfernen")
    print("5:\t Vokabeln zurücksetzen (Alle Vokabeln löschen)")
    print("x:\t Programm beenden")
    
    
def callFunction(choice, vocabDict):
    match choice:
        case "1":
            return addVocab(vocabDict)
        case "2":
            return practiceVocab(vocabDict)
        case "3":
            return showVocab(vocabDict)
        case "4":
            return removeVocab(vocabDict)
        case "5":
            return resetVocab(vocabDict)
        case "x":
            print("Programm wird beendet...")
            writeVocabToFile(vocabDict)
            exit()
            
def addVocab(vocabDict):
    print("Geben Sie die Vokabeln ein, die Sie hinzufügen möchten. Geben Sie 'x' ein, um den Vorgang zu beenden.")
    anzahlVocab = 0
    while True:       
        japaneseSide = input("[Japanisch]>>>")
        germanSide = input("[Deutsch]>>>")
        if checkVocabExists(vocabDict, japaneseSide):
            print(f"Vokabel '{japaneseSide}' existiert bereits. Überspringen...")
            continue
        if japaneseSide == "x" or germanSide == "x":
            writeVocabToFile(vocabDict)
            return f" {anzahlVocab} neue Vokabeln hinzugefügt!"
        vocabDict[utils.normalizeInput(japaneseSide)] = utils.normalizeInput(germanSide)
        anzahlVocab += 1
        print("----------------------------------")
    
    
def practiceVocab(vocabDict):
    practicedVocab = {}
    print("Praxisübungen beenden mit 'x':")
    while True:
        japanese, german = getRandomVocab(vocabDict, practicedVocab)
        print(f"Was bedeutet {japanese}?")
        userAnswer = input(">>> ")
        if userAnswer == "x":
            break
        if userAnswer == german:
            print("Richtig!")
            practicedVocab[japanese] = german
        else:
            print(f"Falsch! Die richtige Antwort ist: {german}")  
        if len(practicedVocab) == len(vocabDict):
            print("Sie haben alle Vokabeln geübt!")
            break     
    return "Übung beendet."

def showVocab(vocabDict):
    print("Ihre Vokabeln:")
    for japanese, german in vocabDict.items():
        print(f"{japanese} \t -- \t {german}")
    return "Ende der Liste."

def writeVocabToFile(vocabDict):
    with open("vocab.txt", "w", encoding="utf-8") as file:
        for japanese, german in vocabDict.items():
            file.write(f"{japanese}:{german}\n")
            
def readVocabFromFile(vocabDict):
    try:
        with open("vocab.txt", "r", encoding="utf-8") as file:
            for line in file:
                japanese, german = line.strip().split(":")
                vocabDict[japanese] = german
    except FileNotFoundError:
        print("Keine vorhandene Vokabeldatei gefunden. Es wird eine neue erstellt.")
        
def getRandomVocab(vocabDict, practicedVocab={}):
    import random
    if not vocabDict:
        return "Keine Vokabeln zum Üben vorhanden."
    availableVocab = {j: g for j, g in vocabDict.items() if j not in practicedVocab}
    if not availableVocab:
        return "Keine Vokabeln zum Üben vorhanden."
    japanese, german = random.choice(list(availableVocab.items()))
    return japanese, german

def removeVocab(vocabDict):
    print("Geben Sie die Vokabel ein, die Sie entfernen möchten. Geben Sie 'x' ein, um den Vorgang zu beenden.")
    while True:
        japaneseSide = utils.normalizeInput(input("[Japanisch]>>>"))
        if japaneseSide == "x":
            return "Vokabeln entfernen beendet."
        if checkVocabExists(vocabDict, japaneseSide):
            del vocabDict[japaneseSide]
            print(f"Vokabel '{japaneseSide}' entfernt.")
        else:
            print(f"Vokabel '{japaneseSide}' nicht gefunden.")
        return "Vokabeln entfernen beendet."

def normalizeDict(vocabDict):
    normalizedDict = {}
    for japanese, german in vocabDict.items():
        normalizedDict[utils.normalizeInput(japanese)] = utils.normalizeInput(german)
    return normalizedDict
        
def checkVocabExists(vocabDict, japanese):
    return utils.normalizeInput(japanese) in vocabDict

def resetVocab(vocabDict):
    confirmation = input("Sind Sie sicher, dass Sie alle Vokabeln löschen möchten? (y/n)>>>")
    if confirmation.lower() == "y":
        vocabDict.clear()
        return "Alle Vokabeln wurden gelöscht."
    else:
        return "Vokabeln zurücksetzen abgebrochen."
    

mainDict = {}
readVocabFromFile(mainDict)
mainDict = normalizeDict(mainDict)
while True:
    printMenu()
    userInput = input(">>>")
    print("\n\n")
    print(callFunction(userInput, mainDict))
    print("----------------------------------")
    
    
    
    