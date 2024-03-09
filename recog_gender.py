import face_recognition
from deepface import DeepFace
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
import pyscreenshot as ImageGrab

model = ""

def preprocess_img(img, target_size=(224,224)):
    img = cv2.resize(img, target_size)
    img_pixels = image.img_to_array(img)
    img_pixels = np.expand_dims(img_pixels, axis = 0)
    img_pixels /= 255 #normalize input in [0, 1]
    return img_pixels


def grab_screenshot():
    im = ImageGrab.grab()
    return im

def recog_gender(img_file=None, image=None):
    global model 
    if model == "": # only need to build the model for the first time
        model = DeepFace.build_model("Gender")
    if img_file:
        image = face_recognition.load_image_file(img_file)
    face_locations = face_recognition.face_locations(image)
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))
    count_man = 0
    count_woman = 0
    for face_location in face_locations:
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        face_image = preprocess_img(img=face_image)
        gender_predictions = model.predict(face_image)[0,:]
        if np.argmax(gender_predictions) == 0:
            count_woman += 1
        elif np.argmax(gender_predictions) == 1:
            count_man += 1
    return count_man, count_woman

if __name__ == '__main__':
    count_man, count_woman = recog_gender(img_file="sample_zoom_screenshot.png")
    print("man:", count_man, "woman:", count_woman )