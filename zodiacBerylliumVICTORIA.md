by = int(input("Enter your birth year: "))
if by < 1900:
    print("Invalid year")
else:
    remainder = (by - 1900) % 12
    if remainder == 0:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
    elif remainder == 1:
        print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")
    elif remainder == 2:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    elif remainder == 3:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    elif remainder == 4:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    elif remainder == 5:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    elif remainder == 6:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    elif remainder == 7:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    elif remainder == 8:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    elif remainder == 9:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    elif remainder == 10:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    elif remainder == 11:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")
