import sys
import numpy as np

char_2_int = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
    ' ': 26}

int_2_char = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z',
    26: ' '}

## MAIN ##
def main():
    data = read_data()
    first_ltrs = compute_first_ltr_probs(data)
    transitions = compute_transition_probs(data)
    print(generate_name(first_ltrs, transitions))

# Return array of names from input (input should only contain names with english letters)
def read_data():
    names = sys.stdin.readlines()
    return [name.lower().rstrip() + "  " for name in names]

def compute_first_ltr_probs(data):
    first_ltrs = np.zeros(27)

    # count occurences of letters as first letter
    for name in data:
        first_ltr_int = char_2_int[name[0]]
        first_ltrs[first_ltr_int] += 1.0
    
    # normalize letter counts to probabilites that sum to 1
    first_ltr_sum = float(len(data))
    for i, count in enumerate(first_ltrs):
        first_ltrs[i] = count / first_ltr_sum
    
    return first_ltrs

def compute_transition_probs(data):
    # transtions[0][1] is prob of next ltr being 'b' ('b' has idx 1) if prev ltr was 'a' (idx 0)
    transitions = np.zeros((27,27))
    
    # count num of transitions between letter pairings
    for name in data:
        for i in range(1, len(name)):
            prev_ltr_int = char_2_int[name[i-1]]
            curr_ltr_int = char_2_int[name[i]]
            transitions[prev_ltr_int][curr_ltr_int] += 1.0
    
    # normalize transition counts for each row to probabilites that sum to 1 (row stochastic)
    for i, row in enumerate(transitions):
        row_sum = 0
        for elem in row:
            row_sum += elem
        for j, elem in enumerate(row):
            transitions[i][j] = elem / row_sum
            
    return transitions

def generate_name(first_ltrs, transitions):
    name = ""

    # select first letter of name
    r = np.random.rand()
    prob_sum = 0
    idx = 0
    while r > prob_sum:
        prob_sum += first_ltrs[idx]
        idx += 1
    
    first_ltr_int = idx - 1
    name = name + int_2_char[first_ltr_int].upper()

    # select rest of letters for name
    # stop when empty space is selected
    prev_ltr_int = first_ltr_int
    curr_name_pos = 1
    while name[len(name)-1] != " ":
        # select a new letter
        if curr_name_pos != 1:
            prev_ltr_int= char_2_int[name[curr_name_pos-1]]

        next_ltr_probs = transitions[prev_ltr_int]
        r = np.random.rand()
        prob_sum = 0
        idx = 0
        while r > prob_sum:
            prob_sum += next_ltr_probs[idx]
            idx += 1
    
        next_ltr_int = idx - 1
        name = name + int_2_char[next_ltr_int]

        curr_name_pos += 1
    
    return name

## ENTRY ##
if __name__ == "__main__":
    main()