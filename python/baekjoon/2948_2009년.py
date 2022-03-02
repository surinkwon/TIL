md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day, month = map(int, input().split())
first_day = 2
total_day = first_day + day
for i in range(month):
    total_day += md[i]
print(days[total_day % 7])
