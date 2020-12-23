# list 관련 method
# append() : 리스트에 원소 삽입 O(1)
# sort() : 오름차순으로 정렬 O(NlogN)
# sort(reverse = True) : 내림차순 정렬
# insert(index, value) : 특정한 인덱스 위치에 원소 삽입 O(N)
# count(value) : 리스트에 특정한 값을 갖는 데이터의 개수 O(N)
# remove(value) : 특정한 값을 갖는 원소를 제거한다.
#                   해당 원소가 여러개라면, 하나만 제거 O(N)


a = [1, 4, 3]
print("a 리스트 : ", a)

a.append(2)
print("삽입 : ", a)

a.sort()
print("오름차순 정렬 : ", a)

a.sort(reverse=True)
print("내림차순 정렬 : ", a)

b = [4, 3, 2, 1]
print("b 리스트 : ", b)

b.reverse()
print("원소 뒤집기 : ", b)

b.insert(2, 3)
print("index 2에 3 추가 : ", b)

b.remove(1)
print("value = 1인 값 삭제 : ", b)


# 리스트에서 특정 값을 갖는 원소 모두 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}  # 집합 자료형

# remove_set에 포함되지 않은 value만 저장
result = [i for i in a if i not in remove_set]
print("집합 자료형 사용하여 특정 원소 제거 : ", result)



