import text_utils  

text = "You never get a second chance to make a first impression"

letter_to_count = 'e'

letter_count = text_utils.count_letter(text, letter_to_count)

print(f"The number of letter '{letter_to_count}': {letter_count}")