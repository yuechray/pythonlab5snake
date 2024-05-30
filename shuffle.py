import random
from typing import List

def shuffle_list(input_list: List[int]) -> List[int]:
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list

# Пример использования:
example_list = [1, 2, 3, 4, 5]
shuffled_example = shuffle_list(example_list)
print(shuffled_example)
