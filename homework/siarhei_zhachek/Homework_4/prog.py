NUM_A = 2
# NUM_C = int(input('try again '))
while True:
    NUM_B = int(input('Enter a number from 1 to 10. '))
    if NUM_B == NUM_A:
        print('Congratulations! You guessed it!')
        break
    print('Try again')
