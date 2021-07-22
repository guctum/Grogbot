import re

import discord
from datetime import date
import pandas as pd
import csv

def pullInWorkouts(muscle):
    df = pd.read_csv('ExerciseDB.csv')
    muscDf = df.loc[df['Major Muscle'] == muscle]
    randMuscDf = muscDf.sample(n=5)
    muscDict= pd.Series(randMuscDf.Example.values, index=randMuscDf.Exercise).to_dict()
    return muscDict
def getExercise(option):
    if option == "-h":
        current = date.today()
        embedVar = discord.Embed(title="Exercise Commands", description="Commands For Exercise response", color=0x008FFF)
        embedVar.add_field(name="__-arms__", value="5 random arm workouts.", inline=False)
        embedVar.add_field(name="__-legs__", value="5 random leg workouts.", inline=False)
        embedVar.add_field(name="__-chest__", value="5 random chest workouts.", inline=False)
        embedVar.add_field(name="__-core__", value="5 random core workouts.", inline=False)
        embedVar.add_field(name="__-fullbody__", value="5 random full body workouts.", inline=False)
        embedVar.add_field(name="__-all__", value="Add after above commands to see full list of workouts for that major muscle.", inline=False)
        embedVar.add_field(name='\u200B', value='\u200B', inline=False)
        embedVar.set_footer(text="Date ran: " + current.strftime('%m/%d/%Y') + ". Dev: Hunter")
        return embedVar

    if option == "-arms":
        embedVar = discord.Embed(title="Arms", description="Commands For Exercise response",
                                 color=0x008FFF)
        return embedVar

    if option == "-legs":
        embedVar = discord.Embed(title="Legs", description="Commands For Exercise response",
                                 color=0x008FFF)
        return embedVar

    if option == "-chest":
        embedVar = discord.Embed(title="Chest", description="Commands For Exercise response",
                                 color=0x008FFF)
        return embedVar

    if option == "-core":
        embedVar = discord.Embed(title="Core", description="Commands For Exercise response",
                                 color=0x008FFF)
        return embedVar

    if option == "-fullbody":
        embedVar = discord.Embed(title="Full Body", description="Commands For Exercise response",
                                 color=0x008FFF)
        return embedVar

    else:
        embedVar = discord.Embed(title="Not a command", description="If you need help, run command !exercise-h",
                                 color=0x008FFF)
        return embedVar