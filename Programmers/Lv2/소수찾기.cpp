#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n) {
    if (n < 2) 
        return false;
    
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0)
            return false;
    }
    
    return true;
}

int solution(string numbers) {
    int answer = 0;
    
    vector<int> nums;
    string s = numbers;
    int s_len = s.size();
    
    //1.가능한 숫자 문자열 리스트 nums
    sort(s.begin(), s.end());
    do {
        for (int i = 1; i <= s_len; i++) {
            string temp = s.substr(0, i);
            nums.push_back(stoi(temp));
        }
    } while (next_permutation(s.begin(), s.end()));
    
    //2.nums 중복 없애기
    sort(nums.begin(),nums.end());
    nums.erase(unique(nums.begin(),nums.end()), nums.end());
    
    //3.소수판별(에라토스테네스의 체)
    for (auto& a : nums) {
        if (is_prime(a)) {
            answer++;
        }
    }
    
    return answer;
}
