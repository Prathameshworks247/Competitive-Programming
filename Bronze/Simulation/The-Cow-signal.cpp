#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    // Fast I/O (recommended for competitive programming)
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int M,N,K;

    cin >> M >> N >> K;

    vector<string>grid(M);

    for (int i = 0; i < M; i ++ ){
        cin >> grid[i];
    }

    vector<string>grid2;

    for (int i = 0; i < M; i ++){
        string row = grid[i];
        string big;
        for (char c: row){
            big += string(K, c);
        }
        grid[i] = big;
        for (int j = 0; j < K; j ++){
            grid2.push_back(grid[i]);
        }
    }

    for (int i = 0; i < M*K; i++){
        cout << grid2[i]<< endl;
    }

}
