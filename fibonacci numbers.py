# 피보나치 수열은 연속된 숫자의 합을 계속해서 붙여나갑니다.
# 1과 2부터 시작해서 10개까지 이어보면 다음과 같이 됩니다.
# ex) 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 400만을 초과하지 않는 값 중에 짝수 수열의 합을 구하세요.
def fibonacci(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    return fibonacci(a-1)+fibonacci(a-2)


n = int(input())
print(fibonacci(n))    
