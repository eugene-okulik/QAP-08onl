ACTIONS = '1.plus. 2.minus. 3.multiply. 4.divide.'
print(*ACTIONS.split(), sep='\n')
ACTIONS = int(input('select the number that indicates the selected action:'))
NUM_1 = int(input('please, enter the first number:'))
NUM_2 = int(input('please, enter the second number:'))


def user_actions(action, num_1, num_2):
    if action == 1:
        return num_1 + num_2
    if action == 2:
        return num_1 - num_2
    if action == 3:
        return num_1 * num_2
    if action == 4:
        if NUM_2 == 0:
            return 'not allowed'
        return num_1 / num_2
    return num_1 // num_2, num_1 % num_2


print(user_actions(ACTIONS, NUM_1, NUM_2))
