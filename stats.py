def number_of_words(book):
    wordlist = book.split()
    word_count = 0
    for word in wordlist:
        word_count += 1
    return word_count

def words_dictionary(content):
    characters = []
    dictionary = {}
    report_list = []
    for character in content:
        lower_case = character.lower()
        if lower_case == "\ufeff":
            continue
        elif lower_case not in dictionary:
            dictionary[lower_case] = 1
        else:
            dictionary[lower_case] += 1
    for key in dictionary:
        report_list.append(f"{key}: {dictionary[key]}")
        report_list.sort(reverse=True, sorted=True)
    print(report_list)

        
        
    return dictionary

        


