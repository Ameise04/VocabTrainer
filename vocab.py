class Vocab:
    def __init__(self, japanese, german):
        self.japanese = japanese
        self.german = german
        self.isSentence = self.checkIfSentence()

    def checkIfSentence(self):
        return " " in self.japanese.strip() or " " in self.german.strip()