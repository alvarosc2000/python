def calculate_love_score(name1, name2):
    compare_word1 = "true"
    compare_word2 = "love"
    compare_word_len = len(compare_word1)
    compare_word_len2 = len(compare_word2)
    name_combined = ""
    cont1 = 0
    cont2 = 0
    name_combined = name1 + " " + name2
    name_combined_len  = len(name_combined)
    name_combined = name_combined.lower()

    print(name_combined)

    for i in range(0,compare_word_len):
        for f in range(0,name_combined_len):
            if compare_word1[i].lower() == name_combined[f]:
                cont1 += 1
            else:
                f += 1
        print(f"{compare_word1[i]} occurs {cont1} times")
        
    for i in range(0,compare_word_len2):
        for f in range(0,name_combined_len):
            if compare_word2[i].lower() == name_combined[f].lower():
                cont2 += 1
            else:
                f += 1
        print(f"{compare_word2[i]} occurs {cont2} times")

    print(f"{cont1}{cont2}")


calculate_love_score("brad pitt", "jennifer aniston")




'''
def calculate_love_score(name1, name2):
    compare_word1 = "true"
    compare_word2 = "love"
    
    name_combined = (name1 + name2).lower()

    cont1 = 0
    for letter in compare_word1:
        count = name_combined.count(letter)
        cont1 += count

    cont2 = 0
    for letter in compare_word2:
        count = name_combined.count(letter)
        cont2 += count

    print(f"{cont1}{cont2}")

calculate_love_score("brad pitt", "jennifer aniston")

'''