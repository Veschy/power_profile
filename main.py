import pandas as pd

data_set = pd.read_csv('time_power_set.csv', delimiter=';', header=0)
set_list = list(data_set['Power'].tolist())
# print(set_list)
sum =0
for b in set_list:
    sum  += b
avg = round(sum/len(set_list))
rez = [0]
n, k = 0, 0
for t in range(len(set_list)):
    if set_list[t] < avg:
        k += set_list[t]-avg
        print(' меньше ', t, k )
    else:
        n += set_list[t]-avg
        print(' больше ', t, n)

#         print(rez)
# print(k)







