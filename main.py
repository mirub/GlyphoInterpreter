# Copyright 2021 Miruna-Elena Banu <mirunaelena.banu@gmail.com>

import sys
import operations as op
import functions as foo

exec_error = 0

instruc_len = 4
instruc_map = {
    '0000' : 'n',    # NOP
    '0001' : 'i',    # Input
    '0010' : '>',    # Rot
    '0011' : '\\',   # Swap
    '0012' : '1',    # Push
    '0100' : '<',    # RRot
    '0101' : 'd',    # Dup
    '0102' : '+',    # Add
    '0110' : '[',    # L-brace
    '0111' : 'o',    # Output
    '0112' : '*',    # Multiply
    '0120' : 'e',    # Execute
    '0121' : '-',    # Negate
    '0122' : '!',    # Pop
    '0123' : ']',    # R-brace 
}

if __name__ == '__main__':
    argums = sys.argv
    
    instrucs = []
    input_file = open(argums[1])
    
    if (len(argums) == 3):
        my_base = int(argums[2])
    else:
        my_base = 10
    
    # Read and decode instructions and create braces map
    instrucs = foo.read_file(input_file, instruc_len)
    decoded = list(map(foo.decode_instruc, instrucs))
    braces = foo.check_braces(decoded)
    
    # Initialize empty stack
    stk = []

    # Don't skip any instruction initially
    jmp = 0
    i = 0

    while i < len(decoded):
        # If the instruction is to be executed
        if jmp == 0:
            ret = foo.execute_instr(decoded[i], stk, my_base, i)
            stk = ret[0]
            new_jmp = ret[1]
            # If the current loop should be skipped jump after
            # its corresponding right brace
            if new_jmp == 1 and jmp == 0:
                i = braces[i] + 1
            else:
                # If the current instruction is a right brace not
                # to be skippes, jump to the left brace
                if (decoded[i] == "0123"):
                    i = foo.get_lbrace(i, braces)
                else:
                    i += 1
        else:
            i += 1
