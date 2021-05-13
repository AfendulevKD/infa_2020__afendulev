#include <iostream>
#include <chrono>
#include <deque>

using namespace std;
int max_k;
void recurtion(int d_S,int k, deque<int> weight, deque<int> cost)
{

        deque<int> new_weight;
        if (d_S<0) return ;
        if (k>max_k) {
                max_k=k;

        }

        if (weight.size()>0){
                new_weight = weight;
                new_weight.pop_back();
                recurtion(d_S-weight[weight.size()-1],k+cost[weight.size()-1],weight,cost );
                recurtion(d_S,k,new_weight,cost );

            return ;
            }

    }



int main()
{
    deque<int> cost;
    deque<int> weight;
    int N,W,c,k,pop;
    cin>> W>>N;
    k=0; max_k=0;
    for (int i=0;i<N;i++) {
        cin>>c;
        weight.push_back(c);
    }
    for (int i=0;i<N;i++) {
        cin>>c;
        cost.push_back(c);
    }

    for (int j=0; j<N;j++){
        for (int i=0;i<N-1;i++){
            if (cost[i]/weight[i]>cost[i+1]/weight[i+1]){
                pop =weight[i];
                weight[i]=weight[i+1];
                weight[i+1]=pop;

                pop =cost[i];
                cost[i]=cost[i+1];
                cost[i+1]=pop;
            }
        }
    }
    recurtion(W,k,weight,cost);
    cout<<max_k;
    return 0;
}
