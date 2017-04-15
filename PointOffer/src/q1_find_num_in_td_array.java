/**
 * Created by Luffy on 2017/3/16.
 */
public class q1_find_num_in_td_array {
	public boolean find(int [][]array, int target){
		int row = 0;
		int col = array[0].length - 1;
		while(row <= array.length - 1 && col >= 0){
			if(target == array[row][col])
				return true;
			else if(target > array[row][col])
				row ++;
			else
				col --;
		}
		return false;
	}

	public static void main(String args[]){

	}
}

