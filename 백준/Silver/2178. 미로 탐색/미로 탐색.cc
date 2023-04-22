#include <bits/stdc++.h>
using namespace std; 
int dy[] = {0, -1, 0, 1}; 
int dx[] = {1, 0, -1, 0};
int n, m, visited[104][104], y, x; 
char a[104][104]; 
string s; 
int main() { 
    cin >> n >> m;
    for (int i = 0; i<n;i++){
        cin >> s; 
        for(int j = 0; j < m; j++){
            a[i][j] = s[j];
        } 
    }
    queue<pair<int, int>> q;
    visited[0][0] = 1;
    q.push({0, 0}); 
    while (q.size()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny<0 || nx<0 || ny>n-1 || nx>m-1) continue;
            if (a[ny][nx] == '0') continue; 
            if (visited[ny][nx]) continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});  
        }
    }
    cout << visited[n-1][m-1];
} 