#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int arr[21][21];
int visited[21][21]={0,};
int N,M;
int getGold(int ci, int cj, int k) {
    int cnt = 0;
    // 마름모 대신 격자 전체를 훑는 게 오히려 빠름 (K가 클 수 있으므로)
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            if (abs(r - ci) + abs(c - cj) <= k)
                cnt += arr[r][c];
    return cnt;
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)      // M이 아니라 N
            cin >> arr[i][j];

    int best = 0;                        // -1이 아니라 0

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {    // M이 아니라 N
            for (int k = 0; k <= 2 * N; k++) {   // can() 제거, 범위 확대
                int cnt = getGold(i, j, k);
                int cost = k * k + (k + 1) * (k + 1);
                if (cnt * M >= cost && cnt > best)
                    best = cnt;
            }
        }
    }

    cout << best << "\n";
    return 0;
}