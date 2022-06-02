from random import choice
import random

color_test=["R","G","B","Y","P","W"]

hex_color={
    "#FF0F0F":"R",
    "#008000":"G",
    "#63D5CA":"B",
    "#FFFF00":"Y",
    "#A32CC4":"P",
    "#FFFFFF":"W"
}


# color_list=["#B90E0A","#008000","#3944BC","#FFFF00","#A32CC4","#ffffff"] for reference 
def refresh():
    alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9']
    alphabets={
    "A":"",
    "B":"",
    "C":"",
    "D":"",
    "E":"",
    "F":"",
    "G":"",
    "H":"",
    "I":"",
    "J":"",
    "K":"",
    "L":"",
    "M":"",
    "N":"",
    "O":"",
    "P":"",
    "Q":"",
    "R":"",
    "S":"",
    "T":"",
    "U":"",
    "V":"",
    "W":"",
    "X":"",
    "Y":"",
    "Z":"",
    "1":"",
    "2":"",
    "3":"",
    "4":"",
    "5":"",
    "6":"",
    "7":"",
    "8":"",
    "9":"",
    "0":""
    }
    # assign red color randomly for 6 times 
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#FF0F0F"
        alpha_list.remove(ch)

    #assign green color randomly for 6 times
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#008000"
        alpha_list.remove(ch)

    #assign blue color randomly for 6 times
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#63D5CA"
        alpha_list.remove(ch)

    #assign yellow color randomly for 6 times
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#FFFF00"
        alpha_list.remove(ch)

    #assign purple color randomly for 6 times
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#A32CC4"
        alpha_list.remove(ch)

    #assign white color randomly for 6 times
    for i in range(6):
        ch=random.choice(alpha_list)
        alphabets[ch]="#FFFFFF"
        alpha_list.remove(ch)

    return alphabets



