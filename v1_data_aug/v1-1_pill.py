from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 첫 번째 이미지 로드
img1 = Image.open("WTDC/data/[BLUE]00028A_130409_007.jpg")

# 첫 번째 이미지 회전
img_rotated1 = img1.rotate(90)

# 첫 번째 이미지 밝기 조정
enhancer1 = ImageEnhance.Brightness(img1)
img_brightened1 = enhancer1.enhance(2.0)

# 두 번째 이미지 로드
img2 = Image.open("WTDC/data/[BLUE]00031A_130124_003.jpg")

# 두 번째 이미지 회전
img_rotated2 = img2.rotate(90)

# 두 번째 이미지 밝기 조정
enhancer2 = ImageEnhance.Brightness(img2)
img_brightened2 = enhancer2.enhance(2.0)

# 세 번째 이미지 로드
img3 = Image.open("WTDC/data/[BLUE]00067A_155529_006.jpg")

# 세 번째 이미지 회전
img_rotated3 = img3.rotate(90)

# 세 번째 이미지 밝기 조정
enhancer3 = ImageEnhance.Brightness(img3)
img_brightened3 = enhancer3.enhance(2.0)

# 6개의 이미지 시각화
fig, ax = plt.subplots(2, 3, figsize=(18, 12)) 

# 첫 번째 이미지 및 결과
ax[0, 0].imshow(img1)  
ax[0, 0].axis('off')
ax[0, 0].set_title("ORG_IMAGE 1")

ax[0, 1].imshow(img_rotated1)  
ax[0, 1].axis('off')
ax[0, 1].set_title("ROTATED_IMAGE 1")

ax[0, 2].imshow(img_brightened1)  
ax[0, 2].axis('off')
ax[0, 2].set_title("BRIGHTENED_IMAGE 1")

# 두 번째 이미지 및 결과
ax[1, 0].imshow(img2)
ax[1, 0].axis('off')
ax[1, 0].set_title("ORG_IMAGE 2")

ax[1, 1].imshow(img_rotated2)  
ax[1, 1].axis('off')
ax[1, 1].set_title("ROTATED_IMAGE 2")

ax[1, 2].imshow(img_brightened2)  
ax[1, 2].axis('off')
ax[1, 2].set_title("BRIGHTENED_IMAGE 2")

# 세 번째 이미지 및 결과
fig, ax2 = plt.subplots(1, 3, figsize=(18, 6))

# 세 번째 이미지 및 결과
ax2[0].imshow(img3)
ax2[0].axis('off')
ax2[0].set_title("ORG_IMAGE 3")

ax2[1].imshow(img_rotated3)
ax2[1].axis('off')
ax2[1].set_title("ROTATED_IMAGE 3")

ax2[2].imshow(img_brightened3)
ax2[2].axis('off')
ax2[2].set_title("BRIGHTENED_IMAGE 3")


img_brightened1.save("./result1.png")
img_brightened2.save("./result2.png")
img_brightened3.save("./result3.png")
img_rotated1.save("./result11.png")
img_rotated2.save("./result22.png")
img_rotated3.save("./result33.png")

# 결과 출력
plt.show()

# a = img1.transpose(Image.Transpose.TRANSVERSE)
# a.save("./result10")