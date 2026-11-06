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
        for (int j = 0; j < K; j ++){
            grid2.push_back(grid[i]);
        }
    }

    for (int i = 0; i < grid2.size(); i ++){
        string temp = grid2[i];
        string temp2;
        for (int i = 0; i < temp.size(); i++){
            temp2.push_back(temp[i]*K);
        }
        grid2[i] = temp2;
    }

}
