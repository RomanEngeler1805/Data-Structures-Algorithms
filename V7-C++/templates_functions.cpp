#include <iostream>
#include <vector>

template <typename T>
T sq(T x){
	return x* x;
}

template <typename Container, typename F>
void apply(Container& c, F f){
	for(auto& x: c)
		x = f(x);
}

template <typename T>
void output(const T& t){
	for (auto x: t)
		std::cout<<x<<" ";
	std::cout<<"\n";
}

int main(){
	std::vector<int> v={1,2,3};
	apply(v,sq<int>);
	output(v);
	return 0;
}
