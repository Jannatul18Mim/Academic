#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
using namespace std;


int next_id = 1;

mutex mtx;


void admitStudent(int thread_num) {
    
    mtx.lock();

    int id = next_id;
    next_id++;

    cout << "Thread " << thread_num 
         << " assigned Student ID: " << id << endl;

    
    mtx.unlock();
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