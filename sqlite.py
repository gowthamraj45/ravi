##import sqlite3
##a=sqlite3.connect("new.dp")
##cr=a.cursor()
##a.execute("create table if not exists marks(c1,c2,c3)")
##a.execute("insert into marks values(1,2,3)")
##a.commit()
##cr.execute("select * from marks")
##b=cr.fetchall()
##print(b)


# import sqlite3

# a= sqlite3.connect('test3.db')
# cr=a.cursor()
# a.execute('''CREATE TABLE if not exists data
#          (Name INT PRIMARY KEY   NOT NULL,
#          gmail       TEXT    NOT NULL,
#          pwd         INT     NOT NULL)''')
# ##a.execute("INSERT INTO COMPANY (ID,NAME,AGE) \
# ##      VALUES (1, 'Paul', 32)")
# a.execute("INSERT INTO COMPANY (NAME,GMAIL,PWD) \
#      VALUES ('Gowtham','gowtham@gmail.com',45456),")
# # a.execute("INSERT INTO COMPANY (name,gmail,pwd) VALUES (gowtham,gow@gmail.com,123456)")
# # c=input("Enter the value : ")
# # d=input("Enter the value : ")
# # e=int(input("Enter the value : "))
# # a.execute("INSERT INTO COMPANY (ID,NAME,AGE) VALUES (?,?,?)",(c,d,e))
# a.commit()

# cr.execute("select * from data")
# ##b=cr.fetchmany(2)
# b=cr.fetchall()
# print(b)

import sqlite3
connection=sqlite3.connect("test4.db")
cursor=connection.cursor()
# a="""create table student(
#       Rollno int primarykey,
#      ename varcher(20));"""
# cursor.execute(a)
a="""insert into student
     (Rollno,ename)
     values(2,"viknesh")"""
cursor.execute(a)
connection.commit()
print("table created")

# import sqlite3 
# connection = sqlite3.connect("Academy.db")
# cursor = connection.cursor() 
# a = [("Thiru","C","M","75.2","1998-05-17"),("Raja","B","F","75.2","1998-04-17")]
# for p in a: 
#      format_str = """INSERT INTO Student
#      (Rollno, Sname, Grade, Gender, Average,birth_date) 
#      VALUES(Null,​"{name}","{gr}","{gender}","{avg}", "{birthdate}");"""

#      b=format_str.format(name=p[0],gr=p[1],gender=p[2], avg=p[3],birthdate=p[4])
#      cursor.execute(b)
# connection.commit() 
# connection.close() 
# print("Records added")