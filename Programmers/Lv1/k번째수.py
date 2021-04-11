def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        l = array[commands[i][0]-1:commands[i][1]]
        l.sort()
        answer.append(l[(commands[i][2]-1)])
    return answer
