import cv2
import matplotlib.pyplot as plt

# 이미지 로드
img1 = cv2.imread('result1.png')

# BGR -> RGB변환(OpenCV는 기본적으로 BGR 형식을 사용)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# 이미지 반전
img_flipped1 = cv2.flip(img1, 1)

img_contrast1 = cv2.convertScaleAbs(img1, alpha=2.0)

fig, ax = plt.subplots(1, 3, figsize=(15, 10))

ax[0].imshow(img1)
ax[0].axis('off')
ax[0].set_title('Origin')

ax[1].imshow(img_flipped1)
ax[1].axis('off')
ax[1].set_title('Flip')

ax[2].imshow(img_contrast1)
ax[2].axis('off')
ax[2].set_title('contrast')

plt.show()

cv2.imwrite("cv_result1.png", img_flipped1)

img2 = cv2.imread("result2.png")

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_flipped2 = cv2.flip(img2, 3)

img_contrast2 = cv2.convertScaleAbs(img2, alpha=5.0)

fig, ax = plt.subplots(1, 3, figsize=(15, 10))

ax[0].imshow(img2)
ax[0].axis('off')
ax[0].set_title('Origin')

ax[1].imshow(img_flipped2)
ax[1].axis('off')
ax[1].set_title('Flip')

ax[2].imshow(img_contrast2)
ax[2].axis('off')
ax[2].set_title('contrast')

plt.show()

cv2.imwrite("cv_result2.jpg", img_flipped2)

img3 = cv2.imread("result3.png")

img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2BGRA)

img_flipped3 = cv2.flip(img3, 2)

img_contrast3 = cv2.convertScaleAbs(img3, alpha=5.0)

fig, ax = plt.subplots(1, 3, figsize=(15, 10))

ax[0].imshow(img3)
ax[0].axis('off')
ax[0].set_title('Origin')

ax[1].imshow(img_flipped3)
ax[1].axis('off')
ax[1].set_title('Flip')

ax[2].imshow(img_contrast3)
ax[2].axis('off')
ax[2].set_title('contrast')

plt.show()

cv2.imwrite("cv_result3.png", img_flipped3)