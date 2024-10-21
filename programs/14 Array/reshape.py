import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
new_arr = arr.reshape(3,4)  # 3 indicates rows & 4 inicates columns...
                            # O/P :[[ 1  2  3  4]
                            #       [ 5  6  7  8]
                            #       [ 9 10 11 12]]
print(new_arr)

