w=""
g=""



import sqlite3
connection = sqlite3.connect('mathites.db')

cursor = connection.cursor()

cursor.execute(
    '''
        create table if not exists mathites(
        id integer primary key,
        ONOMA text,
        THLEFWNO text)
    ''')
cursor.execute(
    ''' Select count (*) from mathites
    ''')

records=cursor.fetchall()
print records

record=records[0]
print record
if record[0]==0:
    cursor.execute('INSERT INTO mathites(ONOMA,THLEFWNO) VALUES("KWSTAS","7646546")')
    cursor.execute('INSERT INTO mathites(ONOMA,THLEFWNO) VALUES("MARIA","1456784")')
    connection.commit()

cursor.execute(
    ''' Select id ,ONOMA,THLEFWNO from mathites
    ''')
records=cursor.fetchall()
L=[]
for record in records:
    dict1={
        "id" : 0 ,
        "ONOMA" : "",
        "THLEFWNO" : ""
        }
    dict1["id"]=record[0]
    dict1["ONOMA"]=record[1]
    dict1["THLEFWNO"]=record[2]
    L.append(dict1)
    
    



while True:
    i=1
    for item in L:
        print i, item["ONOMA"],item["THLEFWNO"]
        i+=1
    print "1:EISAGWGH 2:DIAGRAFH 3:EPEKSERGASIA 4:TAKSINOMHSH 9:EKSODOS"
    x=input("")
    if x==1:
        y=raw_input("BALE ONOMA")
        t=input("DWSE THLEFWNO")
        m={"ONOMA" : "",
      "THLEFWNO" : ""}
        m["ONOMA"]=y
        m["THLEFWNO"]=t
        L.append(m)

    elif x==2:
        z=input("POIO THES NA BGALEIS")
        if z==1:
            L.pop(0)
        elif z==2:
            L.pop(1)
        else:
            L.pop()

    elif x==3:
        e=input("POIO THELEIS NA EPEKSERGASTEIS")
        w=raw_input("EPEKSERGASE ONOMA")
        g=input("BALE THLEFWNO")
        dict3={"ONOMA" : "", "THLEFWNO" : ""}
        dict3["ONOMA"]=w
        dict3["THLEFWNO"]=g
        L[e-1]=dict3

        

    elif x==9:
        exit()



    
    

