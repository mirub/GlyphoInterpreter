# Copyright 2021 Miruna-Elena Banu <mirunaelena.banu@gmail.com>

import functions as foo

# The NOP operation
def NOP_op(stk):
    return stk

# The INPUT operation
def input_op(stk, my_base):
    is_valid = 1
    cpy = stk[:]
    num = input()
    if foo.check_base(num, my_base) == False:
        is_valid = 0
    else:
        num = int(num, my_base)
        cpy.insert(0, num)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The ROT operation
def rot_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) == 0:
        is_valid = 0
    else:
        top = cpy[0]
        cpy.pop(0)
        cpy.append(top)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The SWAP operation
def swap_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) < 2:
        is_valid = 0
    else:
        el1 = cpy[0]
        el2 = cpy[1]
        cpy.pop(0)
        cpy.pop(0)
        cpy.insert(0, el1)
        cpy.insert(0, el2)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The PUSH operation
def push_op(stk):
    cpy = stk[:]
    cpy.insert(0, 1)
    return cpy

# The RROT operation
def rrot_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) == 0:
        is_valid = 0
    else:
        top = cpy[len(stk) - 1]
        cpy.pop(len(stk) - 1)
        cpy.insert(0, top)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The DUP operation
def dup_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) == 0:
        is_valid = 0
    else:
        cpy.insert(0, cpy[0])
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The ADD operation
def add_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) < 2:
        is_valid = 0
    else:
        el1 = cpy[0]
        el2 = cpy[1]
        cpy.pop(0)
        cpy.pop(0)
        cpy.insert(0, el1 + el2)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The OUTPUT operation
def output_op(stk, my_base):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) == 0:
        is_valid = 0
    else:
        print(foo.deci_2_base(cpy[0], my_base))
        cpy.pop(0)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The MULTIPLY operation
def multiply_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) < 2:
        is_valid = 0
    else:
        el1 = cpy[0]
        el2 = cpy[1]
        cpy.pop(0)
        cpy.pop(0)
        cpy.insert(0, el1 * el2)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The L-BRACE operation
def lbrace_op(stk):
    is_valid = 1
    cpy = stk[:]
    jmp = 0
    if len(cpy) == 0:
        is_valid = 0
    else:
        if cpy[0] == 0:
            jmp = 1
    ret = []
    ret.append(cpy)
    ret.append(jmp)
    ret.append(is_valid)
    return ret

# The R-BRACE operation
def rbrace_op(stk):
    return stk

# The EXECUTE operation
def execute_op(stk):
    is_valid = 1
    cpy = stk[:]
    instr = []
    if len(cpy) < 4:
        is_valid = 0
    else:
        li = cpy[0 : 4]
        for i in range(4):
            cpy.pop(0)
        instr = foo.decode_instruc(li)
    fin = []
    fin.append(instr)
    fin.append(cpy)
    fin.append(is_valid)
    return fin

# The NEGATE operation
def negate_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) < 1:
        is_valid = 0
    else:
        cpy[0] = -cpy[0]
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret

# The POP operation
def pop_op(stk):
    is_valid = 1
    cpy = stk[:]
    if len(cpy) == 0:
        is_valid = 0
    else:
        cpy.pop(0)
    ret = []
    ret.append(cpy)
    ret.append(is_valid)
    return ret
