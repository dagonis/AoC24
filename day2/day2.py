def verify_reading(reading: list) -> bool:
    # Lets make sure that the reading is in ascending or descending order
    test_ascending = reading.copy()
    test_descending = reading.copy()
    test_ascending.sort()
    test_descending.sort(reverse=True)
    if reading == test_ascending or reading == test_descending:
        correct_order = True
    else:
        return False
    # Let's make sure that we have the proper levels (-/+ 3) and that we don't have any duplicates
    if correct_order:
        for i in range(len(reading)):
            if not i == len(reading) - 1:
                if (not reading[i+1] - 3 <= reading[i] <= reading[i+1] + 3) or (reading[i] == reading[i+1]):
                    return False
    return True

def main():
    puzzle_input = [_ for _ in open("input.txt").read().split("\n") if _]
    readings = []
    for line in puzzle_input:
        reading = [int(_) for _ in line.split(" ")]
        readings.append(reading)
    # part 1
    valid_readings = 0
    for reading in readings:
        if verify_reading(reading):
            valid_readings += 1 
    print(f"Part 1: {valid_readings}")
    # part 2
    valid_readings = 0
    for reading in readings:
        if verify_reading(reading):
            valid_readings += 1
        else:
            for i in range(len(reading)):
                working_reading = reading.copy()
                working_reading.pop(i)
                if verify_reading(working_reading):
                    valid_readings += 1
                    break
    print(f"Part 2: {valid_readings}")


if __name__ == "__main__":
    main()  