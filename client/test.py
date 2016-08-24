import pymysql
# class people: 
#   #定义基本属性 
#   name = '' 
#   age = 0 
#   #定义私有属性,私有属性在类外部无法直接进行访问 
#   __weight = 0 
#   #定义构造方法 
#   def __init__(self,n,a,w): 
#     self.name = n 
#     self.age = a 
#     self.__weight = w 
#   def speak(self): 
#     print("%s is speaking: I am %d years old" %(self.name,self.age)) 
 
 
# p = people('tom',10,30) 
# p.speak() 

def conn_databaes(acccount):
    conn = pymysql.connect(host = '192.168.84.140' ,user = 'chatroot' ,passwd = '000000' ,db = 'chat' ,charset = 'utf8')
    cur = conn.cursor()
    cur.execute("select * from user_passwd where username = '%s' " %acccount)
    for each in cur:
        return each[2]

info = conn_databaes('admin')
print(info)