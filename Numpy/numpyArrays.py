import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)
# result = np.arange(10,100,5)
# result = np.zeros(10)
# result = np.linspace(0,100,6)
# result = np.random.randint(1,7,3)
# result = np.random.rand(3)
# result = np.random.randn(3)
# np_array = np.arange(50)
# np_multi = np_array.reshape(10,5)

# print(np_multi.sum(axis=1)) #satırların toplamı
# print(np_multi.sum(axis=0)) #sütunların toplamı

rnd_number = np.random.randint(1,100,10)
print(rnd_number)
result = rnd_number.max()
result = rnd_number.min()
result = rnd_number.mean() #average
result = rnd_number.argmax()
result = rnd_number.argmin()
print(result)