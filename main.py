from utils import Utils

directory = 'Input Files'
outputFilePath = 'output.txt'
utils = Utils()

filesNames = utils.getFilesFromDirectory(directory)

running = True

while running:

    for file in filesNames:
            if(file != ".DS_Store"):
                barcode = utils.getBarcodeFromImage(directory, file)
               
                utils.putNameAndBarcodeIntoTxtFile(file, outputFilePath, barcode)
    
    running = False