import numpy
import cv2

# Abrir la camara
capture = cv2.VideoCapture(0)

# Mientras la camara este abierta 
while(capture.isOpened()):
 ret, frame = capture.read()

# Si se presiona X, salir
 if (cv2.waitKey(1) == ord("x")):
   break
 
#  Decodificar el codigo QR
 qrDetector = cv2.QRCodeDetector()
 Data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

# Si hay datos, entonces mostrarlos en la consola
 if len(Data) > 0:
   print(f"Dato: {Data}")
   cv2.imshow("webCam", rectifiedImage)
 else:
   cv2.imshow("webCam", frame)
   
# Llamar la camara y cerrarla
capture.release()




