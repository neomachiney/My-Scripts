from string import ascii_uppercase

class Words:
    def __init__(self):
        self.words_dict = {}
        self.generate_single()

    def generate_single(self):
        words = (line.rstrip('\n') for line in open('/root/MachineYadav/My-Scripts/MnemonicGenerator/words')) #change it
        self.words_dict = {letter: [] for letter in ascii_uppercase}
        for word in words:
            self.words_dict[word[0].upper()].append(word)
