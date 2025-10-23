#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    string a;
    
    cin >> n;
    cin >> a;
    
    unordered_map<int, int> dic;
    
    for (char c : a) {
        if (isdigit(c)) {
            int digit = c - '0';
            dic[digit]++;
        }
    }
    
    int count6 = (dic.find(6) != dic.end()) ? dic[6] : 0;
    int count1 = (dic.find(1) != dic.end()) ? dic[1] : 0;
    
    if (count6 > count1) {
        cout << count1 << endl;
    } else {
        cout << count6 - 1 << endl;
    }
    
    return 0;
}