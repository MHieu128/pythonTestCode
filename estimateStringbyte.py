import sys
test_string = "你" * 2000
print(len(test_string))
sum_byte = sys.getsizeof(test_string)
sum_2 = len(test_string.encode("utf8"))
print(sum_byte)
print(sum_2)