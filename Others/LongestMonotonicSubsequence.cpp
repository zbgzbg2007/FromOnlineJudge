
// Problem: Longest Monotonic Subsequence in 2D
// Description: There is a hypothesis floating around that SAT score is a strong indicator of GPA. Your task is to provide the strongest counter example for this hypothesis. Given a data set of (sat, gpa) for the final year of a group of students, devise an algorithm to construct the longest sequence of (sati, gpai) of students with progressively better SAT scores, and progressively worse gpa’s, i.e. sat1 < sat2 < … < satk and gpa1 > gpa2 > … > gpak ( Assume SAT scores and gpa’s are unique )
// Solution: binary search + dynamic programming (it could also be solved directly by DP, but the time will be O(n^2))
// Time :O(nlongn); Space: O(n)


#include<vector>
#include<algorithm>
using namespace std;

struct data {
	int sat;
	double gpa;
	data(int s, double g): sat(s), gpa(g) {}
};

bool cmp(const data &a, const data &b) {
	return a.sat>b.sat;
}

int binarysearch(vector<data> &set, data &target) {
//Find the right position for target according to its gpa
	if (target.gpa>set.back().gpa)
		return set.size();
	if (target.gpa<set.front().gpa)
		return 0;
	int l=0, r=set.size()-1;
	while (l<r) {
		int mid=l+(r-l)/2;
		if (set[mid].gpa<target.gpa && set[mid+1].gpa>target.gpa)
			return mid+1;
		if (set[mid].gpa>target.gpa)
			r=mid;
		else
			l=mid;
	}
	return l;
}

vector<data> LongestMonotonicSubsequence (vector<data> &set) {
	if (set.size()<2)
		return set;
	sort(set.begin(),set.end(),cmp);

	vector<data> dp;
	//dp[i] saves the last element of such a monotonic subsequence of length i+1
	//that the last gpa of this subsequence is minimum among all those subsequences
	vector<vector<int> >index(set.size(), vector<int>(0,0));
	//index[i] saves the indices of all the elements that has appeared in dp[i]
	
	int i, j, size=set.size();

	//compute values of dp and index in O(nlogn) time
	dp.push_back(set[0]);
	index[0].push_back(0);
	for (i=1;i<size;i++) {
		j=binarysearch(dp,set[i]);
		if (j<dp.size())
			dp[j]=set[i];
		else
			dp.push_back(set[i]);
		index[j].push_back(i);
	}

	//construct result according to dp and index in O(n) time
	vector<data> result;
	result.push_back(dp.back());
	size=dp.size(); //length of the longest monotonic subsequence
	j=index[size-1].back();cout<<index[1].size()<<endl;
	for (i=1;i<size;i++) {
	//find the (i+1)th element in result
		for (int k=index[size-i-1].size();k>=0;k--)
			if (k<j && set[k].gpa<set[j].gpa) {
				j=k;
				break;
			}
		result.push_back(set[j]);
	}
	return result;
}


int main() {
	vector<data> test;
	test.push_back(data(3,7));
	test.push_back(data(4,6));
	test.push_back(data(5,2));
	test.push_back(data(2,1));

	vector<data> res=LongestMonotonicSubsequence(test);
	for (auto entry: res)
		cout<<entry.sat<<" "<<entry.gpa<<endl;
	return 0;
}
