import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline'')as csv_file:
       writer = csv.writer(csv_file)
        
       writer.writerow(["name", "age", "contact Number", "E-Mail ID"])
       writer.writerow(info_list)
   
if __name =='__main__':         
      condition = True
      student_num = 1    
    
     while(condition):
       student_info = input("enter student informationfor student #{} in the following format(name age contact_number E-Mail_ID):".format(student_num))
       print("entered information: " + student_info)
  
   student_info_list = student_info.split(' ')
   print("entered split up information is: " + str(student_info_list))
   print("\nThe entered information is -\n Name: {}\nAge: {}\ncontact_number: {}\nE-mail ID: {}"
           .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
   choice_check = input("Is the entered information correct? (yes/no): ")
  
   if choice_check == "yes":
      write_info_csv(student_info_list)
      
   condition_check = input("enter (yes/no) if you want to enter information for another student: ")
   if condition_check == "yes":
      codition = True
      student_num = student_num + 1 
   elif condition_check == "no":
      condition = False 
   elif choice_check == "no":
      print("\nplease re_enter the values!") 
  
