# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh 
# sab rule follow karne chaiye:
# 1.Kam se kam uski length 6 honi chaiye
# 2.Jada se jada length 16 se jyada na ho
# 3.Kam se kam ek dollar ka sign ($) hona chaiye
# 4.Kam se kam password mein 2 ya 8 hona chaiye
# 5.Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, 
# nahi toh "Weak Password" type karo



nam=input("enter your password ")
if len(nam)>6 and len(nam)<16:
    if "$" in nam:
        if "2" or "8" in nam:
            if "A" or"Z" in nam:
                print("strong password ")
            else:
                print("weak password ")
        else:
            print("weak password ")
    else:
            print("weak password ")
else:
    print("weak password ")
















