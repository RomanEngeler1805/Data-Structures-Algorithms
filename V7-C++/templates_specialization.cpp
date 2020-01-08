#include <iostream>
#include <vector>

template <typename T>
class Pair{
	T left; T right;
	public:
		Pair(T l, T r):left{l}, right{r} {}
		T min(){ return left < right? left:right; }
		std::ostream& print (std::ostream& os) const{
			return os<<"("<<left<<","<<right<<")";
		}
};

template <>
class Pair<bool>{
	short both;	
	public:
		Pair(bool l, bool r):both{(l?1:0)+ (r?2:0)} {};
		std::ostream& print (std::ostream& os) const{
			return os << "("<<both%2 <<","<<both/2<<")";
		}
};

template <typename T>
std::ostream& operator<< (std::ostream& os, const Pair<T>& pair){
	return pair.print(os);
}

int main(){
	Pair<int> i(10,20);
	std::cout<<i<<std::endl;
	Pair<bool> b(true, false);
	std::cout<<b<<std::endl;
	return 0;
}
