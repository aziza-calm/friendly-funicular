import csv

csv_path = 'trips.csv'
d = list(csv.reader(open(csv_path)))
W = [0] * len(d)
L = [0] * len(d[0])

for i in range(len(d)):
    for j in range(len(d[i])):
        L[j] += float(d[i][j])
        W[i] += float(d[i][j])
print('This is L')
print(L)
print('This is W')
print(W)