#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct Point {
    int x, y;
};

// 计算向量点积
int dot(const Point &a, const Point &b, const Point &c) {
    int abx = b.x - a.x;
    int aby = b.y - a.y;
    int acx = c.x - a.x;
    int acy = c.y - a.y;
    return abx * acx + aby * acy;
}

// 计算向量叉积
int cross(const Point &a, const Point &b, const Point &c) {
    int abx = b.x - a.x;
    int aby = b.y - a.y;
    int acx = c.x - a.x;
    int acy = c.y - a.y;
    return abx * acy - aby * acx;
}

// 判断三角形是否为钝角三角形
bool isObtuseTriangle(const Point &a, const Point &b, const Point &c) {
    // 检查三点是否共线
    if (cross(a, b, c) == 0) {
        return false;
    }
    
    // 计算三个角对应的点积
    int dot1 = dot(a, b, c); // 角A
    int dot2 = dot(b, a, c); // 角B  
    int dot3 = dot(c, a, b); // 角C
    
    // 如果任意一个角是钝角，则返回true
    return dot1 < 0 || dot2 < 0 || dot3 < 0;
}

int main() {
    int n;
    cin >> n;
    
    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }
    
    int count = 0;
    // 枚举所有三角形
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (isObtuseTriangle(points[i], points[j], points[k])) {
                    count++;
                }
            }
        }
    }
    
    cout << count << endl;
    
    return 0;
}