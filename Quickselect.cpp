//	Problem: find the kth min element of the array

#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int midof5(vector<int> &num, int start) {
	//find the middle of an array with at most five elements
	int mid;
	if (start+5<=num.size()) {
		sort(num.begin()+start,num.begin()+start+5);
		mid=num[start+2];
	}
	else {
		sort(num.begin()+start,num.end());
		mid=num[start+(num.size()-start)/2];
	}
	return mid;
}

int findk(vector<int> &num, int k) {
	//find the kth min element
	int size=num.size();
	if (size<=5) {
		sort(num.begin(),num.end());
		return num[k];
	}
	vector<int> nnum;
	int i,j;
	//find a good pivot
	for (i=0;i<size;i+=5) {
		nnum.push_back(midof5(num,i));
	}
	int mid=findk(nnum,nnum.size()/2);

	//recursively find the target by binary search	
	for (i=0,j=size-1;i<j;i++) 
		if (num[i]>=mid)
			swap(num[i--],num[j--]);
	if (i==k-1)
		return mid;
	if (i<k-1) {
		vector<int> nums(num.begin()+i,num.end());
		return findk(nums,k-1-i);
	}
	vector<int> nums(num.begin(),num.begin()+i);
	return findk(nums,k);
}

int main() {
	vector<int> test(11,0);
	for (int i=0;i<test.size();i++)
		cin>>test[i];
	cout<<findk(test,test.size()/2)<<endl;
	sort(test.begin(),test.end());
	for (int i=0;i<test.size();i++)
		cout<<test[i]<<" ";
	cout<<endl;
	return 0;
}

