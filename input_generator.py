import random
import numpy as np
from solver import Solver


def random_letter_generator(values):
    letters = [1, 2, 3]
    return random.int


low_constrain = 2**8
high_constrain = 2**16



for file_number in range(80):
    random_number = random.randint(0, 1)
    limit = random.randint(low_constrain, 2**20 - 1)


    input_file = open(f'input/input{file_number}.txt', 'w+')
    input_file.write(f"{limit}\n")

    for _ in range(int(limit/2)):
        i = random.randint(-32768, 32767)

        opcode = random.randint(1, 3)

        input_file.write(f'{opcode}\n{i}\n')
    input_file.write(f'0')

        
