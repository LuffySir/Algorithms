import java.util.Stack;

/**
 * Created by Luffy on 2017/3/21.
 */
public class q22_IsPopOrder {
	public static boolean IsPopOrder(int [] pushA, int [] popA){
		if (pushA.length == 0 || popA.length == 0)
			return false;
		Stack<Integer> stack = new Stack<Integer>();
		int popindex = 0;
		for (int i = 0; i < pushA.length; i ++){
			stack.push(pushA[i]);
			while (!stack.isEmpty() && stack.peek() == popA[popindex]){
				stack.pop();
				popindex ++;
			}

		}
		return stack.isEmpty();
	}

	public static void main(String[] args) {
		int [] pushA = {1,2,3,4,5};
		int [] popA = {4,5,3,1,2};
		boolean res = IsPopOrder(pushA,popA);
		System.out.println(res);
	}
}
