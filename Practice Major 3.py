##Practice Major 3

import string

def doTrans(s, frm, to):
    if len(frm)==len(to):
        table = string.maketrans(frm, to)
        s = string.translate(s, table)
    else:
        print "error"
        
    return s

def encodeMessage(S, code):

    frm = string.ascii_lowercase
    msg = []
    
    for i in range(len(S)):
        newRow = []
        for j in range(len(S[i])):
            newRow.append(doTrans(S[i][j], frm, code))
        msg.append(newRow)

    return msg

def decodeMessage(A, code):
    
    to = string.ascii_lowercase
    msg = []

    for i in range(len(A)):
        newRow = []
        for j in range(len(A[i])):
            newRow.append(doTrans(A[i][j], code, to))
        msg.append(newRow)

    return msg
