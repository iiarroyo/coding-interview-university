#include <iostream>
using namespace std;
class MyVector {       // The class
    public:             // Access specifier
        int size();        // Attribute (int variable)
        int capacity();
        bool is_empty();
        int at(int);
        void push();
        void insert();
        void prepend();
        void pop();
        void m_delete();
        void remove();
        void find();
        void resize();
        int* data = new int[1];

    private:
        int size_val;
    //     int capacity;
};
int MyVector::size() {
    int i = 0;
    int size = 0;
    while(data + i != NULL )
        size++;
    return size;
}
int main(){
    MyVector vector;
    cout << vector.size();
}