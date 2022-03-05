import msvcrt

while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        print(key_stroke)
        print(key_stroke[0])
    #if key_stroke == "b\'\x1b"
