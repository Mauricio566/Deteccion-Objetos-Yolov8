import cv2

def collect_data():
    cap = cv2.VideoCapture(0)
    cap.set(3,1280)#resolucion de videocaptura
    cap.set(4,720)
    con = 0
    #procesara fotogramas entregados por la camara
    while True:
        ret,frame = cap.read()
        
        #lectura de teclado(para saber cuando cerrar video captura y cuando queremos almacenar un fotograma)
        t = cv2.waitKey(5)
        #tecla espacio en el codigo ascci
        if t == 32:
            #cv2.imwrite(f"datasets/images/example/img_example_{con}.jpg",frame)
            #ruta donde se almacenara cada imagen(la captura)
            cv2.imwrite(f"data/datasets/images/example/img_example_{con}.jpg",frame)
            
        
            con = con+1
        
        cv2.imshow("objects detect ",frame)
        
        if t == 27:#salimos de video captura
            break
        
    cap.release()
    cv2.destroyAllWindows()
#llamado a la funcion    
collect_data()        
        
        
    