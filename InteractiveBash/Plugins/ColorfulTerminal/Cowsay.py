import os

from getpass import getuser
from random import choice

filename = "CowsayList"
uid = getuser()
filepath = os.path.dirname(os.path.realpath(__file__))
cowfile = [line.rstrip('\n') for line in open(filepath + "/" + filename)]
random = choice(cowfile)
text = "cowsay -f {} 'Hello {}' ".format(random, uid)

os.system(text)
