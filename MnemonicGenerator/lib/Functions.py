from requests import get
from termcolor import colored
from random import choice, randrange
from rich.progress import track

from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools

from lib.Words import Words
from lib.Globals import console, repl_console

sentence_maker = SentenceMaker()
sentence_tool = SentenceTools()
words_dict = Words().words_dict

class sentences_generator:
    def __init__(self, permutations):
        self.permutations = permutations
    def __iter__(self):
        for f in self.permutations:
            yield sentence_from_initials(f)
    def __len__(self):
        return len(self.permutations)

def write_permutation(output, permutations):
    with open(output + '.permutation', "w+") as f:
        for _ in permutations:
            f.write("".join(_) + '\n')

def write_sentence(output, permutations):
    everything = False
    if input("Write everything: " + repl_console).upper() == "Y":
        everything = True
    sentences = sentences_generator(permutations)
    with open(output + '.sentence', "a") as f:
        if everything:
            for _ in track(sentences):
                f.write(_ + '\n')
        else:
            counter = 0
            for _ in track(sentences):
                counter += 1
                f.write(_ + '\n')
                if counter > 50:
                    if input("Write more: "+ repl_console) == "N":
                        break
                    else:
                        counter = 0

def generate_sentence(permutations):
    while True:
        main = sentence_from_initials(permutations[0])
        initials = colored(permutations[0], color='cyan')
        main_sentence = f"{colored('[+]', color='green')} {colored(main, color='yellow', attrs=['bold'])}" #": {initials}"
        print(main_sentence, end = " ")
        console.print(initials)
        if input("Generate more: " + repl_console).upper() == "N":
            break

def sentence_from_initials(initial_tuple):
    words_list = [return_word(letter) for letter in initial_tuple]
    tagged_sentence = sentence_maker.from_keyword_list(words_list)
    return sentence_tool.detokenize_tagged(tagged_sentence)

def return_word_offline(char: str) -> str:
    if len(char) > 1:
        randword = words_dict[char[0]]
    else:
        randword = words_dict[char]
    return choice(randword)

def return_word_online(char: str) -> str:
    url = f'https://api.datamuse.com/words?sp={char}*&max=10'
    try:
        response = get(url, timeout=10).text
    except Exception:
        return None
    assert False if 'import' in response else True
    _locals = locals()
    exec('data = ' + response, _locals)
    data = _locals['data']
    if data:
        return data[randrange(len(data))]['word']
    else:
        console.print(response)

def return_word(character: str) -> str:
    online_word = return_word_online(character)
    offline_word = return_word_offline(character)
    if online_word:
        return online_word
    return offline_word

def return_initials():
    initials = []
    while True:
        initial = ""
        word = input("> ")
        if not word:
            break
        word_list = word.split(',') if ',' in word else None
        if word_list:
            for word in word_list:
                initial += word[0].upper()
        else:
            initial = word[0].upper()
        initials.append(initial)
    return initials
