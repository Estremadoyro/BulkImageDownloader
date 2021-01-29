import urllib.request
import os

notSavedFiles = []

def readTxt(file):
    text_file = open(file, "r")
    lines = text_file.readlines()
    print(len(lines))
    text_file.close()
    return lines

def downloadImages(teachers, imageFolderPath):
    count = 1
    for x in teachers:
        fileName = str(count) + ".png"
        count = count + 1
        try:
            imageLocation = os.path.join(imageFolderPath, fileName)
            urllib.request.urlretrieve(x, imageLocation)
            print("Saved: {}".format(fileName))
        except urllib.request.HTTPError as error:
            if error.code == 404:
                print("NotFound (404): {}".format(fileName))
                notSavedFiles.append(x)

def createImageFolder():
    currentPath = os.getcwd()
    imageFolderPath = currentPath + "\TeacherImages"
    if (not(os.path.isdir(imageFolderPath))):
        os.mkdir(imageFolderPath)
        print("FolderCreated")
    else :
        print("Image folder already exists..")
    return imageFolderPath

def saveTxtErrors(notSavedFiles):
    stringFiles = "".join(notSavedFiles)
    file_1 = open("404 - NotFound.txt", "w")
    file_1.write(stringFiles)
    file_1.close()
    print("Errors (404) txt created")

def main(file):
    imageFolderPath = createImageFolder()
    lines = readTxt(file)
    downloadImages(lines, imageFolderPath)
    saveTxtErrors(notSavedFiles)
    print("---- Finished ----")
    return

main("teacherImages.txt")
    
    
