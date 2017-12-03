import cv2
import glob
import numpy as np

ima2 = cv2.imread('image.jpg', 0)

# myList = glob.glob("./*.jpg")
# ima = cv2.imread(myList[0], 0)
myList = [ima2, 1, 2, 32, 3, 4]

print(len(myList))

# w1 = cv2.resize(ima, (100, 100))
# w2 = cv2.resize(ima2, (100, 100))

# cv2.imshow('image', ima)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# d = cv2.subtract(w1, w2)

# r = np.any(d)

# print(myList.index(1))

# if r == True:
#     print("different image")
# else:
#     print("same image")
