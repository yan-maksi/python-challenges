""" 
-- Task: Analysing the frequency of letters in a string using loops and lists --
Frequency analysis is the study of the frequency of letters or combination of 
letters in encrypted text. Frequency analysis is based on the fact that in a 
particular language, certain letters, and groups of letters, appear with 
essentially the same frequency in almost all text. For example 'A' is a relatively
common letter in the English language while 'Z' is less common.
"""

def char_count(string):
    frequency = {}
    lower_string = string.lower()
    joined_string = lower_string.replace(" ", "")
    for char in set(joined_string):
        frequency[char] = joined_string.count(char)
    # sort dictionary by key
    sorted_by_key = dict(sorted(frequency.items()))
    return sorted_by_key


if __name__ == "__main__":
    string = "You can have data without information, but you cannot have information without data"
    print(char_count(string))
