# functions


def find_weather(temparature):
    if temparature > 40:
        print("too hot")
    elif temparature > 30:
        print("normal temp")
    else:
        print("nice weather")


def is_even_num(temp):
    return temp % 2 == 0


find_weather(40)
is_even_num(40)
