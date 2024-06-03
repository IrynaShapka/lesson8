# def add_one(some_list):
#     return [int(i) for i in str(int(''.join(map(str, some_list))) + 1)]
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")

# def find_unique_value(some_list):
#     result = []
#     for value in some_list:
#         if some_list.count(value) == 1:
#             result.append(value)
#     if result:
#         return result[0]
#     else:
#         return None
#
#
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

def is_palindrome(text):
    clean_text = ''.join(char for char in text if char.isalnum()).lower()
    return clean_text == clean_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('Р0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")