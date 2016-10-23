
#from __future__ import print_function

import sys, os, shutil
import subprocess as subp


# Installation directory:
installDir = os.environ['USERPROFILE'] + r'\Documents\Paradox Interactive\Europa Universalis IV\mod'



# Make a list of the files that to install:
installList = []

installList.append(r"customPeaceTerms.mod")
installList.append(r"customPeaceTerms\localisation\replace\custompeaceterms_l_english.yml")




# Install files:
for f in installList:
    print("Installing " + f + " :: ", end="")
    source = f
    dest   = installDir + '\\' + source
    shutil.copy(source, dest)

    #if source in os.listdir(installDir):
    if os.path.isfile(dest):
        print('Install successful')
    else:
        print('Install failed')


