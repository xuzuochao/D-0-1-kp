#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 1001//��Ʒ����� 
#define MAXM 1001//��������� 
int dp[MAXN][MAXM];//dp���� 
int w[MAXN],v[MAXN];//�����ͼ�ֵ���� 
int n;//��Ʒ����
int full;//����װ���� 
void solve();//���⺯�� 
int main(){
	cout << "�����뱳�������������" << endl;
	cin>>full;//��������
	cout << "��������Ʒ������" << endl;  
	cin>>n;//��������
	cout << "��������Ʒ������" << endl;  
	for(int i=1;i<=n;i++){
		cin>>w[i];//�������� 
	}
	cout << "��������Ʒ��ֵ��" << endl; 
	for(int i=1;i<=n;i++){
		cin>>v[i];//�����ֵ 
	}
	solve(); 
	return 0;
}
void solve(){
	for(int i=0;i<=n;i++){
		for(int j=0;j<=full;j++){
			if(i==0 || j==0) dp[i][j]=0;//�߽�dp�����Ϊ0 
			else{
				if(j<w[i]) dp[i][j]=dp[i-1][j];//װ���� 
				else dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);//װ���£�max�Ƚ�װ��װ�ĸ����� 
			}
		}
	}
	cout << "��Ʒ��ֵ���Ϊ��" << endl ;
	cout<<dp[n][full]<<endl;//������ 
}

