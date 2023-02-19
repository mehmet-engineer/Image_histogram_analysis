import cv2
import numpy as np

img = cv2.imread("resim.png")
cv2.imshow("resim-orj",img)

# alpha contrast control (1.0-3.0)
# beta brightness control (0-100)

alpha = 1.5
beta = 50
img1 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow("resim1",img1)

alpha = 3
beta = 80
img2 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow("resim2",img2)

alpha = -1
beta = -20
img3 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow("resim3",img3)

alpha = 1
beta = 30
img4 = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow("resim4",img4)

cv2.waitKey()
cv2.destroyAllWindows()