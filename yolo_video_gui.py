import cv2 #zehraharmanda2b
import numpy as np
import os
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

from pygame import mixer # pip install pygame #♦yeni eklendi
import pygame #yeni eklendi
def process():
    
   pygame.mixer.init(44100, -16, 2, 2048) # veya 48000, -16, 1, 1024 #yeni
   pygame.init()
   file = "car.mp3" #yeni
   file1="person.mp3"
   file2="bus.mp3"
   mixer.init()#yeni

   #img = cv2.imread("000072.png")


   cap = cv2.VideoCapture("test1.mp4")

   while True:
        ret, frame = cap.read()
        
        frame = cv2.flip(frame,1)
        frame = cv2.resize(frame,(960,720))
        
        frame_width = frame.shape[1]
        frame_height = frame.shape[0]
    
        frame_blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    
        labels = ["aeroplane", "bicycle" ,"bird" ,"boat", "bottle", 
                  "bus" ,"car" ,"cat" ,"chair" ,"cow", 
                  "diningtable", "dog" ,"horse" ,"motorbike" ,
                  "person" ,"pottedplant" ,"sheep" ,"sofa" ,
                  "train" ,"tvmonitor"]
    
        colors = ["0,0,255","0,0,255","255,0,0","255,255,0","0,255,0"]
        colors = [np.array(color.split(",")).astype("int") for color in colors]
        colors = np.array(colors)
        colors = np.tile(colors,(18,1))
    
    
        model = cv2.dnn.readNetFromDarknet("pascal_yolov4.cfg","pascal_yolov4_last.weights")
    
        layers = model.getLayerNames()
        output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]
        
        model.setInput(frame_blob)
        
    
        
        detection_layers = model.forward(output_layer)
    
    
        ############## NON-MAXIMUM SUPPRESSION - OPERATION 1 ###################
        
        ids_list = []
        boxes_list = []
        confidences_list = []
        
        ############################ END OF OPERATION 1 ########################
        
        for detection_layer in detection_layers:
            for object_detection in detection_layer:
                
                scores = object_detection[5:]
                predicted_id = np.argmax(scores)
                confidence = scores[predicted_id]
                
                if confidence > 0.20:
                    
                    label = labels[predicted_id]
                    bounding_box = object_detection[0:4] * np.array([frame_width,frame_height,frame_width,frame_height])
                    (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
                    
                    start_x = int(box_center_x - (box_width/2))
                    start_y = int(box_center_y - (box_height/2))
                    
                    
                    ############## NON-MAXIMUM SUPPRESSION - OPERATION 2 ###################
                    
                    ids_list.append(predicted_id)
                    confidences_list.append(float(confidence))
                    boxes_list.append([start_x, start_y, int(box_width), int(box_height)])
                    
                    ############################ END OF OPERATION 2 ########################
                    
                    
                    
        ############## NON-MAXIMUM SUPPRESSION - OPERATION 3 ###################
                    
        max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)
             
        for max_id in max_ids:
            
            max_class_id = max_id[0]
            box = boxes_list[max_class_id]
            
            start_x = box[0] 
            start_y = box[1] 
            box_width = box[2] 
            box_height = box[3] 
             
            predicted_id = ids_list[max_class_id]
            label = labels[predicted_id]
            confidence = confidences_list[max_class_id]
          
        ############################ END OF OPERATION 3 ########################
                    
            end_x = start_x + box_width
            end_y = start_y + box_height
                    
            box_color = colors[predicted_id]
            box_color = [int(each) for each in box_color]
                    
                    
            label_format = "{}: {:.2f}%".format(label, confidence * 100)
            print("predicted object {}".format(label_format))    
            if (label=="car"):
             mixer.music.load(file)
             mixer.music.play()
             clock = pygame.time.Clock()
             while pygame.mixer.music.get_busy():
              clock.tick(10)
              pygame.event.poll()
   ####################################3
            if (label=="bus"):
             mixer.music.load(file2)
             mixer.music.play()
             clock = pygame.time.Clock()
             while pygame.mixer.music.get_busy():
              clock.tick(10)
              pygame.event.poll()
      ################   ################################
            if (label=="person"):
             mixer.music.load(file1)
             mixer.music.play()
             clock = pygame.time.Clock()
             while pygame.mixer.music.get_busy():
              clock.tick(10)
              pygame.event.poll()
                    
            cv2.rectangle(frame, (start_x,start_y),(end_x,end_y),box_color,2)
            cv2.rectangle(frame, (start_x-1,start_y),(end_x+1,start_y-30),box_color,-1)
            cv2.putText(frame,label_format,(start_x,start_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
        cv2.imshow("Detector",frame)
        
   cap.release()
   cv2.destroyAllWindows()        
   
        
def start_process():
     process()
  
    
window = tk.Tk()
window.title("DEMO")
#window.geometry('400x200')
window.geometry('500x200')
lbl = tk.Label(window, text=" Object Detection ", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)
lmain = tk.Label(window, text=" Are you ready 3d object detection? Please press start button ", fg = "dark blue",
		 bg = "dark gray",
		 font = "Helvetica 10 bold ")
lmain.grid(row=1, column=0)
startVideoStreamBtn = tk.Button(window, text="Start", command=process)
startVideoStreamBtn.grid(column=0, row=2, padx=15)
window.mainloop()
#%%

    
    
    
    