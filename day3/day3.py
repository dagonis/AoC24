import re

def main():
    puzzle_input = [_.strip() for _ in open("input.txt").read().split("\n") if _]
    mul_re = re.compile(r"mul\(\d{1,3}, ?\d{1,3}\)")
    # part 1
    answer = 0
    for line in puzzle_input:
        results = mul_re.findall(line)
        for res in results:
            a, b = res.lstrip("mul(").rstrip(")").split(",")
            answer += int(a) * int(b)
    print(f"Part 1: {answer}")
    # part 2
    answer = 0
    single_line = "do()"
    for line in puzzle_input:
        single_line += line
    for section in single_line.split("don't()"):
        try:
            section = section.split("do()", maxsplit=1)[1]
            results = mul_re.findall(section)
            for res in results:
                a, b = res.lstrip("mul(").rstrip(")").split(",")
                answer += int(a) * int(b)
        except:
            pass
    print(f"Part 2: {answer}")

if __name__ == "__main__":
    main()
