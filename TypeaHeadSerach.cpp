#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<unordered_map>
#include<sstream>
#include<fstream>
#include<unordered_set>
#include<set>
using namespace std;

enum DataType {
	user,
	topic,
	question,
	board
};
struct Info {
//record the whole information about some id
	string id;
	DataType type;
	double score;
	int time;	//added time of this information
	vector<string> data;
	Info () {
		id = "";
		type = user;
		score = 0;
		time = 0;
		data = vector<string>(0);
	}
	Info (string i, DataType t, double s, int m, vector<string> d) {
		id = i;
		type = t;
		score = s;
		time = m;
		data = d;
	}

};

struct Node {
//trie node containing the id's that contain the substring from root to this node in data
	vector<Node *> children;
	unordered_set<string> idset;
	//we keep idset for every node such that search for id can be faster
	Node () {
		children = vector<Node *>(257, (Node *)NULL);
	}
	~Node() {
		for (int i = 0; i < 257; i++) 
			delete children[i];
	}
};


unordered_map<string, Info> id_Info;	//records for all information
class SearchBar{
private: 
	Node * root;
	int timer;	//clock for adding
	DataType hashType(string const &x) {
		if (x == "user") 
			return user;
		if (x == "topic") 
			return topic;
		if (x == "question")
			return question;
		return board;
	}
	static const bool less(const Info &a, const Info &b) {
		if (a.score - b.score != 0)
			return a.score-b.score < 0;
		return a.time < b.time;
	}
	static const bool nodecmp(const Node * a, const Node * b) {
		return a->idset.size() < b->idset.size();
	}

public: 
	SearchBar() {
		root = new Node();
		timer = 0;
	}
	void add(vector<string> &input) {
	// input does not contain commands
	// data contains no capital letters
	// add id into every node of the letter of word
		vector<string> curdata;
		for (int i = 3; i < input.size(); i++) {
			Node * cur = root;
			curdata.push_back(input[i]);
			for (int j = 0; j < input[i].size(); j++) {
				if ((cur->children)[input[i][j]] == NULL)
					(cur->children)[input[i][j]] = new Node();
				cur = (cur->children)[input[i][j]];
				if ((cur->idset).find(input[1]) == (cur->idset).end()) 
					(cur->idset).insert(input[1]);
			}
		}
		id_Info[input[1]] = Info(input[1], hashType(input[0]), stod(input[2]), timer++, curdata);
	}
	
	void del(string xid) {
	// delete both in trie and id_Info
		vector<string> gone = id_Info[xid].data;
		for (int i = 0; i < gone.size(); i++) {
			Node * cur = root;
			for (int j = 0; j < gone[i].size(); j++) {
				Node * next = (cur->children)[gone[i][j]];
				if (next == NULL || (next->idset).erase(xid) == 0)
					break;
				if ((next->idset).empty()) {
					delete next;
					(cur->children)[gone[i][j]] = NULL;
					break;
				}
				cur = next;
			}
		}
		id_Info.erase(xid);
	}


	
	void query(vector<string> &x, int m, bool w, unordered_map<int, double> &a, unordered_map<string, double> &b) {
	// output results contains all the id whose data contains x
	// if no such Info, res is empty 
	// res contains at most m results
	// w shows if it is weighted
		vector<string> res(0);
		Node * cur = root;
		int i, j;
		vector<Node *> myqueue;
		for (i = x.size() - 1; i >= 0; i--) {
		// find all the token leaves for x
			cur = root;
			for (j = 0; j < x[i].size(); j++) 
				if ((cur->children)[x[i][j]]) 
					cur = (cur->children)[x[i][j]];
				else {
					cout << "" << endl;
					return;
				}
			myqueue.push_back(cur);
		}
		sort(myqueue.begin(), myqueue.end(), nodecmp);
		// sort the leaves such that we always start with the token with minimum ids
		vector<Info> temp(0);
		for (auto &s : myqueue[0]->idset) {
		// add those legal ids into temp
			for (i = 1; i < myqueue.size(); i++)
				if (myqueue[i]->idset.find(s) == myqueue[i]->idset.end())
					break;
			if (i == myqueue.size())
				temp.push_back(id_Info[s]);
		}
		if (w) {
			for (auto &item : temp) {
				switch (item.type) {
					case user:
						j = 0;
						break;
					case topic:
						j = 1;
						break;
					case question:
						j = 2;
						break;
					case board:
						j = 3;
				}
				if (a.find(j) != a.end())
					item.score *= a[j];
				if (b.find(item.id) != b.end())
					item.score *= b[item.id];
			}
		}

		make_heap(temp.begin(), temp.end(), less);
		// use a heap to find the results with high scores
		while (res.size() < m && temp.size() > 0) {
			pop_heap(temp.begin(), temp.end(), less);
			string id = temp.back().id;
			temp.pop_back();
			res.push_back(id);
		}
		if (res.empty()) 
			cout << "" << endl;
		else {
			for ( i = 0; i < res.size() - 1; i++)
				cout << res[i] << " ";
			cout << res[i] <<endl;
		}
	}


};

void insensitive(string &x) {
// turn capital letters into lower cases
	for (int j = 0; j < x.size(); j++) 
		if (x[j] <= 'Z' && x[j] >= 'A')
			x[j] = x[j] - 'A' + 'a';	
}

void simplify(vector<string> &x) {
// remove duplicate tokens and prefix tokens
	sort (x.begin(), x.end());
	int k;
	vector<string>::iterator it1, it2;
	for (it1 = x.begin(); it1 != x.end(); it1++) {
		for (it2 = it1 + 1; it2 != x.end(); it2++) {
			for (k = 0; k < (*it1).size(); k++)
				if ((*it1)[k] != (*it2)[k])
					break;
			if (k == (*it1).size()) {
				it1 = x.erase(it1);
				it1--;
				break;
			}
		}
	}
	
}

int main() {
	SearchBar mybar;
	string line;
	int n, x, i;
	cin >> n;
	getline(cin,line);
	while (n--) {
		getline(cin, line);
		istringstream iss(line);
		string cmd;
		string next;
		iss >> cmd;
		if (cmd == "ADD") {
			vector<string> input;
			while (iss >> next) {
				insensitive(next);
				input.push_back(next);
			}
			mybar.add(input);
		}
		else if (cmd == "DEL") {
			iss >> next;
			mybar.del(next);
		}
		else if (cmd == "QUERY") {
			iss >> next;
			x = stoi(next);
			vector<string> input;
			while (iss >> next) {
				insensitive(next);
				input.push_back(next);
			}
			simplify(input);
			unordered_map<int, double> a;
			unordered_map<string, double> b;
			if (x > 0)
				mybar.query(input, x, false, a, b);
			else
				cout << "" << endl;
		}
		else {
			iss >> next;
			x = stoi(next);
			iss >> next;
			int y = stoi(next);
			unordered_map<int, double> a;
			unordered_map<string, double> b;
			while (y--) {
			// transform boots
				iss >> next;
				for (i = 0; i < next.size(); i++) 
					if (next[i] == ':')
						break;
				string x = next.substr(0, i);
				string w = next.substr(i+1, next.size()-i-1);
				if (x == "user") 
					i = 0;
				else if (x == "topic")
					i = 1;
				else if (x == "question")
					i = 2;
				else if (x == "board")
					i = 3;
				else
					i = 4;
				double s = stod(w);
				if (i == 4)
					b[x] = s;
				else
					a[i] = s;
			}
			vector<string> input;
			while (iss >> next) {
				insensitive(next);
				input.push_back(next);
			}
			simplify(input);
			if (x > 0)
				mybar.query(input, x, true, a, b);
			else
				cout << "" << endl;
		}
	}
	return 0;
}
