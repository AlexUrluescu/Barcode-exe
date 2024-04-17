from utils import Utils

print('INFO: The exe will search for an Input Files directory, please put your images in that directory')
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
               
                utils.putNameAndBarcodeIntoTxtFile(file, outputFilePath, barcode)
                numberOfImages = numberOfImages + 1
    
    
    print(f'Were scanned {numberOfImages} images')
    exit = input("The barcode scan is done. Please press 0 to exit the program: ")
    
    if(exit == '0'):
        running = False