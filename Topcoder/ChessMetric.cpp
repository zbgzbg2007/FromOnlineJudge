//	OJ: Topcoder (TCCC '03 Round 4 Div I Easy)
//	Solution: DP



#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class ChessMetric {
private:
int c[16]={-2,-2,-1,-1,-1,-1,-1,0,0,1,1,1,1,1,2,2};
int r[16]={1,-1,-2,-1,0,1,2,1,-1,-2,-1,0,1,2,1,-1};

public:
long long howMany(int size, vector<int> start, vector<int> end, int numMoves) {
	vector<vector<long long> >dp(size,vector<long long> (size,0));
	dp[start[0]][start[1]]=1;
	for (int i=0;i<numMoves;i++) {
		vector<vector<long long> >ndp(size,vector<long long> (size,0));
		for (int x=0;x<size;x++)
			for (int y=0;y<size;y++) 
				for (int z=0;z<16;z++)
					if (x+r[z]>=0&&x+r[z]<size&&y+c[z]>=0&&y+c[z]<size)
						ndp[x+r[z]][y+c[z]]+=dp[x][y];
		dp=ndp;
	}
	return dp[end[0]][end[1]];
}

};
