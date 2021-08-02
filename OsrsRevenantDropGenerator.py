"""
#     |======================================================|
#     |Formula made by Mod Ash                               |
#     |Code written by CrownMauler/Red X 500/RedX1000        |
#     |Contact me at Discord: RedX1000#3655                  |
#     |Based on this                                         |
#     |https://pbs.twimg.com/media/DpbCbE_WkAYCD6L.jpg:large |
#     |======================================================|
"""

import math
import random
from tkinter import *
from winsound import *
import webbrowser


import tkinter as tk

#Look into changing randint with uniform


#function for Skulled and Entry retreival
def skullCheck(x):
    if x == 1:
        skull = 1
        print("Skulled")
    else:
        skull = 0
        print("Not skulled")

def killsGrab():
    kills = entry.get()

def verify(sk,kill):
    if sk == 1:
        print("You are skulled. You have "+str(kill)+" kills")
    else:
        print("You are not skulled. You have "+str(kill)+" kills")

def itemImages():

    dropItemImageName = ["Revenant_ether_5.png","Coins_10000.png","Amulet_of_avarice.png","Craw's_bow_(u).png",
                         "Thammaron's_sceptre_(u).png","Viggora's_chainmace_(u).png","Ancient_emblem.png",
                         "Ancient_totem.png","Ancient_statuette.png","Ancient_crystal.png","Ancient_medallion.png",
                         "Ancient_effigy.png","Ancient_relic.png","Bracelet_of_ethereum_(uncharged).png",
                         "Battlestaff.png","Rune_full_helm.png","Rune_platebody.png","Rune_platelegs.png",
                         "Rune_kiteshield.png","Rune_warhammer.png","Dragon_platelegs.png","Dragon_plateskirt.png",
                         "Dragon_dagger.png","Dragon_longsword.png","Dragon_med_helm.png","Dragonstone_bolt_tips_5.png",
                         "Onyx_bolt_tips_5.png","Death_rune.png","Blood_rune.png","Law_rune.png","Coal.png",
                         "Adamantite_bar.png","Runite_ore.png","Runite_bar.png","Black_dragonhide.png",
                         "Mahogany_plank.png","Manta_ray.png","Yew_logs.png","Magic_logs.png","Uncut_dragonstone.png",
                         "Magic_seed_5.png","Revenant_cave_teleport.png","Super_restore(4).png"]

    dropItemImage = []
    for i in range(0,len(dropItemImageName)):
        x = PhotoImage(file="RevenantFiles/images/"+dropItemImageName[i])
        dropItemImage.append(x)

    dropItemX = [450,550,650,650,740,740,450,450,550,550,650,650,750,450,450,450,550,550,550,650,650,650,750,750,750,450,
             530,610,690,770,450,450,450,450,550,550,550,550,650,650,650,650,750]
    dropItemY = [50,50,50,88,50,88,130,165,130,165,130,165,130,230,265,300,230,265,300,230,265,300,230,265,300,375,375,375,
             375,375,445,480,515,550,445,480,515,550,445,480,515,550,445]

    for i in range(0,len(dropItemImageName)):
        x = Label(root, image = dropItemImage[i], background = "#808080")
        x.image = dropItemImage[i]
        x.place(x=dropItemX[i],y=dropItemY[i])

#Mediocre Drops
#You have a 91/106 chance to not get a bracelet.
#You can see what all of the drops are for the
#Mediocre Drops table in the attached link.
def mediocreDrops(totalDrops):
    aMedDrops = int(random.randint(1,106))
    if aMedDrops == 1:
        totalDrops[20] += 1
    elif aMedDrops == 2:
        totalDrops[21] += 1
    elif aMedDrops == 3 or aMedDrops == 4:
        totalDrops[15] += 1
    elif aMedDrops == 5 or aMedDrops == 6:
        totalDrops[16] += 1
    elif aMedDrops == 7 or aMedDrops == 8:
        totalDrops[17] += 1
    elif aMedDrops == 9 or aMedDrops == 10:
        totalDrops[18] += 1
    elif aMedDrops == 11 or aMedDrops == 12:
        totalDrops[19] += 1
    elif aMedDrops == 13:
        totalDrops[23] += 1
    elif aMedDrops == 14:
        totalDrops[22] += 1
    elif aMedDrops >= 15 and aMedDrops <= 18:
        totalDrops[42] += 1
    elif aMedDrops >= 19 and aMedDrops <= 22:
        totalDrops[26] += 1
    elif aMedDrops >= 23 and aMedDrops <= 26:
        totalDrops[25] += 1
    elif aMedDrops == 27:
        totalDrops[39] += 1
    elif aMedDrops >= 28 and aMedDrops <= 30:
        totalDrops[27] += 1
    elif aMedDrops >= 31 and aMedDrops <= 33:
        totalDrops[28] += 1
    elif aMedDrops >= 34 and aMedDrops <= 36:
        totalDrops[29] += 1
    elif aMedDrops >= 37 and aMedDrops <= 42:
        totalDrops[32] += 1
    elif aMedDrops >= 43 and aMedDrops <= 48:
        totalDrops[31] += 1
    elif aMedDrops >= 49 and aMedDrops <= 54:
        totalDrops[30] += 1
    elif aMedDrops >= 55 and aMedDrops <= 59:
        totalDrops[14] += 1
    elif aMedDrops >= 60 and aMedDrops <= 65:
        totalDrops[34] += 1
    elif aMedDrops >= 66 and aMedDrops <= 70:
        totalDrops[35] += 1
    elif aMedDrops == 71 or aMedDrops == 72:
        totalDrops[38] += 1
    elif aMedDrops >= 73 and aMedDrops <= 75:
        totalDrops[37] += 1
    elif aMedDrops >= 76 and aMedDrops <= 78:
        totalDrops[36] += 1
    elif aMedDrops >= 79 and aMedDrops <= 84:
        totalDrops[33] += 1
    elif aMedDrops >= 85 and aMedDrops <= 91:
        totalDrops[41] += 1
    else:
        totalDrops[13] += 1
    return totalDrops

#This is the table for the Good Drops
#This table has the weapons, ancient items,
#dragon med, and magic seeds

def goodDrops(skull,totalDrops):
    if skull == 1:
        aGoodDrops = int(random.randint(0,13))
    else:
        aGoodDrops = int(random.randint(0,39))

    #Here's what you've got!
    if aGoodDrops == 0:
        wepRandom = random.randint(1,5)
        if wepRandom == 1:
            totalDrops[5] += 1
        elif wepRandom == 2:
            totalDrops[3] += 1
        elif wepRandom == 3:
            totalDrops[4] += 1
        else:
            totalDrops[2] += 1

    elif aGoodDrops == 1:
        totalDrops[12] += 1

    elif aGoodDrops == 2:
        totalDrops[11] += 1

    elif aGoodDrops >= 3 and aGoodDrops <= 4:
        totalDrops[10] += 1

    elif aGoodDrops >= 5 and aGoodDrops <= 8:
        totalDrops[8] += 1

    elif aGoodDrops >= 9 and aGoodDrops <= 12:
        seeds = random.randint(5,9)
        totalDrops[40] += 1

    elif aGoodDrops >= 13 and aGoodDrops <= 15:
        totalDrops[9] += 1

    #|=====================================================|//
    #|Cannot obtain anything past this point while skulled.|//
    #|=====================================================|//

    elif aGoodDrops >= 16 and aGoodDrops <= 20:
        totalDrops[7] += 1

    elif aGoodDrops >= 21 and aGoodDrops <= 26:
        totalDrops[6] += 1

    elif aGoodDrops >= 27 and aGoodDrops <= 39:
        totalDrops[24] += 1

    return totalDrops

def menu(skullS,killsS,levelS,outputBoxX,outputBoxY):
    skull = int(skullS)
    kills = int(killsS)
    level = int(levelS)
    totalKills = 0

    totalDrops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    totalCalculatedDrops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0,kills):
        totalDrops[0] += 1
        totalDrops[1] += 1

        chanceA = 0.0
        chanceB = 0.0

        clampedLevel = level

        #Formula for chanceA
        chanceA = 2200 / int(math.sqrt(clampedLevel))
        chanceA = int(chanceA)

        #Formula for chanceB
        chanceB = 15 + (math.pow((level + 60), 2)/ 200)
        chanceB = int(chanceB)

        #This will randomize a number,
        #A is set between 0 and (chanceA - 1) inclusive
        a = int(random.randint(0,(chanceA - 1)))

        if(a == 1):
            goodDrops(skull,totalDrops)
        elif a == 0 or a >= 2 and a <= 86:
            mediocreDrops(totalDrops)

        totalKills += 1
        #print(totalKills)


    for i in range(0,len(totalDrops)):
        if i == 0: #Ether
            for j in range(0,totalDrops[i]):
                if level == 7:
                    num = random.randint(1,3)
                    totalCalculatedDrops[i] += num
                elif level == 15:
                    num = random.randint(1,4)
                    totalCalculatedDrops[i] += num
                elif level == 52:
                    num = random.randint(1,8)
                    totalCalculatedDrops[i] += num
                elif level == 60:
                    num = random.randint(1,8)
                    totalCalculatedDrops[i] += num
                elif level == 82:
                    num = random.randint(1,10)
                    totalCalculatedDrops[i] += num
                elif level == 90:
                    num = random.randint(1,10)
                    totalCalculatedDrops[i] += num
                elif level == 98:
                    num = random.randint(1,10)
                    totalCalculatedDrops[i] += num
                elif level == 105:
                    num = random.randint(1,11)
                    totalCalculatedDrops[i] += num
                elif level == 120:
                    num = random.randint(1,11)
                    totalCalculatedDrops[i] += num
                elif level == 126:
                    num = random.randint(1,12)
                    totalCalculatedDrops[i] += num
                elif level == 135:
                    num = random.randint(1,12)
                    totalCalculatedDrops[i] += num
        elif i == 1: #Coins
            for j in range(0,totalDrops[i]):
                if level == 7:
                    num = random.randint(1,51)
                    totalCalculatedDrops[i] += num
                elif level == 15:
                    num = random.randint(1,76)
                    totalCalculatedDrops[i] += num
                elif level == 52:
                    num = random.randint(1,176)
                    totalCalculatedDrops[i] += num
                elif level == 60:
                    num = random.randint(1,176)
                    totalCalculatedDrops[i] += num
                elif level == 82:
                    num = random.randint(1,226)
                    totalCalculatedDrops[i] += num
                elif level == 90:
                    num = random.randint(1,226)
                    totalCalculatedDrops[i] += num
                elif level == 98:
                    num = random.randint(1,226)
                    totalCalculatedDrops[i] += num
                elif level == 105:
                    num = random.randint(1,251)
                    totalCalculatedDrops[i] += num
                elif level == 120:
                    num = random.randint(1,251)
                    totalCalculatedDrops[i] += num
                elif level == 126:
                    num = random.randint(1,276)
                    totalCalculatedDrops[i] += num
                else:
                    num = 0
                    totalCalculatedDrops[i] += num
        elif i == 42: #Super Restore
            for j in range(0,totalDrops[i]):
                num = random.randint(3, 5)
                totalCalculatedDrops[i] += num
        elif i == 26: #Onyx Tips
            for j in range(0,totalDrops[i]):
                num = random.randint(5,10)
                totalCalculatedDrops[i] += num
        elif i == 25: #Dstone Tips
            for j in range(0,totalDrops[i]):
                num = random.randint(40,70)
                totalCalculatedDrops[i] += num
        elif i == 39: #Dstone
            for j in range(0,totalDrops[i]):
                num = random.randint(5,7)
                totalCalculatedDrops[i] += num
        elif i == 27: #Death Runes
            for j in range(0,totalDrops[i]):
                num = random.randint(60,100)
                totalCalculatedDrops[i] += num
        elif i == 28: #Blood Runes
            for j in range(0,totalDrops[i]):
                num = random.randint(60,100)
                totalCalculatedDrops[i] += num
        elif i == 29: #Law Runes
            for j in range(0,totalDrops[i]):
                num = random.randint(60,100)
                totalCalculatedDrops[i] += num
        elif i == 32: #Runite Ore
            for j in range(0,totalDrops[i]):
                num = random.randint(3,6)
                totalCalculatedDrops[i] += num
        elif i == 31: #Adamant Bars
            for j in range(0,totalDrops[i]):
                num = random.randint(8,12)
                totalCalculatedDrops[i] += num
        elif i == 30: #Coal
            for j in range(0,totalDrops[i]):
                num = random.randint(50,100)
                totalCalculatedDrops[i] += num
        elif i == 14: #Battlestaves
            for j in range(0,totalDrops[i]):
                num = 3
                totalCalculatedDrops[i] += num
        elif i == 34: #Black Dragonhide
            for j in range(0,totalDrops[i]):
                num = random.randint(10,15)
                totalCalculatedDrops[i] += num
        elif i == 35: #Mahogany Planks
            for j in range(0,totalDrops[i]):
                num = random.randint(15,25)
                totalCalculatedDrops[i] += num
        elif i == 38: #Magic Logs
            for j in range(0,totalDrops[i]):
                num = random.randint(15,25)
                totalCalculatedDrops[i] += num
        elif i == 37:#Yew Logs
            for j in range(0,totalDrops[i]):
                num = random.randint(60,100)
                totalCalculatedDrops[i] += num
        elif i == 36:#Manta Ray
            for j in range(0,totalDrops[i]):
                num = random.randint(30,50)
                totalCalculatedDrops[i] += num
        elif i == 33:#Rune bars
            for j in range(0,totalDrops[i]):
                num = random.randint(3,5)
                totalCalculatedDrops[i] += num
        elif i == 41:#Teleport scroll
            for j in range(0,totalDrops[i]):
                num = 1
                totalCalculatedDrops[i] += num
        elif i == 40:#Magic seeds
            for j in range(0,totalDrops[i]):
                num = random.randint(5,9)
                totalCalculatedDrops[i] += num
        else:#Everything that doesn't stack
            for j in range(0,totalDrops[i]):
                num = 1
                totalCalculatedDrops[i] += num

    outputBox = []

    for i in range(0,len(totalDrops)):
        Label(root,text="                               ",background="#808080").place(x=outputBoxX[i],y=outputBoxY[i])

    itemImages()

    for i in range(0,len(totalDrops)):
        x = Label(root,text=totalCalculatedDrops[i],background="#808080")
        outputBox.append(x)

    for i in range(0,len(outputBox)):
        outputBox[i].place(x=outputBoxX[i],y=outputBoxY[i])

    #It's going out of range
    #Learn to remove old labels

root = Tk()
root.title("Oldschool Runescape Revenant Generator")
root.geometry("860x657")

#Background Canvases
lootColor = "#686868"

c1 = Canvas(width=430, height = 665)
c1.create_rectangle(0,0,430,665,fill="#1ad3b4")
c1.place(x=-5,y=-5)

c2 = Canvas(width=440, height = 665)
c2.create_rectangle(0,0,440,665,fill="#808080")
c2.place(x=420,y=-5)

c3 = Canvas(width=100,height=100)
c3.create_rectangle(100,100,100,100,fill="#16ac93")
c3.grid(row=7,column=1)

#Main Labels

mainl = Label(root, text ="Welcome to the Revenent Drop Generator",font=10,background="#16ac93")
mainl.place(x=70,y=0)

main2 = Label(root, text ="Written by \nRedX1000/CrownMauler",font=10,background="#16ac93")
main2.place(x=125,y=20)

main3 = Label(root, text ="Here is your Revenant loot!",font=10,background=lootColor)
main3.place(x=545,y=0)

main4 = Label(root, text ="Enter the amount of \nkills, choose if you\n are skulled or not\n and then click"
                          +"\n the revenant to begin!", font=10,background="#16ac93")
main4.place(x = 130,y= 75)

main5 = Label(root,text="Because I can't multithread\n to save my life, there is\nno loading bar and the \nprogram will freeze for a bit"
                        +".\n If you put in a large\n order, be prepared to wait!",font=10,background = "#16ac93")
main5.place(x = 112,y= 340)

#Grid Placeholders

blank = PhotoImage(file="RevenantFiles/images/blank.png")
empty0l = Label(root, text = "",background="#1ad3b4")
empty0l.grid(row=0,column=1)

emptyl = Label(root, image = blank)
emptyl.grid(row=1,column=1)

empty2 = Label(root, image = blank,)
empty2.grid(row=7,column=2)

empty3 = Label(root, image = blank,)
empty3.grid(row=7,column=3)

empty4 = Label(root, image = blank)
empty4.grid(row=1,column=4)


#Drop Labels
dropLabels = ["Ether","Coins","Uniques","Ancient Statuettes","Weapons & Armour","Runes & Ammunition",
              "Resources, Teleports, & Super Restores"]

dropLabelsX = [450,550,650,450,450,450,450]
dropLabelsY = [25,25,25,100,200,345,415]
for i in range(0,len(dropLabels)):
    x = Label(root,text=dropLabels[i],font=10,background=lootColor)
    x.place(x=dropLabelsX[i],y=dropLabelsY[i])

#Drop Icons
itemImages()

#Skulled Toggle

v = IntVar()
v.set(2)
skLabel = Label(root,text="Are you skulled?",background="#16ac93",font=10).place(x=150,y=270)
Radiobutton(root,text="Skulled     ",variable=v,value=1,font=10,background="#16ac93",activebackground="#16ac93").place(x=116,y=292)
Radiobutton(root,text="Not skulled ",variable=v,value=2,font=10,background="#16ac93",activebackground="#16ac93").place(x=195,y=292)


#Entry Box, Enter Button, and URL button
entryLabel = Label(root,text="Enter kills here",font=10,background="#16ac93")
entryLabel.place(x=157,y=205)

entry = Entry(root)
entry.place(x=148,y=235)


def openweb():
    webbrowser.open(url,new=new)

new = 1
url = "https://pbs.twimg.com/media/DpbCbE_WkAYCD6L.jpg:large"
urlB = Button(root,text="Click here to open\nthe original formula\npage posted on Mod\nAsh's twitter page",
              font=10,background="#16ac93",command = lambda: openweb())
urlB.place(x=129,y=559)

#Output Boxes and drops lists
totalDrops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
totalCalculatedDrops = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

outputBox = []
la = Label(root,text="")
outputBox.append(la)
for i in range(1,len(totalDrops)):
    la = Label(root,text="")
    outputBox.append(la)
    outputBox[i].place(x=1000,y=1000)

outputBoxX = [490,590,690,690,790,790,490,490,590,590,690,690,790,490,490,490,590,590,590,690,690,690,790,790,790,
              485,565,645,725,805,490,490,490,490,590,590,590,590,690,690,690,690,790]
outputBoxY = [55,55,55,93,55,93,135,170,135,170,135,170,135,235,270,305,235,270,305,235,270,305,235,270,305,380,380,
              380,380,380,450,485,520,555,450,485,520,555,450,485,520,555,450]

#Music player
def play():
    return PlaySound("RevenantFiles/sounds/Revenants.wav", SND_FILENAME | SND_ASYNC)

def pause():
    return PlaySound("RevenantFiles/sounds/Silent.wav", SND_FILENAME | SND_ASYNC)

vMus = IntVar()
vMus.set(2)
Label(root,text=" Music Player!\nTrack: Revenants",background="#16ac93",font=10).place(x=147,y=475)
Radiobutton(root,text="On         ",variable=vMus,value=1,font=10,background = "#16ac93",
            activebackground="#16ac93",command = lambda: play()).place(x=147,y=517)
Radiobutton(root,text="Off",variable=vMus,value=2,font=10,background = "#16ac93",
            activebackground="#16ac93",command = lambda: pause()).place(x=223,y=517)
#Revenant Buttons
revenantImageName= ["RevenantFiles/images/imp.png","RevenantFiles/images/goblin.png",
                    "RevenantFiles/images/pyrefiend.png","RevenantFiles/images/hobgoblin.png",
                    "RevenantFiles/images/cyclops.png","RevenantFiles/images/hellhound.png",
                    "RevenantFiles/images/demon.png","RevenantFiles/images/ork.png",
                    "RevenantFiles/images/dark_beast.png","RevenantFiles/images/knight.png",
                    "RevenantFiles/images/dragon.png"]

revenantImage = []

for i in range(0,len(revenantImageName)):
    x = PhotoImage(file=revenantImageName[i])
    revenantImage.append(x)

revenantRow = [1,2,3,4,5,1,2,3,4,5,6]
revenantColumn = [1,1,1,1,1,4,4,4,4,4,4]
revenantLevels = [7,15,52,60,82,90,98,105,120,126,135]
for i in range(0,11):
    x = Button(root, image = revenantImage[i], background = "#a0a0a0",command = lambda i=i: (menu(v.get(),entry.get(),
                                    revenantLevels[i],outputBoxX,outputBoxY),(itemImages())))
    x.grid(row=revenantRow[i],column=revenantColumn[i])

root.mainloop()
