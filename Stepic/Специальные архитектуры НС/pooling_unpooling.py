# pooling

import numpy as np
import skimage.measure
a = np.array([[2, 1, 3, 4], [5, 4, 4, 6], [1, 3, 7, 5], [1, 2, 6, 6]])
a_unp = skimage.measure.block_reduce(a, (2,2), np.max)
print(a_unp)




