from Matrix import *
from LinearEq import *

def main():
    while True:
        print("----------------------------- MAIN MENU ---------------------------------")
        print("Choose the program:")
        print("1. Metrix Operation")
        print("2. Solve Linear equations")
        print("0. CLOSE THE PROGRAM")
        print("---------------------------------------------------------------")
        p = int(input("Choose an option 1-2 : "))

        if p == 1 :
            run_Matrix()
        elif p ==2 :
            run_Linear_Equation()
        elif p == 0:
            exit()
        else:
            print("Invalid Input")

main()