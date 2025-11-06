from wordle_functions import find_possible_word

print("Testing find_possible_word...")

assert find_possible_word("salet","bbbbb","steak")==False
print("Test 1 complete")
assert find_possible_word("pleas", "ggggg", "pleak")==False
print("Test 2 complete")
assert find_possible_word("salet", "bybbb","appar")==True
print("Test 3 complete")
assert find_possible_word("salet","bbbbb", "churn")==True
print("Test 4 complete")
assert find_possible_word("salet", "ggggg", "salet")==True
print("Test 5 complete")
assert find_possible_word("salet", "yyyyy","alets")==True
print("Test 6 complete")
assert find_possible_word("salet", "ybyby","lotos")==True
print("Test 7 complete")
assert find_possible_word("ssspo", "yygbb","awsss")==True
print("Test 8 complete")
assert find_possible_word("ssspo", "yygbb","awsss")==True
print("Test 9 complete")
assert find_possible_word("salet", "yyyyy","aleks")==False
print("Test 9 complete")
assert find_possible_word("sally", "bbgbb", "pplpp")==True
print("Test 10 complete")
assert find_possible_word("salet", "bbbbb", "salet")==False
print("Test 11 complete")


print("Tests for find_possible_word are complete")