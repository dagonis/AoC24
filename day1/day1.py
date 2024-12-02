puzzle_input = [_ for _ in open("input.txt").read().split("\n") if _]
# part 1
left_numbers, right_numbers = [], []
for i in puzzle_input:
    left, right = i.split("  ")
    left_numbers.append(int(left))
    right_numbers.append(int(right))
left_numbers.sort(reverse=True)
right_numbers.sort(reverse=True)
differences = []
for i in range(len(puzzle_input)):
    differences.append(abs(left_numbers.pop() - right_numbers.pop()))
print(f"Part 1: {sum(differences)}")
# part 2
left_numbers, right_numbers = [], []
for i in puzzle_input:
    left, right = i.split("  ")
    left_numbers.append(int(left))
    right_numbers.append(int(right))
similarity_score = 0
for number in left_numbers:
    similarity_score += right_numbers.count(number) * number
print(f"Part 2: {similarity_score}")
