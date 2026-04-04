n = int(input("Enter how many lines you gonna type: "))

ans=[]
for i in range(n):
    word = input("Enter you word: ")
    if len(word)>10:
        tem = word[0]+str(len(word)-2)+word[-1]
        ans.append(tem)
    else:
        ans.append(word)
        
for i in ans:
    print(i)