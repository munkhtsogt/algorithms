#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef vector < int > vi;
#define REP(i, a, b) for(int i = a; i < b; i++)

void print(int a[], int n){
	REP(i, 0, n){
		cout << a[i] << " ";
	}
	cout << endl;
}

void printV(vector< int > v){
	REP(i, 0, v.size()){
		cout << v[i] << " ";
	}
	cout << endl;
}

int maxSubArray1(int a[], int n){
	int best = 0;
	REP(i, 0, n){
		int sum = 0;
		REP(j, i, n){
			sum += a[j];
			best = max(best, sum);
		}
	}
	return best;
}

int maxSubArray2(int a[], int n){
	// Kadane's algorithm
	int best = 0, sum = 0;
	REP(i, 0, n){
		sum = max(a[i], sum + a[i]);
		best = max(sum, best);
	}
	return best;
}

void swap(int* a, int* b){
	int* tmp = b;
	b = a;
	a = tmp;
}

void bubbleSort(int a[], int n){
	REP(i, 0, n){
		REP(j, 0, n - 1){
			if(a[j] > a[j + 1]){
				swap(a[j], a[j+1]);
			}
		}
	}
}

vector<int> twoSum(vector<int>& numbers, int target) {
	int lo = 0, hi = numbers.size() - 1;
	while(lo < hi) {
		if(numbers[lo] + numbers[hi] == target){
			vector < int > results;
			results.push_back(lo + 1);
			results.push_back(hi + 1);
			return results;
		}
		else if(numbers[lo] + numbers[hi] > target){
			hi--;
		}
		else lo++;
	}       
}

vector<int> numberOfLines(vector<int>& widths, string S) {
	
	int sum = 0, c = 1;
	for(int i = 0; i < S.length(); i++){
		if(sum + widths[int(S[i]) - 97] <= 100){
			sum += widths[int(S[i]) - 97];
		}
		else {
			c++;
			sum = widths[int(S[i]) - 97];
		}
	}
	vector < int > r;
	r.push_back(c);
	r.push_back(sum);
    return r;
}

int uniqueMorseRepresentations(vector<string>& words) {
	string morse[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};        
	
	map<string, int> r;
	for(int i = 0; i < words.size(); i++){
		string str = "";
		for(int j = 0; j < words[i].length(); j++){
			str += morse[int(words[i][j]) - 97];
		}
		if(r.find(str) == r.end()){
			r[str] = 0;
		}
		else r[str] += 1;
	}
	return r.size();
}


int main() {	
	int a[] = { -1, 2, 4, -3, 5, 2, -5, 2 };
	int n = sizeof(a)/sizeof(int);
	cout << maxSubArray2(a, n) << endl;
	bubbleSort(a, n);
	print(a, n);
	vi v;
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	printV(twoSum(v, 6));
	int arr[] = { 10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10};
	int size = sizeof(arr)/sizeof(int);
	vector < int > widths(arr, arr+size);
	string S = "abcdefghijklmnopqrstuvwxyz";
	printV(numberOfLines(widths, S));
	vector< string > words;
	words.push_back("gin");
	words.push_back("zen");
	words.push_back("gig");
	words.push_back("msg");
	cout << uniqueMorseRepresentations(words) << endl;;
	return 0;
}
