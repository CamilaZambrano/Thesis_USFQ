import json
import os

points = []
xp = []
yp = []
x = []
y = []

json_file = '53587014.json'
jsonPath = 'Jsons/InBreast/JsonFilesSingle/' + json_file
output_folder = 'Coordenates/InBreast'

file_name = os.path.splitext(json_file)[0]
output_file = os.path.join(output_folder, file_name + '.txt')

with open(jsonPath) as json_file:
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

with open(output_file, 'w') as file:
    file.write("Mass_1\n")
    file.write(str(x) + ";\n")
    file.write(str(y) + ";")

print(file_name + " guardado correctamente")