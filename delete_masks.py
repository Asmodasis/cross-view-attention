import os
import shutil #shutil.move
import random

directoryNormal = 'MINI-DDSM-Complete-JPEG-8/Normal'
directoryBenign = 'MINI-DDSM-Complete-JPEG-8/Benign'
directoryCancer = 'MINI-DDSM-Complete-JPEG-8/Cancer'


def deleteFunc(norm,dir):
    # THIS WILL DELETE THE FILES IN THE ORIGINAL LOCATION
    # SAVE BACKUPS
    os.chdir(dir+'/'+norm)
    print("Sub Directory: ",os.getcwd())
    for dirName in os.listdir(os.getcwd()): 
        for fileName in os.listdir(dirName):
            print("Filename ben == ", fileName)
            print(os.getcwd())
            if '.OVERLAY' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif '.COMB' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif 'MLO' not in dirName+'/'+fileName and 'CC' not in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif 'Mask' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif 'Mask2' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif 'MASK2' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)
            elif 'MASK' in dirName+'/'+fileName:
                os.remove(dirName+'/'+fileName)

    
if __name__ == "__main__":
    dir = os.getcwd()
    listOfDir = [   directoryNormal,directoryBenign,directoryCancer
                ]
    for item in listOfDir:
        print("Primary Directory: ",dir)
        deleteFunc(item,dir)
    