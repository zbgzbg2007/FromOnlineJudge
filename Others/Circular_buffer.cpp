//	Problem: Given a size, please implement a circular buffer with the following methods: append element, remove element, print current elements. Each element will be a string.


#include<iostream>
#include<string>
#include<vector>
using namespace std;

class Circular_Buffer{
public:
	void Append(string  s){
		buffer[current]=s;
		current++;
		if (current==size)
			current=0;
		if (current==start) {
			start++;
			if (start==size)
				start=0;
		}
	}
	void Remove(){
		start++;
		if (start==size)
			start=0;
	}
	void List(){
		int i=start;
		while(i!=current) {
			cout<<buffer[i]<<endl;
			i++;
			if(i==size)
				i=0;
		}
	}
	~Circular_Buffer(){
	}
	Circular_Buffer(int n) {
		size=n+1;
		start=0;
		buffer=vector<string>(size,"");
		current=start;
	}
private:
	int size;
	int start;//the earliest buffer position, remove from it
	int current;// buffer tail, append from it
	vector<string> buffer;// buffer head, never change
};

int main()
{
	int size;
	cin>>size;	
	class Circular_Buffer buffer(size);
	string command="";
	while(command!="Q")
	{
		cin>>command;
		if(command[0]=='A'||command[0]=='R')
		{
			int count;
			cin>>count;
			string newline;
			if(command[0]=='A')
			for(int i=0;i<count;i++) {
				cin>>newline;
				buffer.Append(newline);
			}	
			else {
				while (count--)
					buffer.Remove();
			}
		}
		else
		{
			if(command[0]=='L')
				buffer.List();
		}
	}
	return 0;
}
