#include <iostream>
#include <thread>
using namespace std;


int next_id = 1;


bool flag[2] = {false, false};
int turn;


void admitStudent(int i) {
    int j = 1 - i;

   
    flag[i] = true;
    turn = j;

    while (flag[j] && turn == j); // wait

    
    int id = next_id;
    next_id++;

    cout << "Thread " << i 
         << " assigned Student ID: " << id << endl;


    flag[i] = false;
}

int main() {
    thread t1(admitStudent, 0);
    thread t2(admitStudent, 1);

    t1.join();
    t2.join();

    return 0;
}