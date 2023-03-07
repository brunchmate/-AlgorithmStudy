#include <string>
#include <vector>

using namespace std;

string solution(string p) {
    string w = p;
    string u = "";
    string v = "";
    string answer = "";
    int count = 0;
    int length = w.length();

    for (int i = 0; i < length; i++) {
        if (w.substr(i, 1) == "(") {
            count++;
        }
        else {
            count--;
        }
        if (count == 0) {
            u = w.substr(0, i + 1);
            v = w.substr(i+1);
            break;
        }
    }
    if (u.size() == 0) {
        return u + v;
    }
    if (u.front() == ')') {
        string tmp = "(";
        tmp += solution(v);
        tmp += ")";
        u.erase(0, 1);
        u.pop_back();
        length = u.length();
        for (int j = 0; j < length; j++) {
            if (u.substr(j, 1) == "(") {
                u.replace(j, 1, ")");
            }
            else
                u.replace(j, 1, "(");
        }
        answer = tmp + u;
    }
    else {
        if(!v.empty())
            v = solution(v);
        answer = u + v;
    }
    return answer;
}
