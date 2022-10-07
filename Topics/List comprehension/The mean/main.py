sequence = input()

sequence_list = [int(s) for s in sequence]

sequence_sum = 0
for s in sequence_list:
    sequence_sum += s

print(sequence_sum / len(sequence_list))
