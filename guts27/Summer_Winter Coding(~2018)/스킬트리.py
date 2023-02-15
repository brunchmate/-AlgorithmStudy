def solution(skill, skill_trees):
    answer = 0
    for skil in skill_trees:
        flag = 1
        _skill = []
        for s in skil:
            if s in skill:
                _skill.append(s)
        for idx, string in enumerate(_skill):
            if string != skill[idx]:
                flag = 0
                break
        if flag:
            answer += 1
                
    return answer