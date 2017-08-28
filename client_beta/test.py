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

# def conn_databaes(acccount):
#     conn = pymysql.connect(host = '192.168.84.140' ,user = 'chatroot' ,passwd = '000000' ,db = 'chat' ,charset = 'utf8')
#     cur = conn.cursor()
#     cur.execute("select * from user_passwd where username = '%s' " %acccount)
#     for each in cur:
#         return each[2]

# info = conn_databaes('admin')
# print(info)


# def mymap(*seqs,pad=None):
#     seqs = [list(S) for S in seqs]
#     print(seqs)
#     res = []
#     while any(seqs):
#         res.append(tuple((S.pop(0) if S else pad) for S in seqs))
#         return res
# s1,s2 = 'abc','xyz123'
# print(s1)
# print(s2)
# print(mymap(s1,s2))



def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        print (listLength)
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]:
                bubbleList[i] = bubbleList[i] + bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength -= 1
    print(bubbleList)
 
if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    bubble(bubbleList)