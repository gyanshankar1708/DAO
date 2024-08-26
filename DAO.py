import mysql.connector as conn
def add_user():
    while True:
        db=conn.connect(host="localhost",user="root",password="rajput",database="profile")
        cur=db.cursor()
        uid=input("Enter Id->")
        a=(uid,)
        cur.execute("select Id from user_profile")
        rec=cur.fetchall()
        try:
            if a not in rec:
                pwd=input("Enter Password->")
                name=input("Enter Name->")
                mob=input("Enter Mobile number->")
                query="insert into user_profile(id,password,name,mobile_no) values('%s','%s','%s','%s')"%(uid,pwd,name,mob)
                cur.execute(query)
                db.commit()
                print("Profile Created Succesfully.")
                cur.close()
                db.close()
                break
            else:
                print('\n')
                print("User already exists.")
        except:
            print('\n')
            print("Something went wrong")

def login(uid,pwd):
    db=conn.connect(host="localhost",user="root",password="rajput",database="profile")
    cur=db.cursor()
    try:
        query="Select * from user_profile where Id='%s' and password='%s'"%(uid,pwd)
        cur.execute(query)
        rec=cur.fetchall()
        print('\n')
        print("Id->",rec[0][0],"\nName->",rec[0][2],"\nMobile Number->",rec[0][3],"\nDAO->",rec[0][4])
    except:
        print("Something Went Wrong.")

def transfer(uid):
    db=conn.connect(host="localhost",user="root",password="rajput",database="profile")
    cur=db.cursor()
    pwd=input("Enter Your Password->")
    tuid=input("Enter User id you want to transfer->")
    tdao=float(input("Enter DAO to transfer->"))
    try:
        while True:
            query="select dao from user_profile where Id='%s' and password='%s'" %(uid,pwd)
            query2="select dao from user_profile where Id='%s'"%(tuid)
            cur.execute(query)
            rec=cur.fetchone()
            cur.execute(query2)
            rec2=cur.fetchone()
            udao=rec2[0]
            dao=rec[0]
            if tdao<=dao:
                query3="update user_profile set dao='%f' where Id='%s'"%(dao-tdao,uid)
                query4="update user_profile set dao='%f' where Id='%s'"%(udao+tdao,tuid)
                cur.execute(query3)
                db.commit()
                cur.execute(query4)
                db.commit()
                print("Succesfully Transfered")
                break
            else:
                print("Insufficient DAO")
                print('\n')
    except:
        print("Something Went Wrong")   

       
def show_proposel():
    db=conn.connect(host="localhost",user="root",password="rajput",database="proposel")
    cur=db.cursor()
    query="select * from proposel"
    cur.execute(query)
    rec=cur.fetchall()
    for i in rec:
        print("Proposel->",i[1]," Issued by->",i[0]," No. of vote->",i[2])

def add_proposel(uid):
    db=conn.connect(host="localhost",user="root",password="rajput",database="proposel")
    cur=db.cursor()
    prop=input("Enter Proposel->")
    query="insert into proposel (issued_by, proposel) values('%s','%s')"%(uid,prop)
    cur.execute(query)
    db.commit()

def vote_plus(uid,proposel):
    db=conn.connect(host="localhost",user='root',password='rajput',database='profile')
    cur=db.cursor()
    votval=0
    try:
        cur.execute("select dao from user_profile where id='%s'"%uid)
        a=cur.fetchone()
        pval=a[0]
        print(pval)
        db2=conn.connect(host="localhost",user="root",password="rajput",database="proposel")
        cur2=db2.cursor()
        cur2.execute("select vote from proposel where proposel='%s'"%proposel)
        b=cur2.fetchone()
        nval=0.0
        if b[0]== None:
            nval=0.0
        else:
            nval=b[0]
        fval=pval+nval
        cur2.execute("Update proposel set vote='%f' where proposel='%s'"%(fval,proposel))
        db2.commit()
    except:
        print("Some error occured")

def vote_minus(uid,proposel):
    db=conn.connect(host="localhost",user='root',password='rajput',database='profile')
    cur=db.cursor()
    votval=0
    try:
        cur.execute("select dao from user_profile where id='%s'"%uid)
        a=cur.fetchone()
        pval=a[0]
        print(pval)
        db2=conn.connect(host="localhost",user="root",password="rajput",database="proposel")
        cur2=db2.cursor()
        cur2.execute("select vote from proposel where proposel='%s'"%proposel)
        b=cur2.fetchone()
        nval=0.0
        if b[0]== None:
            nval=0.0
        else:
            nval=b[0]
        fval=pval-nval
        cur2.execute("Update proposel set vote='%f' where proposel='%s'"%(fval,proposel))
        db2.commit()
    except:
        print("Some error occured")







print("1.Create id. \n2.Login.")
ch=int(input("Enter choice[1-2]->"))
if ch==1:
    add_user()
elif ch==2:
    uid=input("Enter Your id->")
    pwd=input("Enter Password->")
    login(uid,pwd)
    print("1.Add proposel. \n2.Show proposel")
    c=int(input("Enter your choice->"))
    if c==1:
        add_proposel(uid)
    elif c==2:
        show_proposel()
        pro=input("Enter Proposal to vote->")
        ans=input("Enter Y/N->")
        if ans=="Y" or ans=="y":
            vote_plus(uid,pro)
        elif ans=="N" or ans=="n":
            vote_minus(uid,pro)
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")

