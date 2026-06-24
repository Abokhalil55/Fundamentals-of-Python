choice ="Y"
#start the loop
while choice == "Y":
    #Entering the quize(1,2,3) marks
    quize_1 = int(input("Enter Quize 1 Mark: "))
    quize_2 = int(input("Enter Quize 1 Mark: "))
    quize_3 = int(input("Enter Quize 1 Mark: "))

    #Calculte the average mark of the 3 quizes 
    average = (quize_1+quize_2+quize_3) / 3

    #Check if the mark is equal or over 50
    if average >= 50:
        print("Student passed the subject.")
    else:
        print("Student fail the subject.")
    
    # Choose either rerun the cod eor not
    choice= input("Continue? Selecet Y/N: ")

print("Program Ended")