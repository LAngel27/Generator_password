import random

def generator_password():

    upper_list = ['A','B','C','D','E','F','G','H','I']
    lower_list = ['a','b','c','d','e','f','g','h','i']
    symbol_list = ['!','?','$','Ç','¡','&','y','h','i']
    numbers_list = ['1','2','3','4','5','6','7','8','9']

    character_list = upper_list + lower_list + symbol_list + numbers_list

    password = []

    for i in range(15):
        character_random = random.choice(character_list)
        password.append(character_random)

    password = ''.join(password)

    return password


def run():
    password = generator_password()
    print('You new password is: ' + password )




if __name__ == '__main__':
    run()