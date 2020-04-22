import cv2
import numpy as np
import random as rd

body_model = cv2.CascadeClassifier('haarcascade_fullbody.xml')
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("peopleCounter.avi")

while True:
	
	status, photo = cap.read()
	if status == False:
		break
		
	body_cor = body_model.detectMultiScale(photo)
	face_cor = face_model.detectMultiScale(photo)
	
	for i in range(len(face_cor)):
		if i < len(face_cor) - 1:
			if abs(face_cor[i+1][0] - face_cor[i][0]) < 200 and abs(face_cor[i+1][1] - face_cor[i][1] < 50):
				f = open("data","w")
				f.write("1")
				f.close()
				rect_color = [0,0,255]
			else:
				f = open("data","w")
				f.write("0")
				f.close()
				rect_color = [0,255,0]
			
		photo = cv2.rectangle(photo , (face_cor[i][0],  face_cor[i][1]) , (face_cor[i][2] + face_cor[i][0], face_cor[i][3] + face_cor[i][1]), rect_color, 3)
		
	for i in range(len(body_cor)):
		if i < len(body_cor) - 1:
			if abs(body_cor[i+1][0] - body_cor[i][0]) < 200 and abs(body_cor[i+1][1] - body_cor[i][1] < 50):
				f = open("data","w")
				f.write("1")
				f.close()
				rect_color = [0,0,255]
			else:
				f = open("data","w")
				f.write("0")
				f.close()
				rect_color = [0,255,0]
			
		photo = cv2.rectangle(photo , (body_cor[i][0],  body_cor[i][1]) , (body_cor[i][2] + body_cor[i][0], body_cor[i][3] + body_cor[i][1]), rect_color, 3)
	
	cv2.imshow('hi' , photo)
	if cv2.waitKey(100) == 13:
		break
	
cv2.destroyAllWindows()