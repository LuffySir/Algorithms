/**
 * Created by Luffy on 2017/3/18.
 */
public class q9_Power {
	public static double power(double base, int n){
		double res = 1, curr = base;
		int exponent;
		if (n > 0){
			exponent = n;
		}else if (n < 0){
			if (base == 0)
				throw new RuntimeException("分母不能为0");
			exponent = -n;
		}else{
//			0的0次方
			return 1;
		}
		while (exponent != 0){
			if ((exponent & 1) == 1)
				res *= curr;
			curr *= curr;
			exponent = exponent >> 1;
		}
		return n >= 0 ? res : (1 / res);
	}

	public static void main(String[] args) {
		double res = power(1.1,1);
		System.out.println(res);
	}
}
