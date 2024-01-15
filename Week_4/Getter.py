def and_gate(input1, input2):
    if input1 and input2:
        return True
    else:
        return False

def or_gate(input1, input2):
    if input1 or input2:
        return True
    else:
        return False

def not_gate(input1):
    return not input1

def nand_gate(input1, input2):
    if not (input1 and input2):
        return True
    else:
        return False

def nor_gate(input1, input2):
    if not (input1 or input2):
        return True
    else:
        return False

def xor_gate(input1, input2):
    return (input1 or input2) and not (input1 and input2)

def xnor_gate(input1, input2):
    return not ((input1 or input2) and not (input1 and input2))