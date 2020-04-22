from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
path = "./data/1_No_Finding"
test = Image.open(path+"/NoF_1.jpg")
test.show()
test_array = np.asarray_chkfinite(test)
plt.imshow(test_array)
#print(test_array)
print(test_array.shape)