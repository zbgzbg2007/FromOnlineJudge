//	OJ: Topcoder (TCCC '04 Round 1 Div I Med)
//	Solution: DP


#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

class FloatingMedian {
private:
int segments[65536*2+2];
public:
long long sumOfMedians(int seed, int mul, int add, int N, int K) {
	vector<long long> num(K,0);
	num[0]=seed;
	insert(num[0],1,0,65535);
	int i;
	long long sum;
	for (i=1;i<K;i++) {
		num[i]=(num[i-1]*mul+add)%65536;
		insert(num[i],1,0,65535);
	}
	sum=findMedian(1,(K+1)/2,0,65535);
	for (;i<N;i++) {
		del(num[i%K],1,0,65535);
		num[i%K]=(num[(i-1)%K]*mul+add)%65536;
		insert(num[i%K],1,0,65535);
		sum+=findMedian(1,(K+1)/2,0,65535);	
	}
	return sum;
}
int findMedian(int i, int k, int start, int end) {
	if (start==end)
		return start;
	if (k<=segments[i*2])
		return findMedian(i*2,k,start,start+(end-start)/2);
	else
		return findMedian(i*2+1,k-segments[2*i],start+(end-start)/2+1,end);	
}
void insert(int x, int i, int start, int end) {
	segments[i]++;
	if (start==end) 
		return;	
	if (x<=start+(end-start)/2)
		insert(x,2*i,start,start+(end-start)/2);
	else
		insert(x,2*i+1,start+(end-start)/2+1,end);
}

void del(int x, int i, int start, int end) {
	segments[i]--;
	if (start==end) 
		return;
	if (x<=start+(end-start)/2)
		del(x,2*i,start,start+(end-start)/2);
	else
		del(x,2*i+1,start+(end-start)/2+1,end);
}

};


int main() {
	return 0;
}
