cw_score=float(input("Enter your  cw score"))
if 0<=cw_score<=50:
    break
else:
    print("please enter a value between 0 and 50")
    
    #getting class attendance
    while True:
        attendance=input("did you attend class?(yes/no):").strip().lower()
        if attendance in["yes","no"]:
            break
        else:
            print("Please enter 'yes'or'no'.")
            
            #check cw pass mark and attendance
            
            cw_passmark =17.5 
            if attendance>= cw_passmark and attendance == "yes":
                print("You passed the CW and attended the class. You are allowed to take the exam")
                
                #get EX score from user
                while True: 
                    try:
                         ex_score = float(input("Enter your EX score out of 50:"))
                    if 0 <= ex_score <=50:
                        break
                    else:
                        print ("Please enter a score between 0 and 50.")
                    except ValueError: print("Invalid input")
                        
                        #check EX pass mark
                        
            ex_passmark =17.5
if ex_score >= ex_passmark:
                            print("congratulations! you passed the exam and are allowed to move to semester 2")
                        else:
                            print("Unfortunately, you did not pass the exam. you cannot move to semester 2")
                        
                            if cw_score<cw_passmark:
                                print("Unfortunately, you did not pass the CW.")
                                if attendance == "no":
                                    print("you did not attend class/n you are not allowed to take the exam")
                    