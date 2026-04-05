import re
file=open(r"D:\important text\Atm_data.text", "a")
file=open(r"D:\important text\Atm_data.text", "r")
file_read=file.read()
users={

}
file.seek(0)
if file_read:
    for x in file.readlines():
        name=re.split(":", x,maxsplit= 1)[0]
        values=re.split(":", x,maxsplit= 1)[1]
        values=re.split(",", values)
        money=re.split(":", values[0])
        password=re.split(":", values[1])
        password_int=[]
        for x in password[1]:
            if x in ["\n"]:
             pass
            else:
             password_int.append(x)
        password[1]="".join(password_int)
        users[name]={money[0]:int(money[1]), password[0]:password[1].strip()}
else:
    pass
new_old=input("is this your first time here [y or n]: ".title()).strip().lower()
while True:
   if new_old in ["yes", "y", "n", "no"]:
      break
   else:
      new_old=input(f"your input [{new_old}] please input yes or no: ".title()).strip().lower()
if new_old in ["no", "n"]:
   while True:
    user_name=input("please write your user name: ".title()).strip()
    user_password=input("please write your password: ".title()).strip()
    if user_name in users.keys() and users[user_name][password[0]]==user_password:       
       while True:
        the_order=input("choose what do you want [withdrawal or deposit]: ".title()).strip().lower()
        if the_order in ["withdrawal",  "deposit"]:
           the_order=the_order
           break
        else:
           print(f"your input [{the_order}] please choice from [withdrawal or deposit]".title())
       while True:
        if the_order=="withdrawal":
          the_withdrawal_money=input("please write the total money you want to withdrawal: ".title()).strip()
          while True:
             try:
                the_withdrawal_money=int(the_withdrawal_money)
                break
             except:
                the_withdrawal_money=input(f"your input [{the_withdrawal_money}] pleas write a digits: ".title()).strip()
          if the_withdrawal_money>users[user_name][money[0]]:
             print("Your current balance is not enough to do this operation".title())
             continue
          else:
             users[user_name][money[0]]=int(money[1])-the_withdrawal_money
             print("The operation was completed successfully".title())
             break
        else:
          the_deposit_money=input("please write the total money you want to deposit: ".title()).strip()
          while True:
             try:
                the_deposit_money=int(the_deposit_money)
                break
             except:
                the_deposit_money=input(f"your input [{the_deposit_money}] pleas write a digits: ".title()).strip()
          users[user_name][money[0]]=int(money[1])+the_deposit_money
          print("The operation was completed successfully :)".title())
          break
       break
    file=open(r"D:\important text\Atm_data.text", "w")
    for x in users.keys():
      file.write(f"{x}:{money[0]}:{users[x][money[0]]}, {password[0].strip()}:{users[x][password[0]]}\n")
    else:
      print("the user name or password is wrong pleas write again")
else:
   order=input("do you want make acount [y or n]: ".title()).strip().lower()
   while True:
    if order in ["y", "yes"]:
       user_name=input("pleas write user name: ".title()).strip()
       user_password=input("pleas write a password: ".title()).strip()
       if user_name and user_password:
          if user_name in users.keys():
             print("this is user name already taken sorry :)")
          else:
             users[user_name]={"money":0, "password":user_password}
             print("The operation was completed successfully :)".title())
             order_2=input("do you want deposit a money in the first: ".title()).strip().lower()
             if order_2 in ["y", "yes"]:
                the_deposit_money=input("please write the total money you want to deposit: ".title()).strip()
                while True:
                   try:
                      the_deposit_money=int(the_deposit_money)
                      break
                   except:
                      the_deposit_money=input(f"you write [{the_deposit_money}] pleas write a digits".title()).strip()
                users[user_name]["money"]=the_deposit_money
                print("The operation was completed successfully :)")
                file=open(r"D:\important text\Atm_data.text", "a")
                file.write(f"{user_name}:money:{users[user_name]["money"]}, password:{users[user_name]["password"]}\n")
                break
             elif order_2 in ["n", "no"]:
                print("have a nice day :)")
                file=open(r"D:\important text\Atm_data.text", "a")
                file.write(f"{user_name}:money:{users[user_name]["money"]}, password:{users[user_name]["password"]}\n") 
                break
             else:
                print("please write [yes or no]")
                continue
       else:
          print("pleas write a user name and password".title())
          continue
    elif order in ["n", "no"]:
       print("have a nice day :)".title())
       break
    else:
       order=input(f"you write [{order}] pleas write [yes or no]: ".title()).strip().lower()