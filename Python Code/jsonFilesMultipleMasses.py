import json

points = []
xp = []
yp = []
x = []
y = []

with open('Jsons/InBreast/JsonFilesMultiple/Mass1_20586908.json') as json_file:
    data = json.load(json_file)

for i in data["ROIPoints"]:
    points.append(i)

for j in points:
    s = j[1:len(j) - 1]
    index = s.find(",")
    pointx = s[0:index]
    xp.append(pointx)
    pointy = s[index + 1:len(s)]
    yp.append(pointy)

for k in xp:
    x.append(float(k))

for l in yp:
    y.append(float(l))

print(x)
print('\n')
print(y)