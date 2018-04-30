import numpy as np


arr = np.arange(0,11)
print('array in range 0 and 11' , arr )

zero = np.zeros(10)
print('array of 10 zeros ' , zero)

fives = np.ones(10) * 5
print(fives)

range_ = np.arange(10,51)
print(range_)

array = np.arange(9)
print(array)

Shape = array.reshape(3,3)
print('reshaped array' , Shape)

ra = np.random.rand(1)
print('random number between 0 and 1' , ra)

mat = np.arange(1,26).reshape(5,5)
print('matrix of 5,5' , mat)

val = mat[3,4]
print('value at position 3,4 is' , val)

sum_ = np.sum(mat)
print('sum of mat is ' , sum_)

space = np.linspace(0,10,5)
print(space)

data = np.eye(3)
print(data)

random_integer = np.random.randint(1,50)
print('random integer in between 1 and 50',  random_integer)

ranarr = np.random.randint(0,50,10)
print(ranarr)

print('maximum in ranarr' , ranarr.max())
print('minimum in ranarr' , ranarr.min())

print(ranarr.shape)

print(ranarr.dtype)

num = np.arange(0,10)
print(num)

bool_ = num > 3
print(bool_)

print(num + num )

print(num ** 2)