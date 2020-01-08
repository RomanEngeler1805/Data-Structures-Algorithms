#include <bits/stdc++.h>
#define MAX 1000

class Stack {
	int head;

	public:
		int a[MAX];

		Stack() {head = -1;}
		bool push(int x);
		int pop();
		int top();
		bool isEmpty();
};

bool Stack::push(int x){
	if (head >= (MAX-1)){
		std::cout<<"Stack Overflow";
		return false;
	} else {
		a[++head] = x;
		std::cout<<x<<" pushed into stack\n";
		return true;
	}
}

int Stack::pop(){
	if (head < 0){
		std::cout<<"Stack Underflow";
		return 0;
	} else {
		int x = a[head--];
		return x;
	}
}

int Stack::top(){
	if (head < 0){
		std::cout<<"Stack is Empty";
		return 0;
	} else {
		int x = a[head];
		return x;
	}
}

bool Stack::isEmpty(){
	return (head<0);
}

int main(){
	class Stack s;
	s.push(10);
	s.push(20);
	s.push(30);
	std::cout<<s.pop()<<" Popped from stack\n";
	return 0;
}
