#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

int i = 0;
// 互斥锁
pthread_mutex_t mutex;

void* thr_fun(void* arg){
    // 加锁
    pthread_mutex_lock(&mutex);
    char* num = (char*)arg;
    for(; i < 5; i++){
        printf("%s thread, i:%d\n", num, i);
        sleep(1);
    }
    i = 0;
    // 解锁
    pthread_mutex_unlock(&mutex);
}

void main(){
    pthread_t tid1, tid2;
    // 初始化互斥锁
    pthread_mutex_init(&mutex, NULL);

    pthread_create(&tid1, NULL, thr_fun, "No1");
    pthread_create(&tid2, NULL, thr_fun, "No2");

    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    // 销毁互斥锁
    pthread_mutex_destroy(&mutex);
}