#NUMBER 1

total = int(input("enter the total number of votes"))
can1 =int(input("Enter 1st votes: "))
can2 =int(input("Enter 2nd votes: "))







#Percentage of can1
percentage1 = ((can1)/(total))*100
print(f"percentage is{percentage1}%")

#percentage of can2
percentage2 =((can2)/(total))*100
print(f"percentage is{percentage2}%")



#NUMBER 2

voter_A= input("enter the number of votes for voter_A: ")
voter_B= input("Enter the number of votes for voter_B: ")
if voter_A > voter_B:
 print("voter_A is the winner")

else: 
    print("voter_b is the loser")


#NUMBER 4
user_name= input("Enter name of user: ")
print("Hello,",user_name)
age =int(input("Enter your age: "))
if age < 18:
    print("You are not eligible to vote")
else: print("Congratulations, You are eligible to vote")


#NUMBER 3
num_MPS= int(input("Enter the number of members of parliament: "))
ages= []
for i in range(num_MPS):
    age= int(input(f"Enter the age of member{i+1}:"))
    
#average age
total_age= sum(ages)
average_age= total_age/num_MPS
print(f"Average age is,{average_age:.2f}years")

#NUMBER 6
p_party_seats =500
p_party_no= 3
p_party_G_seats= int(input("Enter the number of seats at the party G: "))
Total_seats= int(input("Enter the total number of seats"))
if p_party_seats > 150:
    print("p_party G is the majority party")
else:
    print("p_party_G is not the majority party")



#NUMBER 5

total_num_votes = int(input("Enter the total number of votes: "))
percentage_votes1 = input("Enter the percentage received by p_party_1: ")
percentage_votes2 = input("Enter the percentage received by p_party_2: ")
#calculating the number of seats
p_party_1 = (percentage_votes1/100)*total_num_votes
p_party_2 = (percentage_votes2/100*total_num_votes)
