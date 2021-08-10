def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1
s = input("Enter the string:\n")
b = reverse_join_reversed_iter(s)
print(s, b)