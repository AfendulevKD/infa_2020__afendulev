#include <iostream>
#include <chrono>


using namespace std;

int* create_massiv(int sz)
{
    int *Array = new int[sz];

    for(int i = 0; i < sz; i++) {
       *(Array+i)=rand();
    }
    return Array;
}
void bubble(int *Array, int sz)
{
    int pop;
    for (int z=0;z<sz;z++){
        for (int i=0;i<sz-1;i++){
            if (Array[i]>Array[i+1]){
                pop=Array[i];
                Array[i]=Array[i+1];
                Array[i+1]=pop;
            }
        }
    }

}
void choice(int *Array, int sz)
{
    int pop,min_i;

    for (int z=0;z<sz-1;z++){
        for (int i=z;i<sz;i++){
            min_i=z;
            if (Array[i]<Array[min_i]){
                min_i=i;
            }
            pop=Array[z];
            Array[z]=Array[min_i];
            Array[min_i]=pop;
        }
    }

}
void inser(int *Array, int sz)
{
    int pop,min_i;

    for (int z=1;z<sz;z++){
        pop=Array[z];
        for (int i=z-1;i>=0;i--){
            Array[i+1]=Array[i];
            if (i==0) Array[i]=pop;
            if (Array[i]<pop)  Array[i+1]=pop;
        }
    }

}
void Shell_standart(int *Array, int sz)
{
    int d = sz / 2;
    int pop;

    while (d > 0)
    {
        for (int i = 0; i < sz - d; i++)
        {
            int j = i;
            while ((j >= 0) and (Array[j] > Array[j + d])){
                pop = Array[j];
                Array[j] = Array[j + d];
                Array[j + d] = pop;
                j-=1;
            }
        }
        d = d/2;
    }
}

int main() {
    int *a = new int[10];
    int max_size;
    long midle_time;
    for (int k=500;k<2000;k+=5){
        delete a;
        a=create_massiv(k);
        midle_time=0;
        for (int repeat_i=0;repeat_i<20;repeat_i++){
            auto start = chrono::high_resolution_clock::now();
            Shell_standart(a,k);
            auto end = chrono::high_resolution_clock::now();
            auto nsec = end - start;
            midle_time+=nsec.count();
        }
        midle_time=midle_time/10;
        cout << midle_time << ',' ;
    }

    return 0;
}
