#include <iostream>
#include <vector>
#include <cmath>


using namespace std;

int main()
{
    int N;
    cin >> N;
    for (int i=0; i<N; i+=2){
        for (int k=0; k<i/2;k++){
            cout << ' ';
        }
        for (int j=N; j>i; j--){
            cout << '*' ;}
        cout << endl ;
        }

    return 0;
}
