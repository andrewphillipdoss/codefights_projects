#A cryptarithm is a mathematical puzzle for which the
#goal is to find the correspondence between letters and digits,
#such that the given arithmetic equation consisting of
#letters holds true when the letters are converted to digits.

#You have an array of strings crypt, the cryptarithm,
#and an an array containing the mapping of letters
#and digits, solution. The array crypt will contain
#three non-empty strings that follow the structure:
#[word1, word2, word3], which should be interpreted
#as the word1 + word2 = word3 cryptarithm.

#If crypt, when it is decoded by replacing
#all of the letters in the cryptarithm with
#digits using the mapping in solution,
#becomes a valid arithmetic equation containing
#no numbers with leading zeroes, the answer is true.
#If it does not become a valid arithmetic solution, the answer is false.

def isCryptSolution(crypt, solution):
    s = dict(solution)
    numb = []
    eq = []
    decode = []
    for j in crypt:
        for i in j:
            decode.append(s[i])
            code=''.join(decode)
        if code[0] == '0' and len(code) > 1:
            return False
        eq.append(int(code))
        decode = []

    if eq[0] - eq[1] == eq[2] or eq[0] + eq[1] == eq[2]:
        return True
    else:
        return False
