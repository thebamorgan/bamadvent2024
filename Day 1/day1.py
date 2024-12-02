#Part 1
with open("Day 1\day1Input.txt","r") as file:
    list1 = []
    list2 = []
    for line in file:
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

sortedList1 = sorted(list1)
sortedList2 = sorted(list2)

distance = 0

for x in range(len(sortedList1)):
    distance += abs(sortedList1[x] - sortedList2[x])

print(distance)

#Part2

def countScore(list1, list2):
    sum = 0
    for x in list1:
        count = 0
        count += list2.count(x)
        sum += (x * count)
    return sum

#Example lists for testing
# list1 = [3,4,2,1,3,3]
# list2 = [4,3,5,3,9,3]

x = countScore(sortedList1, sortedList2)
print(x)