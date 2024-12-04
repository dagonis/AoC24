def get_neighbors(x, y, puzzle_input):
    possible_neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y-1), (x+1,y-1), (x-1,y+1)]
    neighbor_to_remove = set()
    for neighbor in possible_neighbors:
        if neighbor[0] < 0:
            neighbor_to_remove.add(neighbor)
        if neighbor[0] > len(puzzle_input) - 1:
            neighbor_to_remove.add(neighbor)
        if neighbor[1] < 0:
            neighbor_to_remove.add(neighbor)
        if neighbor[1] > len(puzzle_input[0]) - 1:
            neighbor_to_remove.add(neighbor)
    for neighbor in neighbor_to_remove:
        possible_neighbors.remove(neighbor)
    return possible_neighbors

def check_if_colinear(p1, p2, p3, p4):
    cross_product1 = get_cross_product(p1, p2, p3)
    cross_product2 = get_cross_product(p1, p2, p4)
    return cross_product1 == 0 and cross_product2 == 0

def get_cross_product(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def main():
    puzzle_input = [list(_) for _ in [_ for _ in open("input.txt").read().split("\n") if _]]
    # part 1
    x, y = 0, 0
    possible_christmases = []
    for line in puzzle_input:
        y = 0
        for char in line:
            if char == "X":
                first_step_candidates = get_neighbors(x, y, puzzle_input)
                for candidate in first_step_candidates:
                    if puzzle_input[candidate[0]][candidate[1]] == "M":
                        second_step_candidates = get_neighbors(candidate[0], candidate[1], puzzle_input)
                        for candidate2 in second_step_candidates:
                            if puzzle_input[candidate2[0]][candidate2[1]] == "A":
                                third_step_candidates = get_neighbors(candidate2[0], candidate2[1], puzzle_input)
                                for candidate3 in third_step_candidates:
                                    if puzzle_input[candidate3[0]][candidate3[1]] == "S":
                                        possible_christmases.append([[x,y], [candidate[0], candidate[1]], [candidate2[0], candidate2[1]], [candidate3[0], candidate3[1]]]) 
            y += 1
        x += 1
    christmas_count = 0
    for possible_christmas in possible_christmases:
        if check_if_colinear(possible_christmas[0], possible_christmas[1], possible_christmas[2], possible_christmas[3]):
            christmas_count += 1
    print(f"Part 1: {christmas_count}")
    # part 2
    x, y = 0, 0
    possible_xmases = {}
    valid_xmases = 0
    for line in puzzle_input:
        y = 0
        for char in line:
            if char == "A":
                a_neighbors = get_neighbors(x, y, puzzle_input)
                possible_xmases[(x,y)] = a_neighbors
            y += 1
        x += 1
    for k,v in possible_xmases.items():
        if len(v) < 8:
            pass
        elif len(v) == 8:
            upper_left_char = puzzle_input[k[0]-1][k[1]-1]
            upper_right_char = puzzle_input[k[0]+1][k[1]-1]
            lower_left_char = puzzle_input[k[0]-1][k[1]+1]
            lower_right_char = puzzle_input[k[0]+1][k[1]+1]
            if upper_left_char == "M" and upper_right_char == "M" and lower_left_char == "S" and lower_right_char == "S":
                valid_xmases += 1
            elif upper_left_char == "M" and lower_left_char == "M" and upper_right_char == "S" and lower_right_char == "S":
                valid_xmases += 1
            elif upper_left_char == "S" and lower_left_char == "S" and upper_right_char == "M" and lower_right_char == "M":
                valid_xmases += 1
            elif upper_left_char == "S" and upper_right_char == "S" and lower_left_char == "M" and lower_right_char == "M":
                valid_xmases += 1
    print(f"Part 2: {valid_xmases}")
            
    
if __name__ == "__main__":
    main()  