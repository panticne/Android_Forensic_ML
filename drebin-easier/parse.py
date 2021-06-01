__author__ = 'Christian Urcuqui'
# This class generates all information for ML
import Permissions_Android
import xml.etree.ElementTree as ET
import os
from os.path import isfile, join
from multiprocessing import Pool, cpu_count
import csv
import numpy as np


def eraser(package):
    os.system("find " + "Output" + package + " -type f ! -name 'AndroidManifest.xml' -delete")


def permissionParsing(package,writer,MORN):

    array_output = []
    try:
        print(package + "/AndroidManifest.xml")
        tree = ET.parse(package + "/AndroidManifest.xml")
        treeRoot = tree.getroot()
        array_permissions = []

        for permission in treeRoot.findall('uses-permission'):
            per = permission.get('{http://schemas.android.com/apk/res/android}name')
            array_permissions.append(per)

        for item in sorted(Permissions_Android.AOSP_PERMISSIONS):

            if array_permissions.__contains__(item):

                array_output.append("1")
            else:

                array_output.append("0")
        array_output.append(MORN)
        writer.writerow(array_output)
        print("wrote...")
    except:
        print("error")

def separate(filename, dataDir,dataDirDest, MORN):
    fileList = os.listdir(dataDir)
    link = []
    i = 0
    csvFile = filename
    fl = open(csvFile, 'w')
    writer = csv.writer(fl)
    array_data = []
    for criter in sorted(Permissions_Android.AOSP_PERMISSIONS):
        array_data.append(criter)
    array_data.append("malware")
    writer.writerow(array_data)


    for e in fileList:
        link.append(join(dataDir, e))

    for filename in fileList:
        os.system("apktool" + " " + "d -f " + link[i] + " -o " + dataDirDest + "Output" + filename)
        i += 1
        eraser(filename)
        permissionParsing(dataDirDest + "Output" + filename, writer, MORN)

def parse(malDir,malDirDest, goodDir, goodDirDest):
    goodCsvFile = "binaryApps_BEN.csv"
    malwareCsvFile = "binaryApps_MAL.csv"


    pool = Pool(processes=2)

    pool.apply_async(separate, args=(goodCsvFile, goodDir, goodDirDest, "-1"))
    pool.apply_async(separate, args=(malwareCsvFile, malDir, malDirDest, "1"))

    # Step 4: Close Pool and let all the processes complete
    pool.close()
    pool.join()


