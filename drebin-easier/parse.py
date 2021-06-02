"""
    This file is used to :
    1) Call apktool to extract apk inside the right folder;
    2) Clear the apktool output directory and only let AndroidManifest.xml;
    3) Parse it with XML DOM and compare the apk permission Manifest with the list in Permissions_Android.py.

    This file is based on : https://github.com/urcuqui/WhiteHat/tree/master/Research/Android/scripts
"""
import Permissions_Android
import xml.etree.ElementTree as ET
import os
from os.path import join
from multiprocessing import Pool
import csv


def eraser(filename):
    """
    Remove all data in the apktool output to save data space.
    :param filename: filename of the APK.
    :return: None.
    """
    os.system("find Output{} -type f ! -name 'AndroidManifest.xml' -delete".format(filename))


def permissionParsing(package, writer, MORB):
    """
    This permission is used to read the XML, parse it and write in a csv file if a specific permission is present
    in current apk Manifest.
    :param package: Path to the current APK Manifest.
    :param writer: csv.writer object which keep a file open to write a row.
    :param MORB: Indicate if it's a Malware OR Benign.
    :return: None.
    """

    array_output = []
    try:
        print(package + "/AndroidManifest.xml")
        # Create entry point in xml
        tree = ET.parse(package + "/AndroidManifest.xml")
        treeRoot = tree.getroot()
        array_permissions = []
        # Browse all the file, check all occurrences of target and append it to a list
        # If you want to check other characteristics in a XML File you can replace the value in target by another one
        target = 'uses-permission'
        for permission in treeRoot.findall(target):
            # We get the value name of target
            per = permission.get('{http://schemas.android.com/apk/res/android}name')
            array_permissions.append(per)
        # We browse the list of permission, check if the current Manifest permission are in AOSP_PERMISSIONS
        for item in sorted(Permissions_Android.AOSP_PERMISSIONS):

            if array_permissions.__contains__(item):
                # We append to the array 1 if doesn't match
                array_output.append("1")
            else:
                # We append to the array 0 if doesn't match
                array_output.append("0")
        # We add the value of MORB to indicate if it's a malware or a benign application
        array_output.append(MORB)
        # Write a line in csvFile
        writer.writerow(array_output)
        print("wrote...")
    except:
        print("error")

def separate(filename, dataDir, dataDirDest, MORB):
    """
    This method is used to list all APK in the directory and create the header of the file.
    :param filename: Name of the CSV File.
    :param dataDir: Path to the directory which contains all files.
    :param dataDirDest: Path to the directory to store output.
    :param MORB: Indicates if it's a Malware or Benign directory.
    :return: None.
    """
    # We list the dataDir directory and store them
    fileList = os.listdir(dataDir)
    link = []
    i = 0
    csvFile = filename
    # We open the file and create a csv.writer
    fl = open(csvFile, 'w')
    writer = csv.writer(fl)
    array_data = []
    # We store all permissions and write them as header in csv file
    for criter in sorted(Permissions_Android.AOSP_PERMISSIONS):
        array_data.append(criter)
    # We add the malware column to indicate the type
    array_data.append("malware")
    writer.writerow(array_data)

    # For each file in the list we add the full path
    for e in fileList:
        link.append(join(dataDir, e))
    # For all files, we use apktool to extract the apk to dataDirDest
    for filename in fileList:
        os.system("apktool d -f {} -o {}Output{}".format(link[i], dataDirDest, filename))
        i += 1
        eraser(filename)
        permissionParsing(dataDirDest + "Output{}".format(filename), writer, MORB)

def parse(malDir,malDirDest, goodDir, goodDirDest):
    """
    Start 1 process to extract Manifest from APK in goodDir and start another process to extract Manifest from APK
    in malDir.
    :param malDir: Path to the malware APK directory.
    :param malDirDest: Path to the malware output directory.
    :param goodDir: Path to the benign APK directory.
    :param goodDirDest: Path to the benign output directory.
    :return: None.
    """
    # You can change filename here
    goodCsvFile = "binaryApps_BEN.csv"
    malwareCsvFile = "binaryApps_MAL.csv"

    # Create two process
    pool = Pool(processes=2)
    # Attribute data to each process and call separate()
    pool.apply_async(separate, args=(goodCsvFile, goodDir, goodDirDest, "-1"))
    pool.apply_async(separate, args=(malwareCsvFile, malDir, malDirDest, "1"))

    # Close Pool and let all the processes complete
    pool.close()
    pool.join()

