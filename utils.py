from typing import List
import os
import cv2

class Utils():

    def getFilesFromDirectory(self, directoryPath: str) -> List[str]:
        file_names: List[str] = []
        for filename in os.listdir(directoryPath):
            if os.path.isfile(os.path.join(directoryPath, filename)):
                file_names.append(filename)

        return file_names

    
    def getBarcodeFromImage(self,directory: str, image: str):
        img = cv2.imread(f'{directory}/{image}')

        bd = cv2.barcode.BarcodeDetector()

        retval, decoded_info, decoded_type = bd.detectAndDecode(img)

        return retval
    
    
    def putNameAndBarcodeIntoTxtFile(self, imageName: str, text_file_path: str, barcode: str):
        try:
            with open(text_file_path, 'a') as text_file:
                text_file.write(f"{imageName} -> {barcode}\n")
            
        except Exception as e:
            print("Error:", str(e))
