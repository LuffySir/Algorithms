/**
 * Created by Luffy on 2017/3/18.
 */
public class q7_Fibonacci {
	public int fib(int num){
		int prepre = 1;
		int pre = 1;
		int curr = 0;
		if(num <= 0)
			throw new RuntimeException("wrong num");
		if (num<=2)
			return pre;
		for (int i = 2;i < num; i++){
			curr = prepre + pre;
			prepre = pre;
			pre = curr;
		}
		return curr;
	}

	public static void main(String[] args) {
		q7_Fibonacci fibb = new q7_Fibonacci();
		int res = fibb.fib(6);
		System.out.println(res);
	}
}
