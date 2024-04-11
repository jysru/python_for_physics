def even_numbers(start: int, end: int) -> list[int]:
    even_nums = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

def result(start: int, end: int) -> None:
    print(f"Even numbers between {start} and {end} are:\n{even_numbers(start, end)}")