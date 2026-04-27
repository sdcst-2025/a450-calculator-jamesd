#!python3
#Calculator
# Feel free to rename your variables
import os 
import math

def name():
    # Displays the title screen!
    # No input or output needed :3
    # Author: Copper
    # Modified: April 26th, 2026. 
    print(" ----------------------------------------------------------------------------------------")
    print("|  ■■■■     ■     ■        ■■■■   ■     ■   ■         ■     ■■■■■■■    ■■■■■    ■■■■■    |")
    print("| ■       ■   ■   ■       ■       ■     ■   ■       ■   ■      ■      ■     ■   ■    ■   |")
    print("| ■       ■■■■■   ■       ■       ■     ■   ■       ■■■■■      ■      ■     ■   ■■■■■    |")
    print("|  ■■■■   ■   ■   ■■■■■    ■■■■    ■■■■■    ■■■■■   ■   ■      ■       ■■■■■    ■    ■   |")
    print(" ----------------------------------------------------------------------------------------")
    print('                                       April 26th, 2026')

def menu():
    #Displays the Main Menu. 
    #Shows you controls 
    print("1. Calculate")
    print("2. Instructions")
    print("3. Exit")
    inp = 1000
    while inp > 3:
        try:
            inp = int(input("Select a number: "))
        except:
            print("Invalid number")
    return inp    

def redo():
    print("")
    print("1. Again")
    print("2. Menu")
    num = 2
    while num == 2:
        num = int(input("Select a number: "))
        if num == 1:
            print("Redoing")
        elif num == 2:
            cont = 2
            num = 2
            break
        else:
            print("Invalid Number")
        return cont

def volu():
    os.system('cls')
    shape = 100    
    print("VOLUME")
    print("")
    print("1. Rectangular Prism")
    print("2. Cylinder")
    print("3. Sphere")
    print("4. Equilateral Triangle")
    print("5. Pyramid")
    print("6. Cone")
    print("7. Exit")
    print("")
    while shape > 7:
        try:
            shape = int(input("Select a number: "))
        except:
            print("Invalid number")
    volusel(shape)

def volusel(num):
    if num == 1:
        cube()
    elif num ==2:
        cylinder()
    elif num ==3:
        sphere()
    elif num ==4:
        eqtri()
    elif num ==5:
        pyramid()
    elif num == 6:
        cone()
    elif num == 7:
        return None

def cube():
    cont = 1
    while cont != 2:
        os.system('cls')    
        print("RECTANGULAR PRISM VOLUME")
        print("")
        try:
            len = float(input("Write the Length: "))
            hei = float(input("Write the Height: "))
            wid = float(input("Write the Width: "))
            print("")
            print(f"Length: {len}")
            print(f"Height: {hei}")
            print(f"Width: {wid}")
            print("")
            print(f"Volume: {len*hei*wid}")
            cont = redo()
        except:
            print("Invalid Number")

def cylinder():
    cont = 1
    while cont != 2:
        try:
            os.system('cls')    
            print("CYLINDER VOLUME")
            print("")
            rad = float(input("Write the Radius: "))
            hei = float(input("Write the Height: "))
            print("")
            print(f"Radius: {rad}")
            print(f"Height: {hei}")
            print("")
            print(f"Volume: {math.pi * (rad*rad) * hei}")
            cont = redo()
        except:
            print ("Invalid Number")
            
def sphere():
    cont = 1
    while cont != 2:
        os.system('cls')    
        print("SHPERE VOLUME")
        print("")
        try:
            rad = float(input("Write the Radius: "))
            print("")
            print (f"Radius: {rad}")
            print("")
            print (f"Volume: {4/3 * math.pi * (rad*rad*rad)}")
            cont = redo()
        except:
            print("Invalid Number")

def eqtri():
    cont = 1
    while cont != 2:
        os.system('cls')    
        print("EQUILATERAL TRIANGLE VOLUME")
        print("")
        try:
            len = float(input("Write the Lengths: "))
            hei = float(input("Write the Height: "))
            print("")
            print (f"Length: {len}")
            print (f"Height: {hei}")
            print ("")
            print (f"Volume: {(math.sqrt(3)/4)*(len*len)*hei}")
            cont = redo()
        except:
            print("Invalid Number")

def pyramid():
    cont = 1
    while cont != 2:
        os.system('cls')    
        print("PYRAMID VOLUME")
        print("")
        try:
            len = float(input("Write the Length: "))
            hei = float(input("Write the Height: "))
            wid = float(input("Write the Width: "))
            print("")
            print(f"Length: {len}")
            print(f"Height: {hei}")
            print(f"Width: {wid}")
            print("")
            print(f"Volume: {(len*wid*hei)/3}")
            cont = redo()
        except:
            print("Invalid Number")

def cone():
    cont = 1
    while cont != 2:
        os.system('cls')    
        print("CONE VOLUME")
        print("")
        try:
            rad = float(input("Write the Radius: "))
            hei = float(input("Write the Height: "))
            print("")
            print(f"Radius: {rad}")
            print(f"Height: {hei}")
            print("")
            print(f"Volume: {math.pi*(rad*rad)*(hei/3)}")
            cont = redo()
        except:
            print("Invalid Number")

def inst():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: 
    # Modified: 
    os.system('cls')    
    print("INSTRUCTIONS")
    print("----------------")
    print("This is a calculator for determining the volume of several 3D shapes.")
    print('When the program says to "Select a number:" input one of the numbers')
    print("shown next to an option to select that option.")
    print('After seleceting a volume to calculate you should') 
    print('input the needed dimensions of that shape.')
    print("----------------")
    print("")
    try:
        (input("Input any value to exit: "))
    except:
        print("Invalid")

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    burger = 'redo'
    while burger == 'redo':
        name()
        inp = menu()
        if inp == 1:
            volu()
        elif inp ==2:
            inst()
        elif inp ==3:
           os.system('cls')
           burger = 'quit'   
    

if __name__ == "__main__":
    main()
    print("Thanks for using the calculator!")