def verify_number():
    print("insert number")
    num_input = int(input())

    current_number = 0

    fibonacci = [0, 1, 1, 2]

    while num_input > current_number:
        last_two_nums = fibonacci[-2:]
        current_number = last_two_nums[0] + last_two_nums[1]
        fibonacci.append(current_number)
        print(current_number)

    if current_number == num_input:
        return "the number is on the sequence"

    return "the number is not on the sequence"


string = verify_number()

print(string)
