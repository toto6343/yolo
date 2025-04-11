import albumentations as A  
import cv2
import matplotlib.pyplot as plt

# 이미지 로드
img = cv2.imread("frame_000.png")

# BGR2RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Albumentations 설정
transform = A.Compose([
    A.Rotate(limit=20, p=1.0),  # 회전
    A.RandomBrightnessContrast(p=1.0),  # 밝기/대비 조정
    A.HorizontalFlip(p=0.5),  # 수평 뒤집기
    A.GaussianBlur(blur_limit=3, p=0.5),  # 가우시안 블러
    A.ElasticTransform(p=0.5),  # 탄성 변형
])

augmented = transform(image=img)
img_augmented = augmented['image']

# 원본 이미지와 증강된 이미지 비교
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 원본 이미지
axs[0].imshow(img)
axs[0].axis('off')
axs[0].set_title("Original Image")

# 증강된 이미지
axs[1].imshow(img_augmented)
axs[1].axis('off')
axs[1].set_title("Augmented Image")

plt.show()
