/**
 * Created by Luffy on 2017/3/17.
 */

//1    2   6   7   15
//3    5   8   14
//4    9   13
//10   12
//11

public class z_array {
	//之字型走势的数组A，给你个小标(i, j)，求出A(i, j)。
	public int get_num_from_zarray(int i, int j){
		int res = 0;
		int inc = i + j;
		int min = ((1+inc)*inc/2) + 1;
		if((i+j) % 2 == 0)
			res = min + j;
		else
			res = min + i;
		System.out.println(res);
		return res;
	}
	//之字型走势的数组A，给你A(i, j)，求出小标(i, j)。
	public void get_index_by_num(int num){
		int i = 0;
		int j = 0;
		for(int k = 0;k <= num;k++){
			int min = (1+k)*k/2 + 1;
			int max = (1+k+1)*(k+1)/2;
			if(num > min && num < max){
				if(k % 2 == 0){
					j = num -min;
					i = k - j;
					break;
				}
				else{
					i = num - min;
					j = k - i;
					break;
				}
			}
			else if(num == min){
				if (k % 2 == 0){
					i = k;
					j = 0;
					break;
				}else{
					j = k;
					i = 0;
					break;
				}
			}else if (num == max){
				if (k % 2 == 0){
					i = 0;
					j = k;
					break;
				}else{
					i = k;
					j = 0;
					break;
				}
			}
		}

		System.out.println(i);
		System.out.println(j);
	}
	public static void main(String args[]){
		z_array z = new z_array();
		int res = z.get_num_from_zarray(1,6);
		z.get_index_by_num(30);
	}
}
