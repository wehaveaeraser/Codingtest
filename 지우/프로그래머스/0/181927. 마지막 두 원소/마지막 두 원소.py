def solution(num_list):
    num = 0  
    if num_list[-1] > num_list[-2]:
        num = int(num_list[-1]) - int(num_list[-2])
    else:
        num = int(num_list[-1])*2
    
    num_list.append(num)
    return num_list