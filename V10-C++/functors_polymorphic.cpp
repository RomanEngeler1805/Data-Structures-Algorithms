#include <iostream>
#include <vector>
#include <cmath>
#include <functional>

template <typename T>
auto toFunction(std::vector<T> v){
	return [v] (T x) -> double {
		int index = (int)(x+ 0.5);
		if (index < 0) index = 0;
		if (index >= v.size()) index = v.size() -1;
		return v[index];
	};
}

auto Gaussian(double mu, double sigma){
	return [mu, sigma](double x){
		const double a = (x-mu)/ sigma;
		return std::exp(-0.5* a*a);
	};
}

template <typename F, typename Kernel>
auto smooth(F f, Kernel kernel){
	return [kernel, f] (auto x){
		return 0;
	};
}

int main(){
	std::vector<double> v {1,2,5,3};
	/*
	function created from v as stepwise interpolation
	use f(x) to determine function value at x
	equivalent to std::function<double(double)> f = toFunction(v);
	*/
	auto f = toFunction(v);
	/*
	function (Gaussian) callable via k(x)	
	*/
	auto k = Gaussian(0, 0.1);

	for (auto i=0; i<v.size(); ++i)
		std::cout<<f(i)<<' ';
	return 0;
}
