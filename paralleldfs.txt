#include <iostream>
#include <stack>
#include <omp.h>

using namespace std;

const int MAX = 1000;
int graph[MAX][MAX], visited[MAX];

void dfs(int start, int n) {
    stack<int> s;
    s.push(start);
    while (!s.empty()) {
        int curr = s.top();
        s.pop();
        if (!visited[curr]) {
            visited[curr] = 1;
            
            #pragma omp parallel for shared(graph, visited, s) schedule(dynamic)
            for (int i = 0; i < n; i++) {
                if (graph[curr][i] && !visited[i]) {
                    s.push(i);
                }
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
        dfs(start, n);
    }
    cout << "DFS traversal: ";
    for (int i = 0; i < n; i++) {
        if (visited[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}

// 6
// 0 1 1 0 0 0
// 1 0 0 1 0 0
// 1 0 0 0 1 0
// 0 1 0 0 1 1
// 0 0 1 1 0 0
// 0 0 0 1 0 0
// 2