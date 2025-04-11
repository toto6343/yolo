from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# 비디오 파일 로드 및 특정 구간 잘라내기
clip = (
    VideoFileClip(r"WTDC\data\traffic.mp4").subclipped(5, 10)
)

# 비디오 편집
final_video = CompositeVideoClip([clip])

# 결과 비디오 저장
final_video.write_videofile("final_video.mp4")

final_video.write_images_sequence("frame_%03d.png")


final_video.write_gif("final_video.gif")


#---------------------------------------------------------------------------------------------------------------

# 자막 만들기: TextClip을 사용하여 자막 텍스트 생성
subtitle = TextClip("고속도로 교통 현황", fontsize=24, color='white', font='Arial')

# 자막 위치 지정: (x, y) 좌표
subtitle = subtitle.set_position(('center', 'bottom')).set_duration(clip.duration)

# 비디오와 자막을 합치기
final_video = CompositeVideoClip([clip, subtitle])

# 결과 비디오 저장
final_video.write_videofile("final_video2.mp4", codec='libx264', fps=24)
