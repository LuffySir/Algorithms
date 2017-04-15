import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by Luffy on 2017/3/21.
 */
public class q23_PrintTreeNodeFromTopToBottom {
	public ArrayList<Integer> PrintTreeNodeFromTopToBottom(TreeNode root){
		ArrayList<Integer> list = new ArrayList<Integer>();
		if (root == null)
			return list;
		Queue<TreeNode> queue = new LinkedList<TreeNode>();
		queue.offer(root);
		while (!queue.isEmpty()){
			TreeNode tn = queue.poll();
			if (tn.left != null)
				queue.offer(tn.left);
			if (tn.right != null)
				queue.offer(tn.right);
			list.add(tn.val);
		}
		return list;
	}
}
