import numpy as np
numbers = np.random.randint(1,high=20,size=15,dtype='int');
print("random array generated is:",numbers)
num = np.reshape(numbers,(3,5));
print("reshaped array:",num)
print('Replacing Max No. by 0',np.where(num == np.max(num, axis=1).reshape(-1,1), 0, num))
