def word_count(text):
    words = text.split()
    return f"{len(words)} words found in the document"

def character_count(text):
    lower_text = text.lower()
    character_dict= {}
    
    for character in lower_text:
        
        if character not in character_dict:
            character_dict[character] = 1  
        else:
            character_dict [character] += 1
            
    return character_dict