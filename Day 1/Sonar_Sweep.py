#Part 1
x=0
data = []
f = open("input.txt", "r")
for line in f.readlines():
    data.append(line)
f.close()

for i in range(len(data)):
    if(int(data[i])>int(data[i-1])):
        x+=1

print("Part 1\n" 
      "------\n"
      "Datapoints: " + str(len(data)) + 
      "\nAnswer: " + str(x))

#Part 2
x=0
data, triplet = [], []
f = open("input.txt", "r")
for line in f.readlines():
    data.append(line)
f.close()

for i in range(len(data)-2):
    triplet.append(int(data[i])+int(data[i+1])+int(data[i+2]))

for i in range(len(triplet)):
    if(int(triplet[i])>int(triplet[i-1])):
        x+=1

print("\nPart 2\n"
      "------\n"
      "Datapoints: " + str(len(data)) + 
      "\nAnswer: " + str(x))