//	OJ: Topcoder SRM 361
//	Solution: Trie

#include<iostream>
#include<vector>
#include<string>

using namespace std;

class SearchBox {
private: 
struct TrieNode {
	bool word;
	vector<TrieNode *> children;
	char val;
	TrieNode() {
		word=false;
		children=vector<TrieNode *>(256,NULL);
		val=0;
	}
	TrieNode(char c): val(c) {
		word=false;
		children=vector<TrieNode *>(256,NULL);
	}
	~TrieNode() {
		for (int i=0;i<256;i++)
			delete children[i];
	}
};

TrieNode root;

	void addword(string s) {
		TrieNode *p=&root;
		for (int i=0;i<s.size();i++) {
			if (p->children[s[i]]==NULL)
				p->children[s[i]]=new TrieNode(s[i]);
			p=p->children[s[i]];
		}
		p->word=true;
	}		
public:
	int find(string text, string search, string wholeWord, int start) {
		int i=0,j;
		while (start<text.size()) {
			if (text[start]==search[0]&&(wholeWord[0]=='N'||(start==0||text[start-1]==' '))) {
				for (j=1;j<search.size();j++)
					if (text[j+start]!=search[j])
							break;
				if (j==search.size()&&(wholeWord[0]=='N'||(start+j==text.size()||text[start+j]==' ')))
					return start;


			}
			start++;
		}
		return -1;
	}

};

int main(){
	return 0;
}
