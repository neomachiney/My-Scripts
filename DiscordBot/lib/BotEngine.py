import asyncio
import nextcord

from random import choice
from lib.Helper import BotHelper
from lib.Globals import _referrals

from lib.Buttons import HoneygainButton, IproyalButton, PacketstreamButton, Peer2ProfitButton, EarnappButton, BitpingButton, TraffmonetizerButton
from lib.Buttons import PicoworkerButton, AdBtcButton, PresearchButton, BraveButton

class BotEngine(nextcord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loop.create_task(self.do_anything_publish())
        # self.loop.create_task(self.create_embed('brave'))

    async def create_embed(self, embed_name):
        await self.wait_until_ready()

        if embed_name.lower() == "honeygain":
            embed = nextcord.Embed(title="Honeygain", description="First passive income app to let you earn money by sharing your bandwidth", color=0xffff00)
            embed.add_field(name="Rate:", value="0.3$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="20$ (None for JMPT withdrawal)", inline=False)
            embed.add_field(name="Payment Option:", value="BTC, JMPT, PayPal", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate varies depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984024976724213800)
            await channel.send(embed=embed, view=HoneygainButton())
        elif embed_name.lower() == "iproyal":
            embed = nextcord.Embed(title="IP Royal Pawns", description="Simple bandwidth sharing app with good earning rate", color=0x808080)
            embed.add_field(name="Rate:", value="0.2$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="5$", inline=False)
            embed.add_field(name="Payment Option:", value="BTC, Visa Gift Card, Amazon Gift Card", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate varies depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114220536823878)
            await channel.send(embed=embed, view=IproyalButton())
        elif embed_name.lower() == "bitping":
            embed = nextcord.Embed(title="Bitping", description="Distributed pinging tool that lets you earn money for pings", color=0xff0000)
            embed.add_field(name="Rate:", value="DEPENDS", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="None", inline=False)
            embed.add_field(name="Payment Option:", value="BSV", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate may vary depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114272869187584)
            await channel.send(embed=embed, view=BitpingButton())
        elif embed_name.lower() == "packetstream":
            embed = nextcord.Embed(title="Packetstream", description="Residential network bandwidth sharing for $$", color=0xffa500)
            embed.add_field(name="Rate:", value="0.1$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="5$", inline=False)
            embed.add_field(name="Payment Option:", value="PayPal", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate may vary depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114312664731678)
            await channel.send(embed=embed, view=PacketstreamButton())
        elif embed_name.lower() == "peer2profit":
            embed = nextcord.Embed(title="Peer2Profit", description="Monetizing internet traffic to earn money", color=0xffa900)
            embed.add_field(name="Rate:", value="0.8$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="2$", inline=False)
            embed.add_field(name="Payment Option:", value="E-Wallet(Qiwi, Payeer etc), Crypto (XMR, LTC, USDT etc)", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate may vary depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114334529642506)
            await channel.send(embed=embed, view=Peer2ProfitButton())
        elif embed_name.lower() == "earnapp":
            embed = nextcord.Embed(title="Earnapp", description="Just another passive income app", color=0x00ff00)
            embed.add_field(name="Rate:", value="0.1$/GB - 0.3$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="2.5$", inline=False)
            embed.add_field(name="Payment Option:", value="PayPal, Amazon Gift Card", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate may vary depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114241739030538)
            await channel.send(embed=embed, view=EarnappButton())
        elif embed_name.lower() == "traffmonetizer":
            embed = nextcord.Embed(title="Traffmonetizer", description="Traffic Monetizer", color=0x0000ff)
            embed.add_field(name="Rate:", value="0.1$/GB", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="10$", inline=False)
            embed.add_field(name="Payment Option:", value="BTC, Paypal", inline=False)
            embed.add_field(name="Platforms Supported:", value="Android, Linux, Windows", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            embed.set_footer(text='\u200bEarning rate may vary depending on your country, traffic demand, network speed and number of devices')
            channel = await self.fetch_channel(984114682115792906)
            await channel.send(embed=embed, view=TraffmonetizerButton())
        elif embed_name.lower() == "picoworker":
            embed = nextcord.Embed(title="Picoworker", description="An online marketplace that connects freelancers and business owners around the world with easy-to-do affordable tasks.", color=0x22aa58)
            embed.add_field(name="Rate:", value="0.01$-1$ per task", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="5$", inline=False)
            embed.add_field(name="Payment Option:", value="Litecoin, Airtm, Paypal, Skrill, Uphold", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            channel = await self.fetch_channel(984337595762880562)
            await channel.send(embed=embed, view=PicoworkerButton())
        elif embed_name.lower() == "adbtc":
            embed = nextcord.Embed(title="AdBTC", description="Earn money for watching websites", color=0x2d3545)
            embed.add_field(name="Rate:", value="5-30 sat/per ad", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="1000 sat (0.00001000 BTC)/0.15$ approximate.", inline=False)
            embed.add_field(name="Payment Option:", value="BTC, Faucetpay, etc", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            channel = await self.fetch_channel(984337673890185226)
            await channel.send(embed=embed, view=AdBtcButton())
        elif embed_name.lower() == "presearch":
            embed = nextcord.Embed(title="Presearch", description="Search engine that pays and respect your privacy.", color=0x2c8efe)
            embed.add_field(name="Rate:", value="0.05-0.10 presearch token per search (30 paid search daily)", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="1000 presearch token", inline=False)
            embed.add_field(name="Payment Option:", value="Presearch Token (ERC-20)", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            channel = await self.fetch_channel(984337989176000532)
            await channel.send(embed=embed, view=PresearchButton())
        elif embed_name.lower() == "brave":
            embed = nextcord.Embed(title="Brave Browser", description="Browser that pays your for personalised private ads", color=0xf0442b)
            embed.add_field(name="Rate:", value="0.01-0.10 BAT/per ad", inline=False)
            embed.add_field(name="Minimum Withdrawal:", value="Unknown", inline=False)
            embed.add_field(name="Payment Option:", value="BAT", inline=False)
            embed.add_field(name="Join:", value="Click on generate link below", inline=False)
            channel = await self.fetch_channel(984442624398196766)
            await channel.send(embed=embed, view=BraveButton())

    async def do_anything_publish(self):
        await self.wait_until_ready()
        corona_channel = self.get_channel(790767464229109811)
        personal_channel = self.get_channel(803301891772907552)
        while True:
            helper = BotHelper()
            await corona_channel.send(helper.corona_string)
            #await personal_channel.send(helper.personal_string)
            await asyncio.sleep(86400)

    async def on_ready(self):
        print(f'Logged in as: {self.user.name}({self.user.id})')

        self.add_view(HoneygainButton())
        self.add_view(IproyalButton())
        self.add_view(PacketstreamButton())
        self.add_view(Peer2ProfitButton())
        self.add_view(EarnappButton())
        self.add_view(BitpingButton())
        self.add_view(TraffmonetizerButton())
        self.add_view(PicoworkerButton())
        self.add_view(AdBtcButton())
        self.add_view(PresearchButton())
        self.add_view(BraveButton())

