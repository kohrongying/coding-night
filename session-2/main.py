BAD_WORDS = {
    'unreadable': 1,
    'messy': 1,
    'badcode': 2,
    'lone': 2
}

GOOD_WORDS = {
    'tdd': 1,
    'pairing': 1,
    'agile': 1,
}

def find_subsequence_count(s, seq):
    if len(seq) == 0: return 0
    original_seq = seq
    count = 0
    while len(s) > 0:
        if s[0] == seq[0]:
            seq = seq[1:]
        if len(seq) == 0:
            count += 1
            seq = original_seq
        s = s[1:]
    return count


def get_weighted_sum(s, good_words_flag=False):
    weight = 0
    for word in BAD_WORDS:
        count = find_subsequence_count(s, word)
        weight += BAD_WORDS[word] * count
    if good_words_flag:
        for word in GOOD_WORDS:
            count = find_subsequence_count(s, word)
            weight -= GOOD_WORDS[word] * count
    return weight



def get_severity(s):
    weighted_sum = get_weighted_sum(s)
    if weighted_sum == 0:
        return 'NOSEV'
    elif weighted_sum == 1:
        return 3
    elif weighted_sum == 2:
        return 2
    else:
        return 3

