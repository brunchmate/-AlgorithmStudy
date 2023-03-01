# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    def sharp(s):
        return s.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")

    def to_int(s):
        hh, mm = map(int, s.split(":"))
        return hh * 60 + mm

    answer = "(None)"
    t = 0
    m = sharp(m)
    for music in sorted(musicinfos):
        start, end, name, melody = music.split(",")
        start = to_int(start)
        end = to_int(end)
        melody = sharp(melody)
        q, r = divmod((end - start), len(melody))
        melody = melody * q + melody[:r]
        if m in melody:
            if t < end - start:
                answer = name
                t = end - start
    return answer
