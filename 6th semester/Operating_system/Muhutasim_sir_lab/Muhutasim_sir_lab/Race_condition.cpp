#include <iostream>
#include <thread>
#include <vector>
#include <chrono>
using namespace std;


int next_id = 1;


void admitStudent(int thread_num) {
    
    int id = next_id;


    this_thread::sleep_for(chrono::milliseconds(10));

   
    next_id = next_id + 1;

    
    cout << "Thread " << thread_num << " assigned Student ID: " << id << endl;
}

int main() {
    vector<thread> threads;

    
    for (int i = 1; i <= 10; i++) {
        threads.push_back(thread(admitStudent, i));
    }


    for (auto &t : threads) {
        t.join();
    }

    return 0;
}