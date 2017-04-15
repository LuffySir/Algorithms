/**
 * Created by Luffy on 2017/3/18.
 */

public class q6_Get_min_from_revers_arr {
	public int minNumberInRotateArray(int [] array){
		int high = array.length - 1;
		int low = 0;
		if (high < 0) return 0;
		while (low < high){
			int mid = low + (high - low) / 2;
			if (array[mid] > array[high]){
				low = mid + 1;
			}else if (array[mid] == array[high]){
				high -= 1;
			}else
				high = mid;
		}
		System.out.println(array[low]);
		return array[low];
	}

	public static void main(String[] args) {
		q6_Get_min_from_revers_arr getmin = new q6_Get_min_from_revers_arr();
		int arr[] = {3,4,5,1,2};
		getmin.minNumberInRotateArray(arr);
	}
}
