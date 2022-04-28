N = int(input())

rlt_lst = [N]
lst_len = 1

# 반 이하의 수들은 볼 필요 없음(자기 자신일 때보다 적기 때문에)
for i in range(N, N // 2, -1):
    tmp_lst = [N, i]
    n = 1
    while tmp_lst[n - 1] - tmp_lst[n] >= 0:
        tmp_lst.append(tmp_lst[n - 1] - tmp_lst[n])
        n += 1
    
    if lst_len < n + 1:
        rlt_lst = tmp_lst[:]
        lst_len = n + 1
    elif lst_len > n + 1:
        break

print(lst_len)
print(' '.join([str(x) for x in rlt_lst]))