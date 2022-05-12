import pandas as pd
import numpy as np

#data
numbers = [40,45,50,55]
letters = ['yakup','mehmet','buse','melike']
different = ['yakup','mehmet','buse','melike',1,2,3,4]
scalar = 5
dict = {'a':999,'b':2345,'c':56789,'d':123}
random_numbers = np.random.randint(10,100,6)

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(different)
# pandas_series = pd.Series(5, [0,1,2,3])
# pandas_series = pd.Series(numbers, ['a','b','c','d'])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series['a']
# result = pandas_series['d']
# result = pandas_series[['a','c']]
# result = pandas_series.ndim
# result = pandas_series.dtype
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series + pandas_series
# result = pandas_series * pandas_series
# result = pandas_series * 100
# result = np.sqrt(pandas_series)
# result = pandas_series >= 50
# result = pandas_series % 2 == 0

# print(pandas_series[pandas_series % 2 == 1])
# print(pandas_series)
# print(result)




opel2018 = pd.Series([20,30,40,10],["ASTRA","CORSA","MOKKA","INSIGNIA"])
opel2019 = pd.Series([40,30,20,10],["ASTRA","CORSA","GRANDLAND","INSIGNIA"])

total = opel2018 + opel2019

print(total["ASTRA"])
print(total)