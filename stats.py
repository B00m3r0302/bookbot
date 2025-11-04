def number_of_words(book):
    wordlist = book.split()
    word_count = 0
    for word in wordlist:
        word_count += 1
    return word_count

def words_dictionary(content):
    dictionary = {}
    
    # Get character count
    for character in content:
        lower_case = character.lower()
        if lower_case == "\ufeff":
            continue
        elif lower_case not in dictionary:
            dictionary[lower_case] = 1
        else:
            dictionary[lower_case] += 1
    
    return dictionary

def format_word_count(dictionary):
    report_list = []
    small_dictionary = {}

    # create the list with dictionary values
    for item in dictionary:
        small_dictionary = {item : dictionary[item]}
        report_list.append(small_dictionary)
    
    # helps to get the value for the key for sorting
    def get_value(value):
        return list(value.values())[0]

    # sorts the list based on the values for each key
    report_list.sort(reverse=True, key=get_value) 

    # removes symbols
    for item2 in range(0, len(report_list)):
        for key2 in report_list[item2]:
            if key2.isalpha() == True:
                print(f"{key2}: {report_list[item2][key2]}")
            else:
                continue

