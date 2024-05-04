def sayFriday():
    print("Piatek")

def say(stuff):
    print(stuff)

def print_and_get_length(string):
    print(string)
    return len(string)

def print_and_get_length_2(string):
    print(string)
    length = 0
    for ch in string:
        length += 1
    return length

from math import pi
def cone_volume(radius, height):
    return 1/3 * pi * radius**2 * height 

def cone_volume_diam(diameter, height):
    radius = diameter / 2

    return 1/3 * pi * radius**2 * height 

def cylinder_vol_area(radius, height):
    volume = pi * radius** 2 * height
    area = 2*pi*radius * (radius + height)
    return volume, area

def count_characters(string, character):
    count = 0
    for ch in string:
        if ch == character:
            count += 1
    return count

def count__many_characters(string, characters):
    count = 0
    for ch in string:
        if ch in characters:
            count += 1
    return count

if __name__ == "__main__":
    sayFriday()
    say('hejo')
    l = print_and_get_length_2('Hejka!')
    print(f'Len: {l}')
    print(f'cone_volume: {cone_volume(1, 2)}')
    print(f'cone_volume: {cone_volume_diam(2, 2)}')
    cylinder_volume, cylinder_area = cylinder_vol_area(3, 1)
    print(f'cylinder volume: {cylinder_volume}, cylinder area: {cylinder_area}')
    print(f'Count of "a" in "alaaaaaa": {count_characters("alaaaaaa", "a")}')
    print(f'Count of "a" in "alaaaaaa": {count__many_characters("alaaaaaa", ["a", "l"])}')




       