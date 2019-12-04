stopCopying = False
print("Hey how's it going?")
while stopCopying != True:
    cat = str(input())
    if(cat == "stop copying me"):
        print("K, YOU WIN!")
        stopCopying = True
    else:
        print(f"{cat} \n")