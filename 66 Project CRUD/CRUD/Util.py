import random
import string

def random_string(panjang:int) -> str:
    str_rand = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return str_rand