"""
The following code is for the trivia bot found on the JakeMac discord server.
This is the piece of code that interacts with the actual discord server. Pretty much the front end of it.

Author: Kenny Blake
2/14/18

"""
import discord
from discord.ext import commands
import trivia 

answered = 0

client = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*1000)}ms")

@client.command()
async def answer(ctx, ans : str):
    global answered
    if ctx.channel.name == "jedi-gang":
        role = "Jedi"
    elif ctx.channel.name == "sith-gang":
        role = "Sith"
    else:
        ctx.send("Sorry, you must play in either the jedi-gang chatroom , or the sith-gang chatroom.")
    correct = trivia.t.checkAnswer(ans, role)
    if correct:
        q = trivia.t.getQuestion(answered)
        await ctx.send(f"Correct!")
        if q == "j":
            await ctx.send("Game Over! Jedi's Win!")
            await client.close()
        elif q == "s":
            await ctx.send("Game Over! Sith's Win!")
            await client.close()
        else:
            await ctx.send(q)
    else:
        await ctx.send("Incorrect. Try again!")
        
    answered += 1


@client.command()
@commands.has_permissions(manage_messages = True)
async def startgame(ctx, ch1 : discord.TextChannel, ch2 : discord.TextChannel):
    global answered
    await ctx.send(f"""Welcome to the JakeMac server Official Trivia Game!
    -Created by: Kenny Blake
    
    -The objective of the game is to be the first team to get 5 questions right!
    
    -The games are between the Sith, and the Jedi.

    -Remember! You are all on a team!
    """)

    q = trivia.t.getQuestion(answered)
    if q == False:
        await ctx.send("Thanks for playing!")
        await client.close()
    else:
        await ctx.send(f"""Welcome to the JakeMac server Official Trivia Game!
            -Created by: Kenny Blake
            
            -The objective of the game is to be the first team to get 5 questions right!
            
            -The games are between the Sith, and the Jedi.

            -Remember! You are all on a team!
            """)

        await ch1.send(f"""Welcome to the JakeMac server Official Trivia Game!
        -Created by: Kenny Blake
        
        -The objective of the game is to be the first team to get 5 questions right!
        
        -The games are between the Sith, and the Jedi.

        -Remember! You are all on a team!
        """)
        await ch2.send(f"""Welcome to the JakeMac server Official Trivia Game!
        -Created by: Kenny Blake
        
        -The objective of the game is to get the most questions correct!
        
        -The games are between the Sith, and the Jedi.

        -Remember! You are all on a team!

        -To answer questions, type ;answer [your answer here]

        -for help, type ;help
        """)
        await ch1.send(q)
        await ch2.send(q)

@client.event
async def on_command_error(ctx, error: discord.errors):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to do that!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist!")


client.run('Left this part out on github.')