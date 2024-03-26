from typing import List
import os
import cv2

class Utils():

    def getFilesFromDirectory(self, directoryPath: str) -> List[str]:
        file_names: List[str] = []
        for filename in os.listdir(directoryPath):
            if os.path.isfile(os.path.join(directoryPath, filename)):
                file_names.append(filename)

        print(file_names)
        return file_names

    
    def getBarcodeFromImage(self, image: str):
        img = cv2.imread(f'Input Files/{image}')

        bd = cv2.barcode.BarcodeDetector()

        retval, decoded_info, points = bd.detectAndDecode(img)

        print(f"barcode: {retval} -> digits: {len(retval)}")
        return retval
    
    
    def putNameAndBarecodeIntoTxtFile(self, imageName: str, text_file_path: str, barcode):
        try:
            with open(text_file_path, 'a') as text_file:
                text_file.write(f"{imageName} -> {barcode}\n")
            
        except Exception as e:
            print("An error occurred:", str(e))

