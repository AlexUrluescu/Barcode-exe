import cv2

print(cv2.__version__)

img = cv2.imread('Input Files/img3.jpeg')

bd = cv2.barcode.BarcodeDetector()

retval, decoded_info, points = bd.detectAndDecode(img)

print(retval)