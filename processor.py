# original code (legacy function) for project
'''
def process_values(blackbox_output):
    sets = ('1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm')  # Keyboard-based sets
    approved = []
    rejected = []

    if blackbox_output[0] in sets[0]:
        approved.append(blackbox_output[0])
    else:
        rejected.append(blackbox_output[0])

    if blackbox_output[1] in sets[1]:
        approved.append(blackbox_output[1])
    else:
        rejected.append(blackbox_output[1])

    if blackbox_output[2] in sets[2]:
        approved.append(blackbox_output[2])
    else:
        rejected.append(blackbox_output[2])

    if blackbox_output[3] in sets[3]:
        approved.append(blackbox_output[3])
    else:
        rejected.append(blackbox_output[3])

    return ''.join(approved), ''.join(rejected)
'''
# refactoring
'''
def process_single_value(value, valid_set, approved_list, rejected_list):
    if value in valid_set:
        approved_list.append(value)
    else:
        rejected_list.append(value)

def process_values(blackbox_output):
    sets = ('1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm')
    approved = []
    rejected = []

    for i in range(4):
        process_single_value(blackbox_output[i], sets[i], approved, rejected)

    return ''.join(approved), ''.join(rejected)
'''

def process_values(blackbox_output):
    sets = ('1234567890', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm')  # Keyboard-based sets
    approved, rejected = [], []

    for value, valid_set in zip(blackbox_output, sets):
        if value in valid_set:
            approved.append(value)
        else:
            rejected.append(value)
            
    return ''.join(approved), ''.join(rejected)

print(process_values("4qfm"))
print(process_values("w2fm"))