import cv2
import tensorflow as tf
import numpy as np
import pigpio


pi = pigpio.pi()
pi.set_servo_pulsewidth(14,2500)
                        

model = tf.keras.models.load_model("model.h5")
model.summary()
kamera = cv2.VideoCapture(0)


def interpoliere(zahl):
    reichweite = 2000
    schrittweite = reichweite / 10
    return schrittweite * zahl + 500
    

for _ in range(10000):
    _, frame = kamera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(frame,(25,25))
    frame = cv2.resize(frame,(28,28))
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 7);
    frame = np.max(frame) - frame
    frame = frame / np.max(frame)
    cv2.imshow("",frame)
    key =  cv2.waitKey(30)
    if key == 27:
        break

    
    batch = np.reshape(frame, (1,28,28))
    ergebnis = model(batch)
    
    
    zahl = np.argmax(ergebnis[0])
    print("\r",zahl,end="  ")
    
    pi.set_servo_pulsewidth(14,interpoliere(zahl))

kamera.release()
