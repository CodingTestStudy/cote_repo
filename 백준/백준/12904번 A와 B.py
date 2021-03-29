import sys
sys.setrecursionlimit(10**5)
S = list(input())
T = list(input())
# delete_A() : 문자열의 뒤에 A 삭제
# delete_B() : 문자열의 뒤에 B 삭제 후, 뒤집기
# S를 T로 바꿀수 있다면, 반대로 T로도 S를 만들 수 있어야 한다.

def delete_A(X):
    if not X: return False # 문자열이 전부 삭제되었다면, T로 S를 못만듬
    if X == S: return True # S가 만들어지면 True
    if X[-1] != 'A': return False # 맨뒤의 값이 A가 아니라면 삭제 불가
    else: # 맨뒤가 A이기 때문에, A삭제 후, 다시 삭제 연산들 반복
        X.pop()
        return delete_A(X) or delete_B(X) # 둘 중 하나만 성공하면 됨

def delete_B(X): # delete_A 함수와 동일 (문자열 뒤집기만 추가됨)
    if not X: return False
    if X == S: return True
    if X[-1] != 'B':
        return False
    else: # 맨뒤가 B이기 떄문에, B삭제
        X.pop()
        X.reverse() # 삭제 후, 문자열 뒤집기
        return delete_A(X) or delete_B(X)

if delete_A(T) or delete_B(T): print(1) # 둘중 하나라도 성공했다면
else: print(0)