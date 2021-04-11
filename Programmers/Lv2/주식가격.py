def solution(prices):
    answer = []
    for i,x in enumerate(prices):
        num=0
        for j in range(i+1,len(prices)):
            if(x<=prices[j]):
                num+=1
            else:
                num+=1
                break
        answer.append(num)
    return answer
