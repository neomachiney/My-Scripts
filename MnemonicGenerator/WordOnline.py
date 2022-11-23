from lib.Globals import repl_console
from lib.Functions import return_word_online
while True:
    while True:
        data = input("Enter character: " + repl_console)
        print(return_word_online(data))
