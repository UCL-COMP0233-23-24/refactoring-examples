
# Funtion to open a file
def openFile(fileName):
    with open(fileName) as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data.append(row)
    return data

# Opening both data sets
data1 = openFile('data1.csv')
data2 = openFile('data2.csv')


with open('weights.csv') as file:
    lines = file.read()
    weights = []
    for n in lines.split(','):
        weights.append(float(n.strip()))

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(weights)):
        d = data1[i][j] - data2[i][j]
        s += weights[j] * abs(d)
    results.append(s)

critical = 0
for i in range(len(results)):  # for all i
    if results[i] > 5:
        critical = critical + 1  # increase by 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")