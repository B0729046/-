import cv2



def img_sensor():

    img = cv2.imread("before.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21,21), 0)

    faceCascade = cv2.CascadeClassifier("face_detect.xml")
    faceRect = faceCascade.detectMultiScale(gray, 1.2, 2)                  #(data, 縮小倍數, 被框幾次才被偵測到)

    for(x, y, w, h) in faceRect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 5)


    cv2.imshow("img", img)
    cv2.waitKey(0)



if __name__ == '__main__':
    img_sensor()


