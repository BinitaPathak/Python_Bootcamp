# Project Assignment-1

# An Application which tells future based upon the zodiac sign

# assign True in Variable Val
Val = True

# When Val become true then only the loop executed
while Val:
    # here we are using multi statement print function
    print('''       
    1) Aries
    2) Taurus
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    # here user enter their zodiac sign number
    s = int(input("Pick your sign number and press enter\n"))
    print(s)

    # IF-ELIF-ELSE will check the user input
    if s == 1:
        print("Aries")
    elif s == 2:
        print("Taurus")
    elif s == 3:
        print("Gemini")
    elif s == 4:
        print("Cancer")
    elif s == 5:
        print("Leo")
    elif s == 6:
        print("Virgo")
    elif s == 7:
        print("Libra")
    elif s == 8:
        print("Scorpio")
    elif s == 9:
        print("Sagittarius")
    elif s == 10:
        print("Capricorn")
    elif s == 11:
        print("Aquarius")
    elif s == 12:
        print("Pisces")
    else:
        print("Hey you sure about the number?")

    temp = input("Shall we do it again? (Y/N)")

    # when user input Y then only loop execute else it terminate.
    Val = True if temp == "Y" else False
