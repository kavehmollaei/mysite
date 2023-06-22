counter=0
while True:
    counter +=1
    if counter ==3:
        print("finish")
        break

#comment
try:

    for item in range(10):
        print(item)
except Exception as e:
    print(e)


def func_add(a,b):
    return a + b

def string(a:str)->str:
    if "admin" in a:
        print('Exists')
        return True
    return False
    
    
lst=['kaveh@gmail.com',
'noora@gmail.com']

for item in lst:
    print(item)


lambda x: 2*x
