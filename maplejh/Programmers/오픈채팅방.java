//https://school.programmers.co.kr/learn/courses/30/lessons/42888

import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String, String> cmd = new HashMap<>();
        cmd.put("Enter", "%s님이 들어왔습니다.");
        cmd.put("Leave", "%s님이 나갔습니다.");
        HashMap<String, String> uidMap = new HashMap<>();
        ArrayList<String> log = new ArrayList<String>();
        for (String r : record) {
            String[] list = r.split(" ");
            switch (list[0]) {
                case "Enter":
                    log.add(list[1] + " " + list[0]);
                    uidMap.put(list[1], list[2]);
                    break;
                case "Leave":
                    log.add(list[1] + " " + list[0]);
                    break;
                case "Change":
                    uidMap.put(list[1], list[2]);
                    break;
            }
        }
        String[] answer = new String[log.size()];
        int i = 0;
        for (String s : log) {
            String[] list = s.split(" ");
            answer[i] = String.format(cmd.get(list[1]), uidMap.get(list[0]));
            i++;
        }
        return answer;
    }
}