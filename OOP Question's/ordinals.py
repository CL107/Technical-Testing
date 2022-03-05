class letter():
    def __init__(self, User = 'yes'):

        if User == 'no':
                 quit()
        while User == 'yes':
                letter = input('Please enter a letter: ')
                num = ord(letter)
                print('The ordinal for the letter', letter, 'is: ', num)
                letter=chr(num)
                print(f"The letter for the ordinal {num} is: {letter}")
            
                User = input("Another letter? ")
letter()
