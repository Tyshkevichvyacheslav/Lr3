print("Обмен личностями")
def swap(q1, q2):
    tmp = q1[:]
    del q1[:]
    q1 += q2
    del q2[:]
    q2 += tmp


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)

print("________________")
first = [1, 2, 3]
second = [4, 5, 6, 7]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)


input("Press any key to exit")
exit(0)
