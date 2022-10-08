import discord
from discord import message
from discord import colour
from discord import member
from discord.activity import CustomActivity
from discord.ext import commands
from discord.ext.commands import cog
from discord.ext.commands.core import command, has_permissions


client = commands.Bot(command_prefix = "p!")

# Iniciando bot

@client.event
async def on_ready():
    print("Iniciando bot")
    print("Iniciando secion como {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="ForgeCub Development"))

# Logger de mensajes

#@client.event
#async def on_message(message):
#    await client.process_commands(message)
#    if message.author == client.user:
#        return

#    usuario = str(message.author).split('#')[0]
#    mensaje_usuario = str(message.content)
#    canal = str(message.channel.name)

#    logger = (f"{usuario} {mensaje_usuario} {canal}")

#    print(logger)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(description="Argumentos faltantes, `usa r!help (comando) para ver mas informacion`", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
        
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(description="No tienes permisos para hacer eso :rolling_eyes:", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(description="Comando no encontrado, `usa r!help para ver la lista de comandos`", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)        

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.kick_members or ctx.message.author.guild_permissions.administrator or ctx.author.id == 424324326724993034:
        if member == ctx.message.author:
            embed=discord.Embed(description="No puedes banearte a ti mismo", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return

        if member.guild_permissions.administrator:
            embed=discord.Embed(description="No puedes banear a un admin :rage:", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return

        if reason == None:
            embed=discord.Embed(description="Se necesita un motivo valido", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return

        await ctx.guild.ban(member)
        embed=discord.Embed(title="Usuario baneado", description=f"{member.mention} ha sido baneado \nmotivo: `{reason}`\nBaneado por: {ctx.author.mention}", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

    else:
        embed=discord.Embed(description="No tienes permisos para hacer eso :rolling_eyes:", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

@client.command()
async def unban(ctx, *, member):
    if ctx.message.author.guild_permissions.ban_members or ctx.message.author.guild_permissions.administrator or ctx.author.id == 424324326724993034:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(title="Usuario desbaneado", description=f"{user.mention} ha sido desbaneado", color=discord.Color.dark_blue())
                await ctx.send(embed=embed)
                return
                
    else:
        embed=discord.Embed(description="No tienes permisos para hacer eso :rolling_eyes:", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.kick_members or ctx.message.author.guild_permissions.administrator or ctx.author.id == 424324326724993034:
        if member == ctx.message.author:
            embed=discord.Embed(description="No puedes expulsarte a ti mismo", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return
        
        if member.guild_permissions.administrator:
            embed=discord.Embed(description="No puedes expulsar a un admin :rage:", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return

        if reason == None:
            embed=discord.Embed(description="Se necesita un motivo valido", color=discord.Color.dark_blue())
            await ctx.send(embed=embed)
            return

        await ctx.guild.kick(member)
        embed=discord.Embed(title="Usuario expulsado", description=f"{member.mention} ha sido expulsado \nmotivo: `{reason}`\nExpulsado por: {ctx.author.mention}", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(description="No tienes permisos para hacer eso :rolling_eyes:", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)


@client.command()
async def prueba(ctx, member: discord.Member):
    if member == ctx.message.author:
        embed=discord.Embed(description="eres tu", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
        return
        
    if member.guild_permissions.administrator:
        embed=discord.Embed(description="es un admin", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
        return

    embed=discord.Embed(description="no eres tu ni un admin", color=discord.Color.dark_blue())
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, cantidad=0):
    if cantidad == 0:
        embed=discord.Embed(description="Por favor pon una cantidad", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)
    else:
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=cantidad)
        embed=discord.Embed( description="Borrado :thumbsup:", color=discord.Color.dark_blue())
        await ctx.send(embed=embed)

@client.command()
async def anuncio(ctx, titulo, *, descripcion):
    embed=discord.Embed(title=f"{titulo}", description=f"{descripcion}", color=discord.Color.dark_blue())
    embed.set_author(name="Anuncio", icon_url=ctx.author.avatar_url)
    #embed.set_thumbnail(url=" ")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@client.command()
async def decir(ctx, *, mensaje):
    embed=discord.Embed(description=f"{mensaje}", color=discord.Color.dark_blue())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@client.command()
async def admin(ctx):
    embed=discord.Embed(title="Toca aqui para convertirte en admin", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="Quieres convertirte en admin del servidor? :flushed: toca el titulo", color=discord.Color.dark_blue())
    await ctx.send(embed=embed)

client.run("TOKEN")
