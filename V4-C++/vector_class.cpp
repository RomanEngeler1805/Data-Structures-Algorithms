#include <iostream>
#include <iterator>
#include <vector>

class Vector{
	public:
		// constructors
		Vector(): sz{0}, elem{nullptr} {};
		Vector(std::size_t s): sz{s}, elem{new double[s]} {}
		// destructor
		~Vector(){
			delete[] elem;
		}
		// getter
		double get(std::size_t i) const{
			return elem[i];
		}
		// setter
		void set(std::size_t i, double d){
			elem[i] = d;
		}
		// size property
		std::size_t size() const {
			return sz;
		}
		// copy constructor
		Vector(const Vector &v): Vector(v.sz) {
			std::copy(v.elem, v.elem+ v.sz, elem);
		}
		// assinment operator
		Vector& operator= (const Vector&v){
			Vector cpy(v);
			swap(cpy);
			return *this;
		}
		// move constructor
		Vector (Vector&& v): Vector() {
			swap(v);
		};
		// move assignment
		Vector& operator=(Vector&& v){
			swap(v);
			return *this;
		};
		// subscript operator
		double& operator[] (std::size_t pos){
			return elem[pos];
		}
		const double& operator [] (std::size_t pos) const{
			return elem[pos];
		}
		// iterator
		double* begin(){
			return elem;
		}
		double* end(){
			return elem+sz;
		}
		// const iterator
		const double* begin() const{
			return elem;
		}
		const double* end() const{
			return elem+sz;
		}

	private:
		std::size_t sz;
		double* elem;
		// helper function
		void swap(Vector& v){
			std::swap(sz, v.sz);
			std::swap(elem, v.elem);
		}
};

int main(){
	Vector v(32);
	// set
	for (std::size_t i = 0; i!=v.size(); ++i)
		v[i] = i;
	// copy
	Vector w = v;
	// set
	for (int i = 0; i< w.size(); ++i){
		w[i] = i* i;
	}
	// print
	for (int i = 0; i< w.size(); ++i){
		std::cout<< v[i] << ":" << w[i] << " ";
	}

	return 0;
}
