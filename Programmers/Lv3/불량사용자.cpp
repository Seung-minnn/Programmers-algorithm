/*
------------------------------------------------------------------
DFS로 코드 작성했음
  - check 가 중복되는 경우를 처음에 생각못해서 오래걸렸던 문제..ㅠㅠㅠ
------------------------------------------------------------------
*/

#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<bool> check(10, false);
vector<vector<bool>> answer_list;
int cnt = 0;

bool is_right(string a, string b) {
    if (a.size() != b.size()) return false;
    
    for (int i = 0 ; i < a.size(); i++) {
        if (a[i] != b[i]) {
            if (b[i] == '*') continue;
            
            return false;
        }
    } 
    
    return true;
}

void dfs(int index, int level, vector<string> &user_id, vector<string> &banned_id) {
    if (level >= banned_id.size()) {
        bool is_equal; //check 중복되는지 확인하는 변수
        for (auto &a : answer_list) {
            is_equal = true;
            for (int i = 0; i < check.size(); i++) {
                if (a[i] == check[i]) continue;
                is_equal = false;
            }
            if (is_equal) return;
        }
        
        answer_list.push_back(check);
        cnt++;
        return;
    }
    
    for (int i = 0; i < user_id.size(); i++) {
        if (check[i] || !is_right(user_id[i], banned_id[level])) continue;
        
        check[i] = true;
        dfs(i, level + 1, user_id, banned_id);
        check[i] = false;
    }
    
    return;
}

int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;
    
    dfs(0, 0, user_id, banned_id);
    
    answer = cnt;
    return answer;
}
