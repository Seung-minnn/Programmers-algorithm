from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    diff = participant_counter - completion_counter
    answer = list(diff)[0]
    return answer
