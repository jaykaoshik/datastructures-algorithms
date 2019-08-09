#include <iostream>
#include <map>
#include <vector>
#include <fstream>
using namespace std;



bool isvalid(vector<char> array, int size){
    map<char,int> mymap;

    // first insert function version (single parameter):
    mymap.insert ( pair<char,int>('1',1) );
    mymap.insert ( std::pair<char,int>('2',2) );
    mymap.insert ( std::pair<char,int>('3',3) );
    mymap.insert ( std::pair<char,int>('4',4) );
    mymap.insert ( std::pair<char,int>('5',5) );
    mymap.insert ( std::pair<char,int>('6',6) );
    mymap.insert ( std::pair<char,int>('7',7) );
    mymap.insert ( std::pair<char,int>('8',8) );
    mymap.insert ( std::pair<char,int>('9',9) );
    mymap.insert ( std::pair<char,int>('0',10) );
    mymap.insert ( std::pair<char,int>('A',11) );
    mymap.insert ( std::pair<char,int>('B',12) );
    int new_arr[size];
    for(int i=0;i<size;i++){
        new_arr[i]=0;
    }

    for(int i=0;i<size;i++){
        if(array[i]!='.'){
            int index=mymap[array[i]];
            index-=1;
            if(new_arr[index]==0){
                new_arr[index]=1;
            }
            else{
                return false;
            }
        }

    }
    return true;
}
bool isValidSudoku(vector< vector<char> >& board) {
    int rows=board.size();
    int cols=board[0].size();
    for(int i=0;i<rows;i++){
        if(!isvalid(board[i],cols)){
            return false;
        }
    }
    for(int i=0;i<cols;i++){
        vector<char> my_vector;
        for(int j=0;j<rows;j++){
            my_vector.push_back(board[j][i]);
        }
        if(!isvalid(my_vector,rows)){
            return false;
        }

    }

    for(int i=0;i<rows;i+=3){
        for(int j=0;j<cols;j+=4){
            vector<char> my_vector_2;
            my_vector_2.push_back(board[i][j]);
            my_vector_2.push_back(board[i+1][j]);
            my_vector_2.push_back(board[i+2][j]);
            my_vector_2.push_back(board[i][j+1]);
            my_vector_2.push_back(board[i+1][j+1]);
            my_vector_2.push_back(board[i+2][j+1]);
            my_vector_2.push_back(board[i][j+2]);
            my_vector_2.push_back(board[i+1][j+2]);
            my_vector_2.push_back(board[i+2][j+2]);
            my_vector_2.push_back(board[i][j+3]);
            my_vector_2.push_back(board[i+1][j+3]);
            my_vector_2.push_back(board[i+2][j+3]);


            if(!isvalid(my_vector_2,rows)){
                return false;
            }
        }
    }

    return true;
}

bool recursive_sol(vector< vector<char> >& board){
    char candidates[] = {'1','2','3','4','5','6','7','8','9','0','A','B'};
    int rows=board.size();
    int cols=board[0].size();
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            if(board[i][j]=='.'){
                for(int k=0;k<12;k++){
                    board[i][j]=candidates[k];
                    if(isValidSudoku(board)){
                        if(recursive_sol(board)==true){
                            return true;
                        }
                        else{
                            board[i][j]='.';
                        }
                    }
                    else{
                        board[i][j]='.';
                    }

                }
                return false;
            }
        }
    }
    return true;
}

void solveSudoku(vector< vector<char> >& board) {
    bool val = recursive_sol(board);
    cout<<val<<endl;
    for(int i=0; i<12;i++){
      for(int j=0;j<12;j++){
        cout<<board[i][j]<<" ";
      }
      cout<<endl;
    }

}

int main(){
  map<char,int> mymap;
  std::ifstream is("hatke.txt");
  string line;

  // first insert function version (single parameter):
  vector< vector <char> > board;

  while (getline(is, line)) {
      cout<<line<<endl;
      vector <char> myvec;
      for(int j=0;j<12;j++){
        myvec.push_back(line[j]);
      }
      board.push_back(myvec);
  }
  solveSudoku(board);

}
