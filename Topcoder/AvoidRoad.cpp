//	OJ: Topcoder (TCO '03 Semifinals 4 Div I Easy)
//	Solution: Dynaimic programming




#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<unordered_set>
using namespace std;

class AvoidRoads {
public:
long long numWays(int width, int height, vector<string> bad) {
	unordered_set<long long> myhash;
	int i;
	vector<vector<long long> >grid(height+1, vector<long long>(width+1,0));
	for (int j=0;j<bad.size();j++) {
		int a=0,b=0,c=0,d=0;
		for (i=0;bad[j][i]!=' ';i++) 
			a=a*10+bad[j][i]-'0';
		for (i++;bad[j][i]!=' ';i++) 
			b=b*10+bad[j][i]-'0';
		for (i++;bad[j][i]!=' ';i++) 
			c=c*10+bad[j][i]-'0';
		for (i++;i<bad[j].size();i++) 
			d=d*10+bad[j][i]-'0';
		if (a>c)
			swap(a,c);
		if (b>d)
			swap(b,d);
		a=a*101*101*101+b*101*101+c*101+d;
		myhash.insert(a);
	}
	grid[0][0]=1;
	for (i=0;i<=height;i++) 
		for (int j=0;j<=width;j++) {
			if (i+1<=height) {
				int x=i*101*101*101+j*101*101+(i+1)*101+j;
				if (myhash.find(x)==myhash.end())
					grid[i+1][j]+=grid[i][j];
			}
			if (j+1<=width) {
				int x=i*101*101*101+j*101*101+i*101+j+1;
				if (myhash.find(x)==myhash.end())
					grid[i][j+1]+=grid[i][j];
			}
		}
	return grid[height][width];
}

};

int main() {
	return 0;
}
