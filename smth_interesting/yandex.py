a_b = str(input(f'enter A B'))
summ = float(a_b.split()[0]) + float(a_b.split()[1])
summ_isint = lambda n: int(n) == float(n)
result = int(summ) if summ_isint(summ) else summ
print(result)

# a_b = str(input(f'enter A B'))
# summ = int(a_b.split()[0]) + int(a_b.split()[1])
# print(summ)

# a,b=map(int, input().split())

# a, b = input("Enter A B").split()
# try:
#     summ = int(a) + int(b)
#     print(summ)
# except ValueError as e:
#     print('Enter not int num')

# with open('input.txt', 'r') as input:
#     numbers = input.read()
#     a, b = map(int, numbers.split())
#     summ = int(a) + int(b)
#     with open('output.txt', 'w') as output:
#         output.write(str(summ))