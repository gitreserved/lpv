#include <iostream>
#include <vector>
#include <omp.h>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void parallelBubbleSort(vector<int>& arr) {
    int n = arr.size();
    int num_threads = omp_get_num_threads();
    int chunk_size = n / num_threads;
    
    #pragma omp parallel shared(arr) num_threads(num_threads)
    {
        #pragma omp for schedule(static, chunk_size)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }
}

int main() {
    vector<int> arr = {5, 3, 8, 6, 7, 2, 1, 4};
    
    // Sequential bubble sort
    bubbleSort(arr);
    cout << "Sequential bubble sort: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    // Parallel bubble sort
    arr = {5, 3, 8, 6, 7, 2, 1, 4};
    omp_set_num_threads(4);
    parallelBubbleSort(arr);
    cout << "Parallel bubble sort: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;
    
    system("pause"); // Pause the program and keep the window open
    
    return 0;
}
