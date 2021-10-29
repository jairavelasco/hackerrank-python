def mutate_string(string, position, character):
    lis=list(string)
    lis[position]=character
    return ''.join(lis)

