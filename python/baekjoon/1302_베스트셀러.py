N = int(input())
books = [0] * N
selling = [0] * N
i = 0

# 책을 입력받고 그 책을 등록, 팔린 수 + 1
for _ in range(N):
    book = input()
    if book not in books:
        books[i] = book
        selling[i] += 1
        i += 1
    # 이미 등록된 책이면 팔린 수만 + 1
    else:
        selling[books.index(book)] += 1

best_sell_id = 0
# 베스트셀러 판별, 베스트셀러가 여러개일경우 사전에서 가장 빨리 나오는
# 책을 출력해야하므로 max를 쓰지 않고 이렇게 비교
for i in range(len(books)):
    if selling[best_sell_id] < selling[i]:
        best_sell_id = i
    elif selling[best_sell_id] == selling[i]:
        if books[best_sell_id] > books[i]:
            best_sell_id = i
    
    if books[i] == 0:
        break

print(books[best_sell_id])
