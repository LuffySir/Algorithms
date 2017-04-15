/**
 * Created by Luffy on 2017/3/18.
 */
public class q8_Number_of_one {
	public static int Number_of_1(int n){
		int count = 0;
		int flag = 1;
		while(flag != 0){
			if ((n & flag) != 0){
				count ++;
			}
			flag = flag << 1;
		}
		return count;
	}

//	n & (n-1)能够使最右边一位1变成0，前面不变
	public static int Number_of_1_optimal(int n){
		int count = 0;
		while (n != 0){
			count ++;
			n = n & (n-1);
		}
		return count;
	}

	public static void main(String[] args) {
		int res1 = Number_of_1(7);
		int res2 = Number_of_1_optimal(7);
		System.out.println(res1);
		System.out.println(res2);
	}
}
