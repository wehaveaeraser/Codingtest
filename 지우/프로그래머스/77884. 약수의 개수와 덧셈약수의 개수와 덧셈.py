def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        count = 0
        for a in range(1,i+1):
            if i % a == 0:   #약수
                count += 1
        if count % 2 == 0:  #짝수이면 더하기
            answer += i
        else :              #홀수면 빼기
            answer -= i
            
    return answer
