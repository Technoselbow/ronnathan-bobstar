import discord
import random
from discord.ext import commands, tasks

class Gifs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name = "jonathan", brief = "Get gifs for jonathan")
    async def jonathan(self, ctx):
        jonathan_gifs = [
            "https://tenor.com/view/jonathan-joestar-jojo-jojoba-gif-9876465",
            "https://tenor.com/view/jonathan-joestar-shake-my-head-smh-jojos-bizarre-adventure-jonathan-gif-18846963"
        ]
        await ctx.send(random.choice(jonathan_gifs))

    @commands.command(name = "joseph", brief = "Get gifs for joseph")
    async def joseph(self, ctx):
        joseph_gifs = [
            "https://tenor.com/view/joseph-joestar-nice-gif-7319727",
            "https://tenor.com/view/jo-jo-jo-jos-bizarre-adventure-joseph-joestar-anime-opening-gif-15084273",
            "https://tenor.com/view/joseph-joestar-jjba-nigerundayo-smokey-ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhh-gif-19743448"
        ]
        await ctx.send(random.choice(joseph_gifs))

    @commands.command(name = "jotaro", brief = "Get gifs for jotaro")
    async def jotaro(self, ctx):
        jotaro_gifs = [
            "https://tenor.com/view/jotaro-jojo-kujo-jotaro-kujo-star-platinium-gif-19293164",
            "https://tenor.com/view/jojos-bizarre-adventure-anime-jotaro-jotaro-kujo-dancing-gif-17580280   ",
            "https://tenor.com/view/anime-jotaro-jjba-jojo-yare-gif-12243323"
        ]
        await ctx.send(random.choice(jotaro_gifs))

    @commands.command(name = "josuke", brief = "Get gifs for josuke")
    async def josuke(self, ctx):
        josuke_gifs = [
            "https://tenor.com/view/jojo-josuke-higashikata-bam-anime-stylish-pose-gif-16544034",
            "https://tenor.com/view/josuke-josuke-jojo-josuke-higashikata-scream-scared-gif-14400885",
            "https://tenor.com/view/josuke-higashikata-josuke-nijimura-okuyasu-jojo-bizarre-adventure-jojo-gif-16712808",
            "https://tenor.com/view/jojojosuke-josuke-bizzare-gureto-daze-gif-18658827"
        ]
        await ctx.send(random.choice(josuke_gifs))
    
    @commands.command(name = "giorno", brief = "Get gifs for giorno")
    async def giorno(self, ctx):
        giorno_gifs = [
            "https://tenor.com/view/giorno-giovanna-tea-piss-gif-14148345",
            "https://tenor.com/view/giorno-giovanna-try-hard-triggered-minecraft-gif-16346785",
            "https://tenor.com/view/jojo-bizzare-adventure-gifffffer-jojo-nut-giorno-giovanna-gif-14807613"
        ]
        await ctx.send(random.choice(giorno_gifs))
    
    @commands.command(name = "jolyne", brief = "Get gifs for jolyne")
    async def jolyne(self, ctx):
        jolyne_gifs = [
            "https://tenor.com/view/jojo-jolyne-gif-20403991",
            "https://tenor.com/view/jolyne-tired-sleepy-gif-14070200",
            "https://tenor.com/view/jolyne-stone-ocean-jjba-jojo-jojos-bizarre-adventure-gif-17559160"
        ]
        await ctx.send(random.choice(jolyne_gifs))

    @commands.command(name = "johnny", brief = "Get gifs for johnny")
    async def johnny(self, ctx):
        johnny_gifs = [
            "https://tenor.com/view/jesus-johnny-joestar-fortnite-dance-dancing-gif-17600990",
            "https://tenor.com/view/gyro-zeppeli-jojo-pizza-mozzarella-jojo-steel-ball-run-anime-gif-17729028",
        ]
        await ctx.send(random.choice(johnny_gifs))

    @commands.command(name = "josuk8", brief = "Get gifs for josuk8")
    async def josuk8(self, ctx):
        josuk8_gifs = [
            "https://tenor.com/view/josuke-funny-gif-18213896",
        ]
        await ctx.send(random.choice(josuk8_gifs))
    
    @commands.command(name = "stroheim", brief = "Get gifs for stroheim")
    async def stroheim(self, ctx):
        stroheim_gifs = [
            "https://tenor.com/view/rudol-von-stroheim-stroheim-jojos-bizarre-adventure-jojo-battle-tendency-gif-13994621"
        ]
        await ctx.send(random.choice(stroheim_gifs))

def setup(client):
    client.add_cog(Gifs(client))
