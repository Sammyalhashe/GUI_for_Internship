#include <vector>
using namespace std;

vector<int> merge(vector<int> arr, vector<int> left, vector<int> right) {
     //fill origonal list!
     //// I just cpoied this here -> don't really know what erase() and begin() do
    for(int f = 0; f < arr.size(); f++){
            if(left.size() < 1){
                arr[f] = right[0];
                right.erase(right.begin());
                continue;
            }else if (right.size() < 1){
                arr[f] = left[0];
                left.erase(left.begin());
                continue;
            }
        if(left[0] >= right[0]){
            arr[f] = left[0];
            left.erase(left.begin());
        }else{
            arr[f] = right[0];
            right.erase(right.begin());
        }
    }

    return arr;

}

vector<int> mergeSort(vector<int> arr, int l, int r){
    //end of recursion case
    if(arr.size() <2){
        return arr;
    }
    //make two arrays of each half.
    int split = (r-l)/2;
    vector <int> left(split);
    vector <int> right(arr.size()- split);

    //take sorted left and sorted right and merge them by comparing the elements
    left = mergeSort(arr,l,split);
    right = mergeSort(right,split+1,r);

    return merge(arr,left, right);
}