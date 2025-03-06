def count_num_of_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    character_count = {}
    for word in file_contents:
        word = word.lower()
        if word in character_count:
            character_count[word] += 1
        else:
            character_count[word] = 1
    return character_count

def sort_on(dict):
    return dict['count']

def sort_characters(dict):
    dict_list = []
    for item in dict:
        dict_list.append({"char": item, "count": dict[item]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list