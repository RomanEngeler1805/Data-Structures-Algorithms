#include <iostream>
#include <vector>
#include <assert.h>

template <typename T, int size>
class CircularBuffer{
	T buf[size];
	int in; int out;
	
	public:
		CircularBuffer():in{0}, out{0}{};
		bool empty(){
			return in == out;
		}
		bool full(){
			return (in+ 1)% size == out;
		}
		void put(T x);
		T get();
};

template <typename T, int size>
void CircularBuffer<T,size>::put(T x){
	assert(!full());
	buf [in] = x;
	in = (in+ 1)% size;
}

template <typename T, int size>
T CircularBuffer<T,size>::get(){
	assert(!empty());
	T x = buf[out];
	out = (out+ 1)% size;
	return x;
}

int main(){
	CircularBuffer<int,5> buf;
	for (int i = 0; i<4; i++){
		buf.put(i);
	}

	for (int i = 0; i<4; i++){
		std::cout<<buf.get()<<std::endl;
	}
	return 0;
}
