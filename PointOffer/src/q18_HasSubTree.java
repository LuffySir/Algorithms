/**
 * Created by Luffy on 2017/3/20.
 */
public class q18_HasSubTree {
	public boolean HasSubTree(TreeNode root1, TreeNode root2){
		boolean res = false;
		if (root1 != null && root2 != null){
			if (root1.val == root2.val)
				res = DoesSameTree(root1, root2);
			if (!res){
				res = HasSubTree(root1.left, root2);
			}
			if (!res){
				res = HasSubTree(root1.right, root2);
			}
		}
		return res;
	}

	public boolean DoesSameTree(TreeNode root1, TreeNode root2){
		if (root2 == null)
			return true;
		if (root1 == null)
			return false;
		if (root1.val != root2.val)
			return false;
		return DoesSameTree(root1.left, root2.left) && DoesSameTree(root1.right, root2.right);
	}
}
