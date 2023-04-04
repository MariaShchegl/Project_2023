# -*- coding: utf-8 -*-

import os
import time
import sys

def console_header(drives):
	print("==== Defragmentation Utility ====\n\nExisting drives:\n")
	print(" Том Имя Метка ФС Тип Размер Состояние Сведения\n"\
		" ----- ---- --------- ---- -------- ------ --------- --------")
	for item in drives:
		print(item)
	print(" ---------------------------------------------------------------------------")


def get_drives_letters():
	diskpart_file = "C:\drive_info.txt"
	drives = list()
	os.system("chcp 65001 >> localhost") # использование в командной строке кодировки UTF-8
	os.system("echo list volume|diskpart >>" + diskpart_file) # запись в файл списка дисковых устройств
	for string in open(diskpart_file, "r", encoding='utf8').readlines():
		if string.find("Том") != -1:
			if string.find("NTFS") != -1 or string.find("FAT32") != -1:	
				drives.append(string)
	os.system("del "+diskpart_file)
	return drives


def drives_analyzer(drive, drives):
    letters = list()
    drive_list = drive.split(", ")
    for item in drives:
        letters.append(item[15]+":")
    if drive_list[0] != "ALL":
        try:
            filename = "C:\ANALYSIS_" + timestamp() + ".log"
            os.system("chcp 65001 >> localhost")
            error = os.system("defrag.exe " + " ".join(drive_list) + " /A >> " + filename)
            if error == 0:
                return filename
            else:
                return False
        except:
            return False
    elif drive_list[0] == "ALL":
        try:
            filename = "C:\ANALYSIS_" + timestamp() + ".log"
            os.system("chcp 65001 >> localhost")
            error = os.system("defrag.exe " + " ".join(letters) + " /A >> " + filename)
            if error == 0:
                return filename
            else:
                return False
        except:
            return False
    else:
        return False
        

def drives_defrager(drive, drives):
    letters = list()
    drive_list = drive.split(", ")
    for item in drives:
        letters.append(item[15]+":")
    if drive_list[0] != "ALL":
        try:
            filename = "C:\DEFRAG_" + timestamp() + ".log"
            os.system("chcp 65001 >> localhost")
            os.system("defrag.exe " + " ".join(drive_list) + " /V >> " + filename)
            return filename
        except:
            return False
    elif drive_list[0] == "ALL":
        try:
            filename = "C:\DEFRAG_" + timestamp() + ".log"
            os.system("chcp 65001 >> localhost")
            os.system("defrag.exe /C /V >> " + filename)
            return filename
        except:
            return False
    else:
        return False

def timestamp():
    return time.strftime("%d_%m_%Y[%H-%M-%S]", time.localtime())
    
    
if __name__ == "__main__":
    drives = get_drives_letters()
    while True:
        os.system("cls")
        console_header(drives)
        key = input("A - analyze drives\n"
        "D - defragment drives\n"
        "EXIT - exit utility\n"
        ">>> ")
        
        if key == "A":
            os.system("cls")
            console_header(drives)
            drive = input("Match drives by the comma.\n"
            "Example: C:, D:\n"
            "(ALL - for all drives): ")
            os.system("cls")
            print("Starting analysis drives: " + drive)
            print("Please, wait. It can take few minutes...")
            result = drives_analyzer(drive, drives)
            if result:
                os.system("cls")
                print("Analysis successful!\n" \
                "Log file: " + result)
                print_key = input("Print log file? [y/n]")
                if print_key == "y":
                    f = open(result, "r", encoding='utf8')
                    os.system("cls")
                    print(f.read())
                    f.close()
                    input("Press [ENTER] to continue...")
            else:
                os.system("cls")
                print("Error occurred while analysis!")
                input("Press [ENTER] to continue...")
                
        elif key == "D":
            os.system("cls")
            console_header(drives)
            drive = input("Match name of drives by the comma.\n"
            "Example: C:, D:\n"
            "(ALL - for all drives): ")
            os.system("cls")
            print("Starting defragmentation drives: " + drive)
            print("Please, wait. It can take a few minutes...")
            result = drives_defrager(drive, drives)
            if result:
                os.system("cls")
                print("Defragmentation successful!\n" \
                "Log file: " + result )
                print_key = input("Print log file? [y/n]")
                if print_key == "y":
                    f = open(result, "r", encoding='utf8')
                    os.system("cls")
                    print(f.read())
                    f.close()
                    input("Press [ENTER] to continue...")
            else:
                os.system("cls")
                print("Error occurred while defragmentation!")
                input("Press [ENTER] to continue...")
    
        elif key == "EXIT":
            os.system("cls")
            os.system("del C:\Course\Defrag_test1\localhost")
            sys.exit(0)
            
        else:
            os.system("cls")
            console_header(drives)
            print("Wrong parameter!")
            input("Press [ENTER] to continue...")