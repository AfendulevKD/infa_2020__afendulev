
#include <iostream>
#include <chrono>
#include <deque>

using namespace std;
int min_k,need;
void recurtion(int d_S,int k, deque<int> coins)
{
    if (need==1){
        deque<int> new_coins;
        if (d_S<0) return ;
        if ((d_S==0) and (k<min_k)) {
                min_k=k;
                need=0;
                return ;
        }
        else {
            if (coins.size()>0){
            new_coins = coins;
            new_coins.pop_back();
            recurtion(d_S-coins[coins.size()-1],k+1,coins );
            recurtion(d_S,k,new_coins );

            return ;
            }
        }
    }
}


int main()
{
    deque<int> coins;
    int N,S,c,k,pop;
    cin>> S>>N;
    k=0; min_k=S*2;need=1;
    for (int i=0;i<N;i++) {
        cin>>c;
        coins.push_back(c);
    }
    for (int j=0; j<N;j++){
        for (int i=0;i<N-1;i++){
            if (coins[i]>coins[i+1]){
                pop =coins[i];
                coins[i]=coins[i+1];
                coins[i+1]=pop;
            }
        }
    }
    recurtion(S,k,coins);
    cout<<min_k;
    return 0;
}
