import nextcord
from random import choice

from lib.Globals import _referrals

class HoneygainButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="HoneygainButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['honeygain']), ephemeral=True)

class IproyalButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="IproyalButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['iproyal']), ephemeral=True)

class EarnappButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="EarnappButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['earnapp']), ephemeral=True)

class PacketstreamButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="PacketstreamButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['packetstream']), ephemeral=True)

class Peer2ProfitButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="Peer2ProfitButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['peer2profit']), ephemeral=True)

class BitpingButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="BitpingButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['bitping']), ephemeral=True)

class TraffmonetizerButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="TraffmonetizerButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['traffmonetizer']), ephemeral=True)

class PicoworkerButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="PicoworkerButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['picoworker']), ephemeral=True)

class AdBtcButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="AdbtcButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['adbtc']), ephemeral=True)

class PresearchButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="PresearchButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message(choice(_referrals['presearch']), ephemeral=True)

class BraveButton(nextcord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="Generate link", style=nextcord.ButtonStyle.gray, custom_id="BraveButton")
    async def gray_button(self, button:nextcord.ui.Button, interaction:nextcord.Interaction):
        await interaction.response.send_message('https://www.brave.com', ephemeral=True)
