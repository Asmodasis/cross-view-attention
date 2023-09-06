import os
import shutil #shutil.move
import random

directoryNormal = 'MINI-DDSM-Complete-JPEG-8/Normal'
directoryBenign = 'MINI-DDSM-Complete-JPEG-8/Benign'
directoryCancer = 'MINI-DDSM-Complete-JPEG-8/Cancer'

targetNormal = 'MINI-DDSM-Complete-JPEG-8-test/Normal'
targetBenign = 'MINI-DDSM-Complete-JPEG-8-test/Benign'
targetCancer = 'MINI-DDSM-Complete-JPEG-8-test/Cancer' 

random.seed()                       # system time

# THIS WILL DELETE THE FILES IN THE ORIGINAL LOCATION
for filename in os.listdir(directoryNormal):
    if random.randrange(0,100) > 90:
        # 10% split on testing
        shutil.move(directoryNormal+'/'+filename,targetNormal+'/'+filename, copy_function = shutil.copytree)                        
                                    # copy directory
        
        print(filename)
    else:
        continue                    # don't copy directory 
for filename in os.listdir(directoryBenign):
    if random.randrange(0,100) > 90:
        # 10% split on testing
        shutil.move(directoryBenign+'/'+filename,targetBenign+'/'+filename, copy_function = shutil.copytree)                        
                                    # copy directory
        
        print(filename)
    else:
        continue                    # don't copy directory 

for filename in os.listdir(directoryCancer):
    if random.randrange(0,100) > 90:
        # 10% split on testing
        shutil.move(directoryCancer+'/'+filename,targetCancer+'/'+filename, copy_function = shutil.copytree)                        
                                    # copy directory
        
        print(filename)
    else:
        continue                    # don't copy directory 