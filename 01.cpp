#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 1001//物品最大数 
#define MAXM 1001//重量最大数 
int dp[MAXN][MAXM];//dp数组 
int w[MAXN],v[MAXN];//重量和价值数组 
int n;//物品数量
int full;//最大可装重量 
void solve();//解题函数 
int main(){
	cout << "请输入背包的最大容量：" << endl;
	cin>>full;//输入重量
	cout << "请输入物品数量：" << endl;  
	cin>>n;//输入数量
	cout << "请输入物品重量：" << endl;  
	for(int i=1;i<=n;i++){
		cin>>w[i];//输入重量 
	}
	cout << "请输入物品价值：" << endl; 
	for(int i=1;i<=n;i++){
		cin>>v[i];//输入价值 
	}
	solve(); 
	return 0;
}
void solve(){
	for(int i=0;i<=n;i++){
		for(int j=0;j<=full;j++){
			if(i==0 || j==0) dp[i][j]=0;//边界dp，结果为0 
			else{
				if(j<w[i]) dp[i][j]=dp[i-1][j];//装不下 
				else dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);//装得下，max比较装或不装哪个更大 
			}
		}
	}
	cout << "物品价值最大为：" << endl ;
	cout<<dp[n][full]<<endl;//输出结果 
}

