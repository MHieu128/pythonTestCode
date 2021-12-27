test_string = "tui:ten:la:hieu"
test_list = ("a")
print(type(test_list))
if [ele for ele in test_list if(ele in test_string)]:
    print("true")
else:
    print("False")

a = ["a","b","c","d","e"]
a += ["j","k","q"]
print(a)
