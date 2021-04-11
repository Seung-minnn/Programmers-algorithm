# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
import math

def solution(progresses, speeds):
    answer = []
    size = len(progresses) # 입력 리스트의 크기
    point = 0 # 리스트 요소를 가리키는 인덱스 역할
    count = 0

    for i in range(size) :
        progresses[i] = math.ceil((100 - progresses[i]) // speeds[i])
        # 완료까지 필요한 기간을 구해서 올림으로 저장

    while point+count < size :
        if progresses[point] >= progresses[point+count] :
            # 앞에 있는 기능을 구현하는데 필요한 기간이 뒤에 보다 크다는 것
            # 더 오래 걸리기 때문에 구현 완성됐을 때 함께 배포 가능하다는 것
            count += 1 # 함께 배포되는 기능의 수 증가
        else : # 뒤에 기능이 더 오래걸린다면
            answer.append(count) # 이미 완성해서 배포 가능한 기능의 수를 리스트에 추가
            point += count # 더 오래 걸리는 기능으로 인덱스 수정
            count = 0 # 같이 배포하는 기능의 수는 0으로 리셋
            
    answer.append(count) # while 문 마지막에 count를 추가하지 못해서 한번 더 수행
    print(answer)
    return answer

input_progresses = [5, 5, 5]
input_speeds = [21, 25, 20]
solution(input_progresses, input_speeds)
