import interactions

guild_ids = [764805300229636107]


class help(interactions.Extension):
    def __init__(self, bot):
        self.bot: interactions.Client = bot

    @interactions.extension_command(name="help", description="Shows list of commands", scope=guild_ids)
    async def _help(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**Help**__", value = "\u200b\n`/modhelp` Gives a list of all the moderation commands available\n\n`/aircraft` Gives you a list of the aircraft supported by YourControls\n\n`/install` Shows the instructions on how to install YourControls\n\n`/brokengauge` Shows the list of possible fixes for the Could not connect to the YourControls gauge\n\n`/vatsim` Shows the instructions on how to use YourControls with Vatsim/IVAO\n\n`/nomsg` Shows possible fixes for the No Message Recived From Server error")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="modhelp", description="Shows list of moderation commands", scope=guild_ids)
    async def _modhelp(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**Moderation Commands**__", value = "\u200b\n`/ban` Bans a user\n\n`/kick` Kicks a user\n\n`/mute` Mutes a user\n\n`/unmute` Unmutes a user\n\n`/clear` Clears a number of messages\n\n`/warn` Warns a user")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="aircraft", description="Lists supported aircraft", scope=guild_ids)
    async def _aircraft(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**Aircraft Supported By YourControls**__", value = "\u200b\n`• All Stock Asobo Aircraft`\n`• AeroplaneHeaven C140`\n`• AeroplaneHeaven Electra-10A`\n`• Aerosoft CRJ`\n`• Aerosoft TwinOtter`\n`• BigRadials JRF-6B Goose`\n`• Carenado C170B`\n`• Carenado M20R Ovation`\n`• Carenado PA34T Seneca V`\n`• DCDesigns Concorde`\n`• Deejing RV-7`\n`• FlyByWire A32NX Stable`\n`• FlyByWire A32NX Development`\n`• FlyByWire A32NX Experimental `\n`• FlyInside Bell 47G`\n`• Flysimware C414AW Chancellor`\n`• Headwind A330-900neo`\n`• Heavy Division 78XH `\n`• HypePerformanceGroup H135`\n`• IRIS G115 T.1 Tutor `\n`• IRIS J160-J170 Jabiru`\n`• JPLogistics C152`\n`• JustFlight PA28R Arrow `\n`• JustFlight PA28R TurboArrow`\n`• JustFlight PA28 Warrior`\n`• Magraina C208B EX `\n`• Milviz Porter `\n`• mixMugz TBM930`\n`• Mrtommymxr C172 `\n`• Mrtommymxr DA40NGX`\n`• Mrtommymxr DA62X`\n`• Parallel42 KitFox STi`\n`• PMDG DC6A-B`\n`• RotorSimPilot H125`\n`• RotorSimPilot R44 `\n`• SaltySimulations 747-8i`\n`• SimSkunkWorks TF-104G`")    
        embed.add_field(name = "\u200b", value = "\u200b\n`• SimWorks Kodiak 100 `\n`• SimWorks RV-14`\n`• TheFrett BonanzaG36 `\n`• WorkingTitle CJ4`\n`• Wing42 Boeing 247D`")    
        await ctx.send(embeds=embed, ephemeral=True)

    @interactions.extension_command(name="install", description="Shows how to install YourControls", scope=guild_ids)
    async def _install(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**How To Install YourControls**__", value = "There are two ways to install YourControls either using the installer or by installing it manually. \n\n**Install Using The Installer**\nDownload and run the [installer](https://github.com/sequal32/yourcontrolsinstaller/releases/latest/download/installer.zip). If the installer doesn't launch then you may need to install [WebView2](https://go.microsoft.com/fwlink/p/?LinkId=2124703)\n\n**Manual Install**\nIf you would prefer to install it manually then please follow the instructions listed [here](https://docs.yourcontrols.one/installing#manual-installation).")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="brokengauge", description="Shows possible fixes for the Could Not Connect To The YourControls Gauge error", scope=guild_ids)
    async def _gauge(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**How To Fix Broken YourControls Gauge**__", value = "If you're getting an error which says `Could Not Connect To The YourControls Gauge` one possibility for why YourControls can't connect to the gauge is because when YourControls was installed all or parts of the app were installed to the wrong location.\n\n**Step 1:**\nExit Microsoft Flight Simulator if it's running\n\n**Step 2:**\nDownload, extract and run the installer from [here](https://github.com/Sequal32/yourcontrolsinstaller/releases/download/1.2.4/installer.zip)\n\n**Step 3:**\nVerify the paths are correct. **The first path is the install location** (Where you want to launch YourControls from) and the **second path is the location of your MSFS Community folder.**")        
        embed.set_image(url="https://cdn.discordapp.com/attachments/793511228986097727/928425976352894986/YC_Install.png")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="vatsim", description="Shows the instructions on how to use YourControls with Vatsim/IVAO", scope=guild_ids)
    async def _vatsim(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**How To Use YourControls With Vatsim/IVAO**__", value = "If you are looking to use YourControls with either Vatsim or IVAO then check out the instructions [here](https://docs.yourcontrols.one/vatsim-ivao)")
        await ctx.send(embeds=embed)

    @interactions.extension_command(name="nomsg", description="Shows possible fixes for the No Message Recived From Server error", scope=guild_ids)
    async def _nomsg(self, ctx):
        embed=interactions.Embed(color=0x00d0ff)
        embed.add_field(name = "__**No Message Received From Server**__", value = "There are a number of reasons that you may be getting this error. Check both your firewall and router settings and ensure neither of them are blocking YourControls, or that your ISP is blocking the connection. Also, make sure you both have the latest version of YourControls and try with IPv4 P2P and direct.")
        await ctx.send(embeds=embed)

def setup(bot):
    help(bot)