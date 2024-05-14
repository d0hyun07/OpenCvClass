import cv2

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 배경 영상 저장 플래그
save_bg = False
bg_img = None

while True:
    # 웹캠 프레임 읽기
    ret, frame = cap.read()

    # 키보드 입력 확인
    key = cv2.waitKey(1) & 0xFF

    # 프레임을 흑백으로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 'a' 키가 눌리면 배경 영상 저장
    if key == ord('a'):
        save_bg = True
        bg_img = gray_frame.copy()
        print("Background image saved.")

    # 배경 영상이 저장되었다면 차영상 계산
    if save_bg:
        diff = cv2.absdiff(gray_frame, bg_img)

        # 'b' 키가 눌리면 차영상 이진화
        if key == ord('b'):
            _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            cv2.imshow("Thresholded", thresh)
        else:
            cv2.imshow("Difference", diff)
    else:
        cv2.imshow("Webcam", gray_frame)

    # 'q' 키가 눌리면 종료
    if key == ord('q'):
        break

# 웹캠 및 창 닫기
cap.release()
cv2.destroyAllWindows()
