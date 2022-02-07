# 일곱 난쟁이

# 드워프들의 키
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# 9명 키의 합, 초과된 키
total_height = 0
for dwarf in dwarfs:
    total_height += dwarf
over_height = total_height - 100

# 초과된 키에서 드워프들의 키를 순서대로 빼봄
# 빼고 남은 키가 나머지 드워프 키 하나와 같으면 그 둘을 삭제
for dwarf_height in dwarfs:
    if (over_height - dwarf_height != dwarf_height) and (over_height - dwarf_height in dwarfs):
        dwarfs.remove(dwarf_height)
        dwarfs.remove(over_height - dwarf_height)
        break # 가능한 답이 여러 경우가 있을 수 있으므로 하나 찾으면 끝냄

dwarfs.sort()
rlt = ''
for dh in dwarfs:
    rlt += str(dh) + '\n'
print(rlt[:len(rlt)-1])