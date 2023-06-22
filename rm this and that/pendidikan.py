import random

total_iterations = 52744
sma_count = int(total_iterations * 0.60)
s1_count = int(total_iterations * 0.25)
smp_count = int(total_iterations * 0.05)
d3_count = total_iterations - sma_count - s1_count - smp_count

strings = ["SMA"] * sma_count + ["S1"] * s1_count + ["SMP"] * smp_count + ["D3"] * d3_count
random.shuffle(strings)

file_name = "cekulah.txt"
with open(file_name, 'w') as file:
    for string in strings:
        file.write(string + "\n")

print("Output saved to", file_name)
