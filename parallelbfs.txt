#include <iostream>
#include <queue>
#include <omp.h>

using namespace std;

const int MAX = 1000;
int graph[MAX][MAX], visited[MAX];

void bfs(int start, int n) {
    queue<int> q;
    visited[start] = 1;
    q.push(start);
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        #pragma omp parallel for shared(graph, visited, q) schedule(dynamic)
        for (int i = 0; i < n; i++) {
            if (graph[curr][i] && !visited[i]) {
                visited[i] = 1;
                q.push(i);
            }
        }
    }
}

int main() {
    int n, start;
    cout << "Enter number of vertices: ";
    cin >> n;
    cout << "Enter adjacency matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }
    cout << "Enter starting vertex: ";
    cin >> start;
    #pragma omp parallel num_threads(4)
    {
        bfs(start, n);
    }
    cout << "BFS traversal: ";
    for (int i = 0; i < n; i++) {
        if (visited[i])
            cout << i << " ";
    }
    cout << endl;
    return 0;
}

// 5
/*0 1 0 1 0
1 0 1 0 0
0 1 0 0 0
1 0 0 0 1
0 0 0 1 0*/
// 2