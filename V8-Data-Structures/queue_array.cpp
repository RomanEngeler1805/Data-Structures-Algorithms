#include <iostream>
#include <vector>

#define SIZE 10

// class
class queue{
	int *arr;
	int capacity;
	int head;
	int tail;
	int count;

	public:
		queue(int size = SIZE);
		~queue();

		void enqueue(int x);
		int dequeue();
		int top();
		bool isEmpty();
		bool isFull();
};

//
queue::queue(int size){
	arr = new int[size];
	capacity = size;
	head = 0;
	tail = -1;
	count = 0;
}

//
queue::~queue(){
	delete arr;
}

// enqueue
void queue::enqueue(int x){
	if (isFull()){
		std::cout<<"Overflow\n";
		exit(EXIT_FAILURE);
	}

	tail = (tail+ 1)% capacity;
	arr[tail] = x;
	count++;
}

// dequeue
int queue::dequeue(){
	if (isEmpty()){
		std::cout<<"Underflow\n";
		exit(EXIT_FAILURE);
	}

	int element = arr[head];	

	head = (head+ 1)% capacity;
	count--;

	return element;
}

// top
int queue::top(){
	if (isEmpty()){
		std::cout<<"Underflow\n";
		exit(EXIT_FAILURE);
	}
	return arr[head];
}

// isEmpty
bool queue::isEmpty(){
	return (count == 0);
}

// isFull
bool queue::isFull(){
	return (count == capacity);
}

int main(){
	queue q(5);
	
	q.enqueue(3);
	q.enqueue(5);

	std::cout<<q.dequeue()<<std::endl;
	std::cout<<q.dequeue()<<std::endl;

	return 0;
}
