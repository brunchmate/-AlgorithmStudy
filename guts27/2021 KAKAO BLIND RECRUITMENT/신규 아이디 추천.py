import re
def solution(new_id):
    new_id = new_id.lower()
    p = re.compile('[\w]')
    arr = ['.','-','_']
    rest=""
    for s in new_id:
        if p.match(s) or s in arr:
            rest += s
    new_id = rest
    rest = ''
    num = 0
    for s in new_id:
        if s =='.':
            num+=1
        else:
            rest += s
            num = 0
        if num == 1:
            rest += s
    new_id = rest
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id)<=2:
        new_id += new_id[-1]
    return new_id 
