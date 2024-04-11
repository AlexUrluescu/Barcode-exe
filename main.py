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

    
    def getBarcodeFromImage(self,directory, image: str):
        img = cv2.imread(f'{directory}/{image}')

        bd = cv2.barcode.BarcodeDetector()

        retval, decoded_info, decoded_type = bd.detectAndDecode(img)

        return retval
    
    
    def putNameAndBarecodeIntoTxtFile(self, imageName: str, text_file_path: str, barcode):
        try:
            with open(text_file_path, 'a') as text_file:
                text_file.write(f"{imageName} -> {barcode}\n")
            
        except Exception as e:
            print("An error occurred:", str(e))


print('INFO: The exe will search for a Input Files directory, please put your images in that directory')
input("Press the enter key to proceed")

directory = 'Input Files'
outputFilePath = 'output.txt'
utils = Utils()

filesNames = utils.getFilesFromDirectory(directory)

running = True

while running:

    print("Scanning ...")
    numberOfImages = 0

    for file in filesNames:
            if(file != ".DS_Store"):
                barcode = utils.getBarcodeFromImage(directory, file)
               
                utils.putNameAndBarecodeIntoTxtFile(file, outputFilePath, barcode)
                numberOfImages = numberOfImages + 1
    
    
    print(f'Were scanned {numberOfImages} images')
    exit = input("The barcode scan is done. Please press 0 to exit the program: ")
    print(exit)
    
    if(exit == '0'):
        running = False