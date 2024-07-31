from unittest import result
import annotated_types
import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
#resolucion de nuestra video captura
cap.set(3,1280)
cap.set(4,720)

model = YOLO("models/best2.pt")
#annotated_frames = None  # Inicializar annotated_frames fuera del bucle
while True:
    ret,frame = cap.read()
    
    results = model.predict(frame,imgsz = 640,conf = 0.4)
    #print("resultados ",results)
    #print("resultado pocision 0 lista ",results[0])
    
    #if len(results) != 0:
    #for res in results:
     #   print("objeto detectado")
            
    #else:
        #print("nada detectado")        
            
        #annotated_frames = results[0].plot()
        
        
    
    #cv2.imshow("objects detects",annotated_frames)
    #cv2.imshow("objects detects",results[0].plot())
    cv2.imshow("objects detects",results[0].plot())
    
    
    t = cv2.waitKey(5)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()    
                 