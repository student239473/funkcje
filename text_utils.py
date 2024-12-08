def count_letter(text, letter):
    """
    This function takes a string `text` and a `letter` to count how many times
    the `letter` appears in the `text`.
    """
    text = text.lower()
    letter = letter.lower()
    
    return text.count(letter)