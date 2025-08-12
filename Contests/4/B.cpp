#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n,i;
        cin>>n>>i;
        i--;
        string s;
        cin >> s; 

        int left_w  =0;
        int right_w = 0;
        for(int j = i; j < n; j++)
        {
            if(s[j] == '#')

            {
                right_w = j;
                break;
            }
        }
        for(int j = i; j >= 0; j--)
        {
            if(s[j] == '#')
            {
                left_w = j;
                break;
            }
        }
        int left = left_w+1;
        int right = n - right_w;
        
        if(left>right)
        {
            right = n-i+1;
        }
        else
        {
            left = i+1;
        }
        cout<<min(left,right)+1<<endl;




    }
}