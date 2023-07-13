input_file = open('calorie_counting_input', 'r')
inputs = input_file.readlines()

inputs = [input.strip('\n') for input in inputs]

temp = []
final_input = []

for i in range(0, len(inputs)):
    if inputs[i] != '':
        temp.append(inputs[i])
    elif inputs[i] == '':
        final_input.append(temp)
        temp = []
    if i == len(inputs) - 1:
        final_input.append(temp)

for input_list in final_input:
    for i in range(0, len(input_list)):
        input_list[i] = int(input_list[i])


output_list = []
for input_list in final_input:
    sum = 0
    for input in input_list:
        sum += input
    output_list.append(sum)

output_list.sort()

print(final_input)
print(len(final_input))
print(len(inputs))
print(output_list)
print(len(output_list))
print(output_list[-1])