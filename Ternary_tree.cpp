//	Problem: Implement a ternary tree with the following methods: insert an value, delete an value and find if some value is in the tree.

#include<iostream>
#include<queue>
#include<unordered_map>

using namespace std;

struct TreeNode{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode *mid;
	TreeNode(int x): val(x), left(NULL), right(NULL), mid(NULL){}
	~TreeNode(){
		delete this->left;
		delete this->right;
		delete this->mid;
	}
};
class TernaryTree{
public:
void insertNode(int x){
//insert a node with value x
	if(root==NULL)
	{
		root=new TreeNode(x);
		return ;
	}
	TreeNode *parent=search(x);
	if(parent->val==x)
		parent->mid=new TreeNode(x);
	if(parent->val>x)
		parent->left=new TreeNode(x);
	if(parent->val<x)
		parent->right=new TreeNode(x);
}

void deleteNode(int x){
//delete a node with value x
	if(root==NULL)
		return;
	TreeNode *p=search(x);
	if(p->val!=x)//there is no node with value x
		return ;
	if(p->val==x)
	{//there is at least one node with value x
		p=root;
		while(p&&p->val!=x&&p->left->val!=x&&p->right->val!=x)
		{//p will be the parent of the highest node with value x or root
			if(p->val<x)
				p=p->right;
			else
				p=p->left;	
		}
		TreeNode *q;//q is the highest node with value x
		if(p->val==x)
			q=p;
		else
		{
			if(p->left->val==x)
				q=p->left;
			if(p->right->val==x)
				q=p->right;
		}
		if(q->mid)	
		{//there are more than one nodes with value x, so just delete the last such node
			while(q->mid->mid)
				q=q->mid;
			delete q->mid;
			q->mid=NULL;
			return ;
		}
		else
		{//there is only one node with value x
			if(q->left==NULL&&q->right==NULL)
			{//if q is a leaf, then just delete it
				if(q==p)
				{//if q is the root
					delete q;
					root=NULL;
					return ;
				}
				if(p->left->val==x)
					p->left=NULL;	
				else
					p->right=NULL;
				delete q;
				return ;
			}
			else
			{//if q is an internal node, we need to delete it while keeping the structure of the tree
				if(q->left)
				{//if q has left child, we replace q with its left child
					TreeNode *temp=q->left;
					while(temp->right)//find the rightmost leaf in the left subtree of q
						temp=temp->right;
					temp->right=q->right;
					if(p==q)//if q is the root
						root=q->left;
					else
					{
						if(p->left->val==x)
							p->left=q->left;	
						else	
							p->right=q->left;
					}
					q->left=NULL;
					q->right=NULL;
					delete q;
				}	
				else	
				{//otherwise we replace q with its right child
					if(q==p)
						root=q->right;
					else
					{
						if(p->left->val==x)
							p->left=q->right;
						else
							p->right=q->right;
					}
					q->right=NULL;
					delete q;
				}
			}
		}
	}	
}
void printByLevel(){
//just BFS for test
	if(root==NULL)
		return ;
	TreeNode *p;
	queue<TreeNode *> myqueue;
	unordered_map <TreeNode *,int> myhash;
	myqueue.push(root);
	myhash[root]=0;
	while(myqueue.empty()!=true)
	{
		p=myqueue.front();
		myqueue.pop();
		cout<<p->val;
		if(p->left)
		{
			myqueue.push(p->left);
			myhash[p->left]=myhash[p]+1;
		}
		if(p->mid)
		{
			myqueue.push(p->mid);
			myhash[p->mid]=myhash[p]+1;
		}	
		if(p->right)
		{
			myqueue.push(p->right);
			myhash[p->right]=myhash[p]+1;
		}
		if(myqueue.empty()!=true)
		{
			TreeNode *q=myqueue.front();
			if(myhash[q]==myhash[p])
				cout<<"  ";
			else
				cout<<endl;
		}
	}
	cout<<endl;
}
TreeNode * search(int x){
/*
find if there is nodes with value x	
if such nodes exist, return the deepest one
if there is no such node, return the position it will be inserted to
*/
	TreeNode *p=root;
	while(p&&(p->val!=x||p->mid!=NULL))
	{
		if(p->val==x)
			p=p->mid;
		else
		{
			if(p->val<x)
			{
				if(p->right!=NULL)
					p=p->right;
				else
					break;
			}
			else
			{
				if(p->left!=NULL)
					p=p->left;
				else
					break;
			}
		}
	}
	return p;
}

TernaryTree(int x){
	root=new TreeNode(x);
}
TernaryTree(){
	root=NULL;
}
~TernaryTree(){
	delete root;
}
private:
TreeNode *root;

};

int main()
{
	class TernaryTree t;
/*	t.insertNode(5);
	t.deleteNode(5);
	t.printByLevel();
	t.insertNode(4);
	t.insertNode(9);
	t.insertNode(5);
	t.insertNode(7);
	t.insertNode(2);
	t.insertNode(2);
	t.insertNode(5);
	t.printByLevel();
	t.deleteNode(5);
	t.printByLevel();
	t.deleteNode(9);
	t.printByLevel();
	t.deleteNode(5);
	t.printByLevel();
	t.deleteNode(5);
	t.printByLevel();
	t.deleteNode(4);
	t.printByLevel();
*/	return 0;
}
