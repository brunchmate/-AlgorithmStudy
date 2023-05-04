//https://school.programmers.co.kr/learn/courses/30/lessons/42889


class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int player = stages.length;
        int[] cur = new int[N + 1];
        double[] failure = new double[N];
        for (int s : stages) {
            cur[s - 1] += 1;
        }
        int cnt = player;
        for (int i = 0; i < N; i++) {
            failure[i] = (double) cur[i] / cnt;
            cnt -= cur[i];
            answer[i] = i + 1;
        }
        int a, b, tmpi;
        double tmpd;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (failure[i] < failure[j] || (failure[i] == failure[j] && answer[i] > answer[j])) {
                    tmpd = failure[i];
                    tmpi = answer[i];
                    failure[i] = failure[j];
                    answer[i] = answer[j];
                    failure[j] = tmpd;
                    answer[j] = tmpi;
                }
            }
        }
        return answer;
    }
}
