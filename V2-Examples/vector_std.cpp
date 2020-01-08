#include <iostream>
#include <iterator>
#include <vector>

int main(){
	// Vector of lenght 10
	std::vector<int> v(10);
	// input
	for (int i = 0; i < v.size(); ++i){
		std::cin >> v[i];
	}
	// output
	for (auto it = v.begin(); it != v.end(); ++it){
		std::cout << *it << " ";
	}
}
