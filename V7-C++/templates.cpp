#include <iostream>
#include <vector>

template <typename T>
void swap(T& x, T& y){
	T temp = x;
	x = y;
	y = temp;
}

int main(){
	int a = 5;
	int b = 7;
	std::cout<<a<<std::endl;
	swap(a,b);
	std::cout<<a<<std::endl;	

	return 0;
}
