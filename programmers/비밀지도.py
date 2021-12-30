def solution(n, arr1, arr2):
    answer = []
    
    for a1,a2 in zip(arr1,arr2):
        s = bin(a1|a2)[2:].rjust(n,'0')
        s=s.replace('1','#')
        s=s.replace('0',' ')
        answer.append(s)
    
    return answer
