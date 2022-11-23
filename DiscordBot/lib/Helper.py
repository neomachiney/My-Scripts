from datetime import datetime
from humanize import intcomma

from lib.Functions import fetch_corona_infection
from lib.Globals import _repositories

class BotHelper:
    def __init__(self):
        self.corona_string = self.corona()
        #self.personal_string = self.personal()

    def corona(self):
        send_string = ""
        infection, death = fetch_corona_infection()
        send_string += f"**SARS-CoV-2 Status** ({datetime.now().strftime('%B %d %Y %H:%M:%S')})\n"
        send_string += f"Infection: {intcomma(infection)}\nDeath: {intcomma(death)}\n"
        return send_string

    # def personal(self):
        # send_string = ""
        # for _ in _repositories:
            # active, closed = fetch_pulls(f"https://github.com/{_}/pulls")
            # reponame = _.split('/')[-1]
            # reponame = repo_names[f"{_.split('/')[-1]}"]
            # send_string += f"**{reponame}**: \nActive: {intcomma(active)} :white_check_mark:, Total: {intcomma(active + closed)} :skull_crossbones:\n"
        # return send_string
