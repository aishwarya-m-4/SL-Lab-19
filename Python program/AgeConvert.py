from datetime import date 
  
def ageConvert(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 
      
# Driver code  
dob = input("Enter date of birth: ")
num = dob.split("-")
print(ageConvert(date(int(num[2]),int(num[1]),int(num[0]))), "years") 
