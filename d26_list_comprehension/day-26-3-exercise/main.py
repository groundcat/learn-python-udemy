
with open("file1.txt", "r") as file_1:
    list_1 = [int(line.strip()) for line in file_1]

with open("file2.txt", "r") as file_2:
    list_2 = [int(line.strip()) for line in file_2]

result = [number for number in list_1 if number in list_2]

# Write your code above 👆

print(result)


