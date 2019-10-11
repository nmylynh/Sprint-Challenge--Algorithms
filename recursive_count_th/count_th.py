'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if not word:
        return 0
    elif word.find('th') == -1:
        return 0
    elif word.find('th') == 1 :
        return 1 + count_th(word[1:]) 
    else:
        return count_th(word[1:])
