//	OJ: Topcoder (TCCC '04 Round 4 Div I Easy)
//	Solution: DP


#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class BadNeighbors {
public:
int maxDonations(vector<int> donations) {
	if (donations.size()==1)
		return donations[0];
	vector<int> done0=donations;
	vector<int> undo0(donations.size(),0);
	done0[0]=0;
	vector<int> done1=donations;
	vector<int> undo1(donations.size(),0);
	int i;
	for (i=1;i<donations.size()-1;i++) {
		done0[i]+=undo0[i-1];
		undo0[i]+=max(undo0[i-1],done0[i-1]);
		done1[i]+=undo1[i-1];
		undo1[i]+=max(undo1[i-1],done1[i-1]);
	}
	done0[i]+=undo0[i-1];
	undo0[i]=max(done0[i-1],max(undo0[i-1],max(done1[i-1],undo1[i-1])));
	return max(done0[i],undo0[i]);
}

};

int main() {
	return 0;
}
