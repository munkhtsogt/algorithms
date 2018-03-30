#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class Solution {
	public:
		
		// https://leetcode.com/problems/rotate-string/description/
		bool rotateString(string A, string B){
			return (A.length() == B.length() && (A + A).find(B) != string::npos);
		}
		
		// https://leetcode.com/problems/all-paths-from-source-to-target/description/
		vector< vector<int> > allPathsSourceTarget(vector< vector<int> > &graph) {
        	vector< vector<int> > results;
       		vector<int> tmp;
       		tmp.push_back(0);
       		vector<bool> visited(graph.size(), false);
       		visited[0] = true;
        	DFS(0, graph, visited, tmp, results);
        	return results;
    	}
    	
    	void DFS(int u, vector< vector<int> > adj, vector<bool> &visited, vector<int> tmp, vector< vector<int> > results){
    		if(u == adj.size() - 1) {	
    			results.push_back(tmp);
    		}
    		else {
				for(int i = 0; i < adj[u].size(); i++){
					if(visited[adj[u][i]] == false) {
    					tmp.push_back(adj[u][i]);
    					visited[adj[u][i]] = true;
						DFS(adj[u][i], adj, visited, tmp, results);
						tmp.pop_back();
    					visited[adj[u][i]] = false;
					}
				}
    		}
    	}
    	
    	// https://leetcode.com/problems/champagne-tower/description/
    	double champagneTower(int poured, int query_row, int query_glass) {
		    double triangle[102][102] = {0.0};
		    triangle[0][0] = poured;
		    for(int i = 0; i <= query_row; i++){
		        for(int j = 0; j <= i; j++){
		            if(triangle[i][j] >= 1.0){
		                double d = triangle[i][j] - 1.0;
		                triangle[i][j] = 1.0;
		                triangle[i+1][j] += d / 2.0;
		                triangle[i+1][j+1] += d / 2.0;
		            }
		        }
		    }
		    return triangle[query_row][query_glass];
    	}
    	
    	// https://leetcode.com/problems/number-of-matching-subsequences/description/
    	int numMatchingSubseq(string S, vector<string>& words) {
        	int counter = 0;
        	map<string, int> flagged;
        	for(int i = 0; i < words.size(); i++){
        		if(flagged.find(words[i]) == flagged.end()){
        			flagged[words[i]] = 0;
        			int len = 0, j = 0;
		    		for(int k = 0; k < words[i].length(); k++){
		    			while(j < S.length()){
		    				if(words[i][k] == S[j]){
		    					len++;
		    					j++;
		    					break;
		    				}
		    				j++;
		    			}
		    		}
					if(len == words[i].length()) {
						counter++;
						flagged[words[i]] = 1;
					}
        		}
        		else if(flagged[words[i]] == 1) counter++;
        	}
        	return counter;
    	}
    	
    	// https://leetcode.com/contest/weekly-contest-74/problems/number-of-subarrays-with-bounded-maximum/
    	int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
    		int max = -1, counter = 0;
        	for(int i = 0; i < A.size(); i++){
        		if(L <= A[i] && A[i] <= R){
        			max = A[i] > max ? A[i] : max;
        			counter++;
        		}
        	}
        	return counter;
    	}
    	
    	// https://leetcode.com/contest/weekly-contest-74/problems/valid-tic-tac-toe-state/
    	bool validTicTacToe(vector<string>& board) {
        
        	return false;
    	}
};

int main() {
	Solution sol;
	/*
	cout << sol.rotateString("abcde", "abced") << endl;
	cout << sol.rotateString("bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy",
"wpnrbwfcdmwctusunasdbpbmhnvybqqutquvbtgouklsayfvze") << endl;
	cout << sol.champagneTower(5, 2, 0) << endl;
	cout << sol.champagneTower(2, 2, 0) << endl;
	cout << sol.champagneTower(1, 0, 0) << endl;
	cout << sol.champagneTower(2, 1, 1) << endl;
	cout << sol.champagneTower(1, 1, 1) << endl;
	cout << sol.champagneTower(6, 2, 1) << endl;
	cout << sol.champagneTower(0, 1, 0) << endl;
	cout << sol.champagneTower(1, 1, 0) << endl;
	cout << sol.champagneTower(1000000000, 99, 99) << endl;
	vector<string> words;
	words.push_back("a");
	words.push_back("bb");
	words.push_back("acd");
	words.push_back("ace");
	cout << sol.numMatchingSubseq("abcde", words) << endl;*/
	return 0;
}
