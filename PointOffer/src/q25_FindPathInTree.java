import java.util.ArrayList;

/**
 * Created by Luffy on 2017/3/22.
 */
public class q25_FindPathInTree {
	static ArrayList<ArrayList<Integer>> paths = new ArrayList<ArrayList<Integer>>();
	static ArrayList<Integer> path = new ArrayList<Integer>();
	public static ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
		if (root == null) return paths;
		path.add(root.val);
		target -= root.val;
		if (target == 0 && root.left == null && root.right == null)
			paths.add(new ArrayList<Integer>(path));
		FindPath(root.left, target);
		FindPath(root.right, target);
		path.remove(path.size() - 1);
		return paths;
	}

	public static void main(String[] args) {
		TreeNode t1 = new TreeNode(6);
		TreeNode t2 = new TreeNode(3);
		TreeNode t3 = new TreeNode(2);
		TreeNode t4 = new TreeNode(4);
		TreeNode t5 = new TreeNode(7);
		TreeNode t6 = new TreeNode(5);
		t1.left = t2;
		t1.right = t3;
		t2.left = t4;
		t3.right = t5;
		t3.left = t6;

		ArrayList<ArrayList<Integer>> res = FindPath(t1, 13);
		System.out.println(res);

	}
}
