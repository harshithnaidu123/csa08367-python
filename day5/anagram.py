def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram('typhoon', 'opython'))  
print(is_anagram('Alice', 'Bob')) 