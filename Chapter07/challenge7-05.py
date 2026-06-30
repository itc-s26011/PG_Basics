list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = []

for num1 in list1:          # 外側

    for num2 in list2:      # 内側

        answer = num1 * num2

        result.append(answer)

print(result)
