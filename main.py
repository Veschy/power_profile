import pandas as pd

data_set = pd.read_csv('time_power_set.csv', delimiter=';', header=0)
set_list = list(data_set['Power'].tolist())
sum =0
for b in set_list:
    sum += b
avg = round(sum/(len(set_list)-1))
print(avg)
rez = []
time_less, time_more, power_less, power_more = 0, 0, 0, 0
time = 0
for t1 in range(len(set_list)):
    if set_list[t1] < avg:
        if time_more > 0:
            rez.append([time_more, power_more, round(power_more / time_more)])
        power_more = 0
        time_more = 0
        power_less += set_list[t1] - avg
        time_less += 1
    else:
        if time_less > 0:
            rez.append([time_less,power_less, round(power_less/time_less)])
        power_less = 0
        time_less = 0
        power_more += set_list[t1] - avg
        time_more += 1
for t2 in range(len(rez)):
    print('длительность / энергия / средняя мощность ', rez[t2])
print('Среднее значение  мощности за всю выборку =', avg)
print('Количетсво интервалов', len(rez))






