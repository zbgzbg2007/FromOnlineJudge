//	OJ: Topcoder SRM 232
//	Solution: Trie

#include<iostream>
#include<string>
#include<vector>


using namespace std;

class WordFind {
public:
	vector<string> findWords(vector<string> grid, vector<string> wordList){
		vector<string> res(wordList.size(),"");
		for (int i=0;i<wordList.size();i++)
			addword(wordList[i],i);
		for (int i=0;i<grid.size();i++) 
			for (int j=0;j<grid[0].size();j++)
				search(grid,i,j,res,root.children[grid[i][j]-'A'],i,j);
		return res;
	}
private:

	struct TrieNode{
		char val;
		vector<TrieNode *> children;
		vector<int> num;
		TrieNode() {
			val=0;
			children=vector<TrieNode *>(26,NULL);
		}
		TrieNode(char c): val(c) {
			children=vector<TrieNode *>(26,NULL);
		}
		~TrieNode() {
			for (int i=0;i<26;i++)
				delete children[i];
		}
	};
	TrieNode root;
	void search(vector<string> &grid, int x, int y, vector<string> &res, TrieNode *cur, int startx, int starty) {
		if (cur==NULL)
			return;
		if (cur->num.empty()!=true) {
			for (int i=0;i<cur->num.size();i++)
				if (res[cur->num[i]].empty())
					res[cur->num[i]]=to_string(startx)+" "+to_string(starty);
		}
		if (x+1<grid.size())
			search(grid,x+1,y,res,cur->children[grid[x+1][y]-'A'],startx,starty);
		if (y+1<grid[0].size())
			search(grid,x,y+1,res,cur->children[grid[x][y+1]-'A'],startx,starty);
		if (x+1<grid.size()&&y+1<grid[0].size())
			search(grid,x+1,y+1,res,cur->children[grid[x+1][y+1]-'A'],startx,starty);
	}
	void addword(string s, int x) {
		TrieNode *p=&root;
		for (int i=0;i<s.size();i++) {
			if (p->children[s[i]-'A']==NULL)
				p->children[s[i]-'A']=new TrieNode(s[i]);
			p=p->children[s[i]-'A'];
		}
		p->num.push_back(x);
	}
};

int main() {
	vector<string> grid,lists;
	grid.push_back("TEST");
	grid.push_back("GOAT");
	grid.push_back("BOAT");
	lists.push_back("GOAT");
	lists.push_back("BOAT"); 
	lists.push_back("TEST");
	string g[]={"SXXX", "XQXM", "XXLA", "XXXR"},l[]={"SQL", "RAM"};
	vector<string> gg(g,g+sizeof(g)/sizeof(g[0]));
	vector<string> ll(l,l+sizeof(l)/sizeof(l[0]));
	class WordFind ss;
	vector<string> res=ss.findWords(gg,ll);
	for (auto x: res)
		cout<<x<<endl;
	return 0;
}
