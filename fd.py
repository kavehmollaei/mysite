counter=0
while True:
    counter +=1
    if counter ==3:
        print("finish")
        break


try:

    for item in range(10):
        print(item)
except Exception as e:
    print(e)

