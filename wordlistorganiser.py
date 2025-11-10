from wordfreq import word_frequency

organised_words_list =[]

for word in words_list:
    if len(organised_words_list) == 0:
        organised_words_list.append(word)
        continue

    inserted = False
    for i in range(len(organised_words_list)):
        if word_frequency(word, "en") > word_frequency(organised_words_list[i], "en"):
            organised_words_list.insert(i, word)
            inserted = True
            break  # Important: stop after inserting

    # If word wasn't inserted (has lowest frequency), append to end
    if not inserted:
        organised_words_list.append(word)


filtered_list=[]
for i in range(4000):
    if organised_words_list[i][4].lower()!="s":
        filtered_list.append(organised_words_list[i])
print(filtered_list)