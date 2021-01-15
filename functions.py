# Copyright 2021 Miruna-Elena Banu <mirunaelena.banu@gmail.com>

import operations as op
import sys

# Function to read the commands
def read_file(file, len_instr):
    line = file.readline()
    if len(line) % 4 != 0:
        sys.stderr.write(f'Error:{(len(line) - 1) // 4}')
        sys.exit(-1)

    instruc = [line[i:i+len_instr] for i in range(0, len(line), len_instr)]
    return instruc

# Function to decode the instructions
def decode_instruc(coded_instruc):
    dec = []

    # Remove duplicates
    symbols = list(dict.fromkeys(coded_instruc))

    # Index elements
    sym_table = {}
    sym_table[symbols[0]] = 0
    count = 0
    for sy in symbols:
        if count != 0:
            sym_table[symbols[count]] = count
        count += 1
    
    # Decode the instruction
    for sy in coded_instruc:
        dec.append(sym_table[sy])

    # Transform the decoded instruction in a string
    dec = list(map(lambda x : str(x), dec))
    str1 = ""
    return str1.join(dec)

# Check if the braces match using a stack
def check_braces(instrucs):
    braces = {}
    left_braces = []
    count = 0
    for i in instrucs:
        # If the current instruction is '['
        # add it to the stack
        if i == "0110":
            left_braces.append(count)
        # If the current instruction is ']'
        elif i == "0123":
            # If there are no corresponding '[' left
            if len(left_braces) == 0:
                sys.stderr.write(f'Error:{count}')
                sys.exit(-1)
            else:
                # Create the braces map and remove the
                # corresponding '[' from the stack
                braces[left_braces[len(left_braces) - 1]] = count
                left_braces.pop(len(left_braces) - 1)
        count += 1
    
    # If not all the '[' close
    if len(left_braces) != 0:
        sys.stderr.write(f'Error:{len(instrucs)}')
        sys.exit(-1)
    
    return braces

# Execute an instruction
def execute_instr(e, s, my_base, index):
    if len(s) != 0:
        stk = s[:]
    else:
        stk = []
    jmp = 0

    if e == "0000":
        # NOP
        stk = op.NOP_op(stk)
    elif e == "0001":
        # INPUT
        ret = op.input_op(stk, my_base)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0010":
        # ROT
        ret = op.rot_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0011":
        # SWAP
        ret = op.swap_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0012":
        # PUSH
        stk = op.push_op(stk)
    elif e == "0100":
        ret = op.rrot_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0101":
        # DUP
        ret = op.dup_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0102":
        # ADD
        ret = op.add_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0110":
        # L-BRACE
        ret = op.lbrace_op(stk)
        stk = ret[0]
        jmp = ret[1]
        is_valid = ret[2]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0111":
        # OUTPUT
        ret = op.output_op(stk, my_base)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0112":
        # MULTIPLY
        ret = op.multiply_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0120":
        # EXECUTE
        fin = op.execute_op(stk)
        e1 = fin[0]
        stk = fin[1]
        is_valid = fin[2]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
        else:
            # Cannot execute '[' or ']'
            if e1 == "0110" or e1 == "0123":
                sys.stderr.write(f'Exception:{index}')
                sys.exit(-2)
            ret = execute_instr(e1, stk, my_base, index)
            stk = ret[0]
    elif e == "0121":
        # NEGATE
        ret = op.negate_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0122":
        # POP
        ret = op.pop_op(stk)
        stk = ret[0]
        is_valid = ret[1]
        if is_valid == 0:
            sys.stderr.write(f'Exception:{index}')
            sys.exit(-2)
    elif e == "0123":
        # R-BRACE
        stk = op.rbrace_op(stk)
    else:
        print(f'Invalid instruction inserted {e}')
        pass

    ret = []
    ret.append(stk)
    ret.append(jmp)
    return ret

# Transform from decimal to the given base
def deci_2_base(number, base):
    result = ""
    neg = 0
    # If the number is negative
    if number < 0:
        neg = 1
        number *= -1
    # Transform the number
    while number > 0:
        current_digit = int(number % base)
        # If the digit is less than 10
        if current_digit < 10:
            result += str(current_digit)
        else:
            unicode_A = ord('A')
            result += chr(unicode_A + current_digit - 10)
        number //= base
    result = result[::-1]
    # If the number is different form 0
    if len(result) != 0:
        if neg == 1:
            result = "-" + result
    else:
        result = str(0)
    return result

# Check if the input number can be the given base
def check_base(num, my_base): 
    if my_base > 36:
        return False
    if num[0] == '-':
        num = num[1:]
    for i in range(len(num)):
        if ord(num[i]) < ord('0'):
            return False
        elif my_base < 10:
            if ord(num[i]) >= ord(str(my_base)):
                return False
        elif my_base >= 10:
            if ord(num[i]) > ord('9') and ord(num[i]) < ord('A'):
                return False
            if ord(num[i]) >= (ord('A') + my_base - 10):
                return False 
    return True

# Get the corresponding l-brace
def get_lbrace(rbrace, braces):
    for key, value in braces.items():
        if rbrace == value:
            return key
 
    return "key doesn't exist"