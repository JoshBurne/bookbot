def word_count(text):
    words = text.split()
    return f"Found {len(words)} total words"

def character_count(text):
    lower_text = text.lower()
    character_dict= {}
    
    for character in lower_text:
        
        if character not in character_dict:
            character_dict[character] = 1  
        else:
            character_dict [character] += 1

    return character_dict


def sorter(character_dict):

    def sort_on(dict):
        return dict["num"]
    
    dictionary_list = []
    for key in character_dict:
        if key.isalpha():
            dictionary_list.append({"char":key, "num":character_dict[key]})
    
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
        
