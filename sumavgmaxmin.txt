#include <iostream>
#include <omp.h>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    int n = 1000;
    int arr[n];
    // Generate random array
    srand(time(NULL));
    for(int i=0;i<n;i++) {
        arr[i] = rand() % 100;
    }
    // Min Operation
    int min_val = arr[0];
    #pragma omp parallel for reduction(min:min_val)
    for(int i=1;i<n;i++) {
        if(arr[i] < min_val) {
            min_val = arr[i];
        }
    }
    cout << "Minimum Value: " << min_val << endl;
    // Max Operation
    int max_val = arr[0];
    #pragma omp parallel for reduction(max:max_val)
    for(int i=1;i<n;i++) {
        if(arr[i] > max_val) {
            max_val = arr[i];
        }
    }
    cout << "Maximum Value: " << max_val << endl;
    // Sum Operation
    int sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for(int i=0;i<n;i++) {
        sum += arr[i];
    }
    cout << "Sum: " << sum << endl;
    // Average Operation
    double average = 0.0;
    #pragma omp parallel for reduction(+:sum)
    for(int i=0;i<n;i++) {
        sum += arr[i];
    }
    average = (double)sum / n;
    cout << "Average: " << average << endl;
    return 0;
}

/*minimum: 0
max: 99
sum: 48883
avg: 97.766*/