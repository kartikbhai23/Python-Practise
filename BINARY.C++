#include <iostream>
using namespace std;

int binary(int arr, int n, int k){
    int start = 0;
    int end = n-1;
    int mid;
    for(int i = start; i<end; i++){\
        int mid = (start + end)/2;
        if(arr[mid] == k){
            return mid;
        }else(int[mid]<k){
            start = mid +1;
            binary(start, n, k);
        }else{
            end = mid -1;
            binary(start, n , key);
        }
    }

}

int main(){
    int n = 7;
    int arr[n] = {2,4,5,6,7,8,9};
    binary(arr, n, 8);
}