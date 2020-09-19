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
    s = input("Pick your sign number and press enter\n")

    # IF-ELIF-ELSE will check the user input
    if s == "1":
        print('''Aries : You will be somehow good. Money which was stuck will be recovered now, it will increase liquidity in
              the business. There will be some good news in terms of job, your performance will be good,
              and you will expect promotions. There will be some good news in terms of legal matters also.''')
    elif s == "2":
        print('''Taurus : Today, you may feel a positive energy. You may plan for higher studies to groom your career.
         You may be busy with the kids. Students are advised to focus themselves towards their studies to achieve their 
        desired goal.''')
    elif s == "3":
        print('''Gemini : the moon is not favourable for you. Situations may be somehow disappointing; you may be 
        impatient and not able to focus towards your goals. Investments in the fixed assets are advised to be postponed
         for a while.''')
    elif s == "4":
        print('''Cancer : you may likely feel internal strength; your internal energy may be helpful to complete your
         projects before the timeline. You may likely hear some good news related to siblings. There may likely to
          be some short trips related to business also possible.''')
    elif s == "5":
        print('''Leo: you will be happy. You will spend good time with your family or friends; you may buy something 
        for family or friends. Domestic harmony will be improved but you are advised to control your 
        straightforwardness and harsh speaking.''')
    elif s == "6":
        print('''Virgo : you will be happy. You will spend good time with your family or friends; you may buy 
        something for family or friends. Domestic harmony will be improved but you are advised to control your 
        straightforwardness and harsh speaking.''')
    elif s == "7":
        print('''Libra : you will feel dull; you will feel negativity pulling you back from making strong decisions, 
        which will affect your professional commitments. You will not be able to complete the task on time. It is 
        advised to avoid adventure tours or rush driving.''')
    elif s == "8":
        print('''Scorpio : your losses will convert into profits now, which will increase your liquidity in the 
        business. You will generate some extra income. Kids' health will improve now. Love bird will make some 
        decisions in terms of marriage. With the help of wisdom, you will keep yourself safe from conspiracy against 
        you.''')
    elif s == "9":
        print('''Sagittarius : you will be busy at work. You will plan to make investments in the business in terms 
        of growth. You will be able to implement your plans easily, which will boost your confidence. You will be 
        praised by your seniors; you will expect to get some important position in your work.''')
    elif s == "10":
        print('''Capricorn : you will get ample opportunities in terms of work, which will grow your work. With the 
        help of an influential person in terms of the partnership, you will get benefits in terms of your work. There 
        will be mental peace and happiness around you. Job seekers will hear good news in terms of suitable jobs. You 
        will plan to visit some spiritual places.''')
    elif s == "11":
        print('''Aquarius : the moon is negative, there will be some dullness in your nature, you will be arrogant, 
        and it will affect your professional and domestic life. It is advised to drive safely and shall avoid going 
        on adventure tours. Couples and love birds are advised to keep some distance and control their tongue while 
        speaking.''')
    elif s == "12":
        print('''Pisces : you will be blessed by a positive moon. Things will be under control now. In partnerships, 
        many issues will be resolved. You will start implementing new plans in your business. Students will make 
        quick decisions in terms of their career. Job seekers will hear good news in terms of new job opportunities. 
        Ego issues between couples will be resolved now.''')
    else:
        print("Hey you sure about the number?")

    temp = input("Shall we do it again? (Y/N)")

    # when user input Y then only loop execute else it terminate.
    Val = True if temp.lower() == "y" else False
