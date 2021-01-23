
# generate all possible passwords between 4 and 6 characters long
# save it to a file 'file_path'
#
# generate a random password and find it in the above file

char_l = ord('a')  # a
char_h = ord('z')  # z
file_path = 'passwords'

import time
import random

def generate_pass():
    starting_time = time.time()

    f = open(file_path, 'w')
    for char1 in range(char_l, char_h+1):
        print(f'generating.. {int((char1-char_l)*100/(char_h-char_l))}%')
        for char2 in range(char_l, char_h+1):
            for char3 in range(char_l, char_h+1):
                for char4 in range(char_l, char_h+1):
                    f.write(chr(char1) + chr(char2) + chr(char3) + chr(char4) + '\n')
                    for char5 in range(char_l, char_h+1):
                        f.write(chr(char1) + chr(char2) + chr(char3) + chr(char4) + chr(char5) + '\n')
                        for char6 in range(char_l, char_h+1):
                            f.write(chr(char1) + chr(char2) + chr(char3) + chr(char4) + chr(char5) + chr(char6) + '\n')

    ending_time = time.time()
    f.close()
    print(f'password generation time: {ending_time - starting_time}s')

def find_pass():
    starting_time = time.time()
    password = ''

    for i in range(random.randint(4,6)):
        password += (chr(random.randint(char_l,char_h)))

    f = open(file_path, 'r')

    while True:
        line = f.readline()
        if line == '':
            print(f'password ({password}), was not found in the file :(')
            break
        if (password + '\n') == line:
            ending_time = time.time()
            print(f'found password({password}) at character #{f.tell()}, it took: {ending_time - starting_time}s')
            break
    f.close()

def main():
    print('choose your option:')
    print('1 - to generate passwords file')
    print('2 - to generate a random password and find it in the file')
    m_input = int(input())
    if m_input == 1:
        generate_pass()
    if m_input == 2:
        find_pass()

main()
