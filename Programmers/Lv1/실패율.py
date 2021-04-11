def solution(N, stages):
    answer = []
    error_list = {}
    stage_list = {}

    for i in range(1, N+1, 1):
        stage_list[i] = 0
        error_list[i] = 0

    for i, v in enumerate(stages):
        if v == N+1:
            continue
        stage_list[v] += 1

    total_num = len(stages)
    for i in range(1, N+1, 1):
        if total_num <= 0:
            break
        temp = stage_list[i]/total_num
        total_num -= stage_list[i]
        error_list[i] = temp

    # t1_array:keys, t2_array:values
    t1_array = list(error_list.keys())
    t2_array = list(error_list.values())

    for i in range(0, N):
        temp = t2_array.index(max(t2_array))
        answer.append(t1_array[temp])
        t2_array.pop(temp)
        t1_array.pop(temp)

    
    return answer
