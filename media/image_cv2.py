import cv2
import glob
import numpy as np


class Image(object):
    def __init__(self, name=None, percent=None, image=None):
        self.name = name
        self.percent = percent
        self.image = image


def compares(img):
    myList = glob.glob("./media/*.jpg")
    img_percent = []
    if myList:
        print("there is image - " + str(len(myList)))
        print()
        y = 0
        counter = 0

        for i in myList:
            counter = counter + 1
            u = i.split('\\')

            u1 = u[0] + '/' + u[1]
            print(str(u1))

            u2 = u1.split('.')
            print(str(u2[2]))

            i = u[1]
            print("/media/" + str(i))
            n = cv2.imread("./media/" + str(i),2)
            m = cv2.imread(img, 2)

            # cv2.imshow('image', m)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            w1 = cv2.resize(m, (100, 100))
            w2 = cv2.resize(n, (100, 100))

            d = cv2.subtract(w1, w2)

            r = np.any(d)

            s = np.percentile(d, 50)

            print(str(s)+" ojasbhfliuhjsnbadfigujnsafikjnsaifkjsaa")

            # img_percent.append(Image("Trademark No : " + str(counter), s, i))
            # print(s)

            # if r != True:
            #     y = y + 1
            #     print("same image - " + str(counter))
            #     s = (str(100 - (s / 255) * 100) + " %")
            #
            # else:
            #     print("different image - " + str(counter))
            #
            #     if s <= 10:
            #         s = (str(100 - (s / 255) * 100) + " %")
            #     elif s <= 50:
            #         s = (str(100 - (s / 255) * 100) + " %")
            #     elif s <= 100:
            #         s = (str(100 - (s / 255) * 100) + " %")
            #     elif s <= 200:
            #         s = (str(100 - (s / 255) * 100) + " %")
            #     elif s <= 250:
            #         s = (str(100 - (s / 255) * 100) + " %")
            #     elif s > 250:

            #         s = (str(100 - (s / 255) * 100) + " %")
            s = (str(100 - (s / 255) * 100) + " %")

            print(str(s))

            img_percent.append(Image("Trademark No : " + str(counter), s, i))

        print("the similarity is " + str(y))
        # cv2.imshow('image', m)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print("there is no image")

    return img_percent

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
