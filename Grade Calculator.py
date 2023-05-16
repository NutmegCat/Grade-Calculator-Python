# Aaron Prince Anu

class gradeConverter:

    # initialize vars
    A = 'A' 
    B = 'B' 
    C = 'C' 
    D = 'D'
    F = 'F'
    grade = int(0)

    print("\nWhat is your grade?")
    grade = input()

    # grade range into character
    if 80 <= int(grade) <= 100:
        print("\nYou have an: " + A + "\n")
    elif 70 <= int(grade) <= 79:
        print("\nYou have a: " + B + "\n")
    elif 60 <= int(grade) <= 69:
        print("\nYou have a: " + C + "\n")
    elif 50 <= int(grade) <= 69:
        print("\nYou have a: " + D + "\n")
    elif isinstance(grade, int):
        print("\nInvalid\n")
        
    if int(grade) == 100:
        f = open("congratulations.txt", "w")
        f.write("wOw cOnGrAtUlAtIoNs :D\n")
        f.close
        
        f = open("congratulations.txt", "r")
        print(f.read())
    else:
        x = open("oof.txt", "w")
        x.write("oOf fOr tHe gRaDe tHo nO 100% iMaGiNe\n")
        x.close
        
        x = open("oof.txt", "r")
        print(x.read())