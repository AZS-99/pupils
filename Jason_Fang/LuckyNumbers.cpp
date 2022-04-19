//
// Created by Adam Saher on 2022-04-17.
//

#include <iostream>
#include <vector>
#include "LuckyNumbers.h"





//std::pair<unsigned, unsigned> luckynumber(){
//    int num;
//    std::cin >> num;
//    std::vector<unsigned> arr;
//    for(int i=0;i<=2*num;i++){
//        arr.push_back(2*i+1);
//    }
//    int luckpos=2;
//    int cursize=arr.size();
//    while(arr[luckpos]< arr.size() && arr[arr[luckpos]-1]<=num) {
//        for (int j = cursize / arr[luckpos]; j > 0; j--) {
//            arr.erase(arr.begin() + j * arr[luckpos] - 1);
//        }
//        cursize -= cursize / arr[luckpos];
//        luckpos++;
//    }
//    unsigned sm,bi;
//    for(int i=arr[arr[luckpos-1]];;i++){
//        if(arr[i]>=num){
//            sm=arr[i-1];
//        }
//        if(arr[i-1]<=num){
//            bi=arr[i];
//            break;
//        }
//    }
//    auto p = std::make_pair(sm,bi);
//    return p;
//}