#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int top_down(int arr[][10], int S[], int m, int n){


	if(n<0 || m<0){
		return 0;
	}

	else if(n==0){
		if(arr[m][n]==-1){
			arr[m][n]=1;
		}
		return 1;
	}

	if(m==0 && n>0){
		if(arr[m][n]==-1){
			arr[m][n]=0;
		}
		return 0;	

	}

	if(arr[m][n]==-1){	
		arr[m][n]=top_down(arr,S,m-1,n)+top_down(arr,S,m,n-S[m]);
	}
	
	return arr[m][n];


}


int main(){
	int arr[3][10];
	memset(arr, -1 , sizeof(arr[0][0])*3*10);
	int S[3]={1,2,3};

	top_down(arr,S,3,10);
	cout<<arr[0][10];

	return 0;
}