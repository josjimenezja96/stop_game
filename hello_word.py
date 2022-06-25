import random
def _randomMult(a):
  b =  random.randint(5, 15)
  multi = a * b
  return multi


def _resta(x,y):
	return x-y


def _sumArray(arr):
    sum=0
    for i in arr:
        sum= sum + i
    return sum

print(_sumArray([1, 1]))

def division(numerador, divisor):
    if (divisor != 0):
        return numerador/divisor
    else :
        return 0
        