//	Classic KMP algorithm

#include<iostream>
#include<vector>

using namespace std;

class KMP{
public:
	int KMPCompare(char *a, char *b) {
	//find b in a
	//return the first complete start position, or -1 if not compared
		if(a[0]==0)
			return -1;
		if(b[0]==0)
			return 0;
		int length2;
		for(length2=0;b[length2];length2++) ;
		//	vector<int> next1(length2,0);
		//next1[i] store the longest common suffix and prefix of b[1...i-1]
		vector<int> next(length2,0);
		//optimized next1, promise b[i] and b[next2[i]] are different
	
		int i=0,j=0;
		while(b[j]&&a[i]) {
			if(a[i]==b[j])
				i++,j++;
			else {
				if(next[j]==-1)
					j=0,i++;
				else
					j=next2[j];
			}
		}
		if (b[j]==0)
			return i-j;
		return -1;
	}
	
	void findposition(char *b, vector<int> &w) {
        //Compute the positoin array for b
	 	w[0]=-1;
        	int j=0;//suffix
        	int k=-1;//prefix
        	while (b[j]) {
            		if (k==-1||b[k]==b[j]) {
                		k++,j++;
                		if (b[j]==0)
                    			break;
                		if (b[j]==b[k])
                    			w[j]=w[k];
                		else
                    			w[j]=k;
            		}
            		else
               			k=w[k];
        	}
    	}
};


int main()
{
	class KMP ss;
	char *a="aaa",*b="aaa";
	cout<<ss.KMPCompare(a,b)<<endl;
	return 0;
}
