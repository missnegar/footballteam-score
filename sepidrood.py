counter = 0
scores = []
for _ in range(30):    
    num = int(input(""))
    scores.append(num)
    totalscore = sum(scores)
    if num == 3:     
        counter = 1+counter
print("scores is :",totalscore ,counter)