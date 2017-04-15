import java.util.Arrays;

/**
 * Created by Luffy on 2017/3/22.
 */
public class q24_VerifySequenceOfBST {
	public static boolean VerifySquenceOfBST(int [] sequence) {
		if (sequence == null || sequence.length == 0)
			return false;
		int root = sequence[sequence.length - 1];
		int i = 0;
		for (;i < sequence.length - 1;i++){
			if (sequence[i] > root)
				break;
		}
		int j = i;
		for (;j < sequence.length - 1;j++){
			if (sequence[j] < root)
				return false;
		}
		boolean left = true;
		boolean right = true;
		if (i > 0)
			left = VerifySquenceOfBST(Arrays.copyOfRange(sequence,0,i));
		if (j < sequence.length - 1)
			right = VerifySquenceOfBST(Arrays.copyOfRange(sequence,i,sequence.length-1));
		return (left && right);
	}

	public static void main(String[] args) {
		int [] sec = {4,7,6,12,10,8};
		boolean res = VerifySquenceOfBST(sec);
		System.out.println(res);
	}
}
