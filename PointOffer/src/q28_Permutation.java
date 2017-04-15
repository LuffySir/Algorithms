import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by Luffy on 2017/3/25.
 */
public class q28_Permutation {

	public static ArrayList<String> Permutation(String str){
		ArrayList<String> res = new ArrayList<>();

		if(str != null && str.length() > 0){
			PermutationHelper(str.toCharArray(), 0, res);
			Collections.sort(res);
		}
		System.out.println(res);
		return res;
	}

	public static void PermutationHelper(char[] cs, int i, ArrayList<String> list){
		if (i == cs.length - 1){
			list.add(String.valueOf(cs));
		} else{
			for (int j = i; j < cs.length; ++j){
				if (j == i || cs[j] != cs[i]){
					swap(cs, i, j);
					PermutationHelper(cs, i+1,list);
					swap(cs, i, j);
				}
			}
		}
	}
	public static void swap(char[] cs, int i, int j){
		char temp = cs[i];
		cs[i] = cs[j];
		cs[j] = temp;
	}

	public static void main(String[] args) {
		Permutation("abcd");
	}

}
