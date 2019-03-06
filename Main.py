import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from core.deepmcore import *
from multiprocessing import Process
from termcolor import colored

def menu():
    os.system("clear")
    print(colored("""
        .................................
        ...####...................####...
        ....####.................####....
        .....####......###......####.....
        ......####....#####....####......
        .......####..#######..####.......
        ........#################........
        .........#####.....#####.........
        ..........####.....####..........
==============================================
 [-] Make By Without ID
 [-] https://github.com/Wekai
 [-] Admin : Wekai
===============================================
1. BruteForce [ MEDSOS ]
2. Info Gathering
3. Web Hacking
4. Termux [ TOOLS ]
5. Fix [ ERROR ]
6. Update Tools [-]
7. About This Tools
8. Store
9. Coming Soon
================================================
10. EXIT
""", 'green'))

loop = True

while loop:
    menu()
    Wekai = raw_input("Wekai > ")

    if Wekai == "1":
          os.system("clear")
          achacking()
    elif Wekai == "2":
          os.system("clear")
          info()
    elif Wekai == "3":
          os.system("clear")
          webhacking()
    elif Wekai == "4":
          os.system("clear")
          termux()
    elif Wekai == "5":
          os.system("clear")
          Fix()
    elif Wekai == "6":
          os.system("chmod +x update")
          os.system("./update")
    elif Wekai == "7":
          About()
    elif Wekai == "8":
         os.system("clear")
         deepstore()
    elif Wekai == "9":
         print (colored("under progress...", 'green'))
         timeout(3)
         restartprogram()
    elif Wekai == "10":
        sys.exit()
    elif Wekai == "0":
          restartprogram()
    else:
                  print  (colored("ERROR : [ KONTOL ]", 'red'))
                  timeout(2)
                  restartprogram()
