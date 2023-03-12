import pywhatkit
from datetime import datetime
import mysql.connector as myconnect
import random
a=""
for i in range(0,6):
    a+=str(random.randint(0,9))
b=list(a)
random.shuffle(b)
c=""
for i in b:
    c+=i
print(c)    
con=myconnect.connect(host='localhost',user='root',password='kesavmelo2002',database='food')
# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt1=dt_string[11:13]
dt2=dt_string[14:16]
print("date and time =",dt2)	

query1="select max(phoneid) from phoneno"
mycur=con.cursor()
mycur.execute(query1)
row1=mycur.fetchall()
query2="select phonenum from phoneno where phoneid={}".format(row1[0][0])
mycur=con.cursor()
mycur.execute(query2)
row2=mycur.fetchall()
pywhatkit.sendwhatmsg('+91'+row2[0][0],"OTP is "+c,int(dt1),int(dt2)+1)
query="select max(otpid) from otptable"
mycur=con.cursor()
mycur.execute(query)
row1=mycur.fetchall()
h=row1[0][0]+1
query="insert into otptable values({},'{}')".format(h,c)
mycur=con.cursor()
mycur.execute(query)
con.commit()
mycur.close()
