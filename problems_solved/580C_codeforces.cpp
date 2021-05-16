#include <iostream>
#include <vector>

using namespace std;

bool vis[100001];
int ans = 0;
int a[100001];
vector<int> d[100001];
int n, m;

void dfs(int node, int count) {
    if(a[node] == 1) {
        count += 1;
    }
    else {
        count = 0;
    }

    if(count > m){
        return ;
    }

    vis[node] = true;
    bool leaf = true;

    for(int i = 0; i < d[node].size(); i++) {
        int curr = d[node][i];
        if(vis[curr] == false) {
            leaf = false;
            dfs(curr, count);
        }
    }
    if(leaf == true) {
        ans += 1;
    }
}

int main() {
    a[0] = 0;
    cin >> n >> m;

    for(int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    for(int i = 1; i < n; i++) {
        int x, y;
        cin >> x >> y;
        d[x].push_back(y);
        d[y].push_back(x);
    }

    for(int i = 0; i <= n; i++) {
        vis[i] = false;
    }

    // for(int i = 1; i <= n; i++) {
    //     for(int j = 0; j < d[i].size(); j++)
    //         cout << d[i].at(j) << " ";
    //     cout << "\n";
    // }

    dfs(1, 0);
    printf("%d\n", ans);

    return 0;
}