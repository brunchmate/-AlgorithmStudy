def change(string):
    string = string.replace('C#','c')
    string = string.replace('D#','d')
    string = string.replace('F#','f')
    string = string.replace('G#','g')
    string = string.replace('A#','a')
    return string
def solution(m, musicinfos):
    answer = []
# 문자 변환
    m = change(m)
# 안에있는거 다담고 재생시간. 제목
    for i in range(len(musicinfos)):
        start,end,name,music = musicinfos[i].split(',')
        music = change(music)
        s,e = map(int,start.split(':'))
        start = s*60 +e
        s,e = map(int,end.split(':'))
        end = s*60+e
        time = end-start
        if time < len(music):
            music = music[0:time]
        else:
            q,r = divmod(time,len(music))
            music = music*q + music[0:r]
        
        if m in music:
            answer.append((time,i,name))
# 재생시간엔먼저입력된순 반환
    if len(answer) == 0:
        return '(None)'
    answer.sort(key = lambda x :(-x[0],x[1]))  
    return answer[0][2]