# координаты точек по четвертям

a = [tuple(map(int, input().split())) for n in range(int(input()))]
print('Первая четверть: {}'.format(sum([1 for t in a if t[0] > 0 and t[1] > 0])))
print('Вторая четверть: {}'.format(sum([1 for t in a if t[0] < 0 and t[1] > 0])))
print('Третья четверть: {}'.format(sum([1 for t in a if t[0] < 0 and t[1] < 0])))
print('Четвертая четверть: {}'.format(sum([1 for t in a if t[0] > 0 and t[1] < 0])))


xy = [[0,0],[0,0]]
for i in range(int(input())):
    x, y = map(int, input().split())
    if x!=0 and y!=0:
        xy[x>0][y>0] += 1
print(f'Первая четверть: {xy[1][1]}')
print(f'Вторая четверть: {xy[0][1]}')
print(f'Третья четверть: {xy[0][0]}')
print(f'Четвертая четверть: {xy[1][0]}')


s = int(input())

I, II, III, IV = 0, 0, 0, 0

def quarter_check(x, y):
    global I, II, III, IV
    if (x > 0 and y > 0): I += 1
    if (x < 0 and y > 0): II += 1
    if (x < 0 and y < 0): III += 1
    if (x > 0 and y < 0): IV += 1

for i in range(s):
    x, y = map(int, input().split())
    quarter_check(x, y)

print("Первая четверть: {}".format(I))
print("Вторая четверть: {}".format(II))
print("Третья четверть: {}".format(III))
print("Четвертая четверть: {}".format(IV))