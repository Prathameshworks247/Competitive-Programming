def decode_borze(borze_code):
    i = 0
    result = []
    while i < len(borze_code):
        if borze_code[i] == '.':
            result.append('0')
            i += 1
        elif borze_code[i] == '-':
            if borze_code[i + 1] == '.':
                result.append('1')
                i += 2
            elif borze_code[i + 1] == '-':
                result.append('2')
                i += 2
    return ''.join(result)

# Example usage
borze_code = input()  # Input Borze code string
decoded_number = decode_borze(borze_code)
print(decoded_number)