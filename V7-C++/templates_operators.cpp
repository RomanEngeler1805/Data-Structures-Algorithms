#include <iostream>
#include <vector>

template <typename T>
class Pair{
	T left; T right;
	
	public:
		Pair(T l, T r): left{l}, right{r}{}
		T min(){return left<right? left: right;}
		std::ostream& print (std::ostream& os) const{
			return os<<"("<<left<<","<<right<<")";
		}
};

template <typename T>
std::ostream& operator<< (std::ostream& os, const Pair<T>& pair){
	return pair.print(os);
}

int main(){
	Pair<int> a(10,20);
	auto m = a.min();
	std::cout<<m<<std::endl;

	std::cout<<a;

	return 0;
}
