def solution(n, words):
    answer = []
    dict = {}
    people = [0]*n
    i = 0
    end = words[0][0]
    for word in words:
        first = word[0]
        if word in dict or end != first:
            return [i+1,people[i]+1]
        else:
            dict[word] = True
        end = word[-1]
        people[i] +=1
        i = (i+1)%n
            
    return [0,0]