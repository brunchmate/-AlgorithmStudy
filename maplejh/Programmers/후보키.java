// https://school.programmers.co.kr/learn/courses/30/lessons/42890
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    ArrayList<Integer> candidates;
    String[][] r;
    int n;

    public int solution(String[][] relation) {
        r = relation;
        int answer = 0;
        candidates = new ArrayList<Integer>();
        n = relation[0].length;
        for (int i = 1; i <= Math.pow(2, n); i++) {
            if (minimality(i) && uniqueness(i)) {
                candidates.add(i);
                answer += 1;
            }
        }
        return answer;
    }

    boolean minimality(int num) {
        for (int c : candidates) {
            if ((c & num) == c) {
                return false;
            }
        }
        return true;
    }

    boolean uniqueness(int num) {
        HashSet<String> flag = new HashSet<String>();
        for (int i = 0; i < r.length; i++) {
            String tmp = "";
            for (int j = 0; j < n; j++) {
                if (((num >> j) & 1) == 1) {
                    tmp += r[i][j] + " ";
                }
            }
            flag.add(tmp);
        }
        return flag.size() == r.length ? true : false;

    }
}