package Algorithms;

import java.util.Hashtable;

public class Problems {

	static int stickers(String word) {
		Hashtable<String, Integer> ht = new Hashtable<>();
		ht.put("w", 1);
		ht.put("p", 1);
		ht.put("e", 2);
		ht.put("n", 2);
		ht.put("g", 1);
		ht.put("i", 1);
		Hashtable<String, Integer> ht2 = new Hashtable<>();
		
		for(int i = 0; i < word.length(); i++) {
			String chr = "" + word.charAt(i);
			if(!ht2.containsKey(chr)) {
				ht2.put(chr, 1);
			}
			else {
				ht2.put(chr, ht2.get(chr) + 1);
			}
		}
		
		int diff = -1;
		for(String key: ht2.keySet()) {
			if(ht.containsKey(key)) {
				diff = (int) Math.max(Math.ceil((double)ht2.get(key)/ht.get(key)), diff);
			}
			else return -1;
		}
		
		return diff;
	}
	
	static int checksum(int[] arr) {
		if (arr.length == 0) return 0;
		int rightMost = arr.length - 1;
		int sum = arr[rightMost];
		for(int i = rightMost - 1; i >= 0; i--) {
			if((rightMost - i) % 2 != 0) {
				int num = arr[i] * 5;
				while (num != 0) {
					sum += num % 10;
					num /= 10;
				}
			}
			else sum += arr[i];
		}
		return sum;
	}
	
	static int longestCycle(int[] arr) {
		if(arr.length  <= 1) return arr.length;
		int longest = 0;
		Hashtable<Integer, Boolean> ht = new Hashtable<>();
		for(int i = 0; i < arr.length; i++) {
			int c = 0;
			int j = arr[arr[i]];
			while(!ht.containsKey(j)) {
				ht.put(j, true);
				j = arr[j];
				c++;
			}
			longest = Math.max(longest, c);
		}
		return longest;
	}
	
	public static void main(String[] args) {
		/*System.out.println(stickers("winning"));
		int[] arr = {1};
		System.out.println(checksum(arr));*/
		int[] arr2 = {1,0};
		System.out.println(longestCycle(arr2));
	}
}

