marks1=int(input("enter your number 1"))
marks2=int(input("enter your number 2"))
marks3=int(input("enter your number 3"))
total_percentage=(100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed",total_percentage)

else:
    print("you failed") 