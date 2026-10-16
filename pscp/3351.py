"""Rabbit language"""
sentence = input().strip()
text = sentence.upper()

if text and all(char in 'IT' for char in text):
    print(f"unknown {len(text)}")
else:
    is_invalid = False
    invalid_idx = -1
    max_a = 0
    idx = 0
    length = len(text)

    while idx < length:
        char = text[idx]

        if char == 'A':
            if not idx or text[idx - 1] not in 'RA':
                is_invalid, invalid_idx = True, idx
                break
            idx += 1

        elif char == 'R':
            if idx + 1 >= length or text[idx + 1] != 'A':
                is_invalid, invalid_idx = True, idx + 1
                break
            idx += 1
            count_a = 0
            while idx < length and text[idx] == 'A':
                count_a += 1
                idx += 1
            max_a = max(max_a, count_a)

        elif char == 'B':
            if idx + 1 >= length or text[idx + 1] not in 'IT':
                is_invalid, invalid_idx = True, idx + 1
                break
            idx += 1
            while idx < length and text[idx] in 'IT':
                idx += 1

        elif char in 'IT':
            idx += 1

        else:
            is_invalid, invalid_idx = True, idx
            break

    if is_invalid:
        print(f"no {invalid_idx}")
    else:
        print(f"yes {max_a}")
