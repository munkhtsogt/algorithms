
import java.io.*;
import java.util.*;

// Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise. Your function then should return that array. Analyze the time and space complexities of your solution.

// Example:

// input:  inputMatrix  = [ [1,    2,   3,  4,    5],
//                          [6,    7,   8,  9,   10],
//                          [11,  12,  13,  14,  15],
//                          [16,  17,  18,  19,  20] ]

// output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
class SpiralMatrix {
  public static void main (String[] args) {

    int[][] matrix = 
      {
        {1,    2,   3,  4,    5},
         {6,    7,   8,  9,   10},
         {11,  12,  13,  14,  15},
         {16,  17,  18,  19,  20}
      };
      
      int[] results = helper(matrix);
      
      for(int i = 0; i < results.length; i++){
        System.out.print(results[i] + " ");
      }
      System.out.println();
  }
  
  public static int[] helper(int[][] matrix){
    int[] results = new int[matrix.length * matrix[0].length];
      
    int bottom = 0, right = matrix[0].length - 1, left = 0, up = matrix.length - 1;
    int index = 0;

    while(left != right && up != bottom){
      // right
      for(int i = left; i <= right; i++){
        results[index] = matrix[bottom][i];
        index++;
      }
      bottom++;

      // bottom
      for(int i=bottom; i <= up; i++){
        results[index] = matrix[i][right];
        index++;
      }
      right--;

      // left
      for(int i=right; i >= left; i--) {
        results[index] = matrix[up][i];
        index++;
      }
      up--;

      // up
      for(int i = up; i >= bottom; i--){
        results[index] = matrix[i][left];
        index++;
      }
      left++;
    }
    
    return results;
  }
  
}
