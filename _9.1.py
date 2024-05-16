N = int(input())

numbers = list(map(int, input().split()))

distinct_numbers = set(numbers)

print(len(distinct_numbers))
