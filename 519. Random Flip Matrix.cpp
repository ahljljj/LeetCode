/*
519. Random Flip Matrix

You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.

*/

// cpp, random

class Solution {
    int nr, nc, rem;
    unordered_map<int, int> m;
    //c++11 random integer generation
    mt19937 rng{random_device{}()};
    //uniform random integer in [0, bound]
    int randint(int bound) {
        uniform_int_distribution<int> uni(0, bound);
        return uni(rng);
    }

public:
    Solution(int n_rows, int n_cols) {
        nr = n_rows;
        nc = n_cols;
        rem = nr * nc;

    }

    vector<int> flip() {
//        int r = rand() % rem;
//        --rem;
        int r = randint(--rem);
        int x;
        if (m.find(r) == m.end()){
            x = r; m[r] = r;
        }
        else{
            x = m[r];
        }
        if (m.find(rem) != m.end()) m[r] = m[rem];
        else{
            m[rem] = rem; m[r] = rem;
        }

        return {x / nc, x % nc};

    }

    void reset() {
        m.clear();
        rem = nr * nc;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n_rows, n_cols);
 * vector<int> param_1 = obj.flip();
 * obj.reset();
 */