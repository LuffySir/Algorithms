/**
 * Created by Luffy on 2017/3/23.
 */

class RandomListNode {
	int val;
	RandomListNode next = null;
	RandomListNode random = null;

	RandomListNode(int label) {
		this.val = label;
	}
}

public class q26_CopyComplexLinklist {
	public RandomListNode CopyComplexLinklist(RandomListNode head){
//		第一步，复制原始链表节点并连入原始节点的next
		RandomListNode pNode = head;
		while (pNode != null){
			RandomListNode cNode = new RandomListNode(pNode.val);
			cNode.next = pNode.next;
			cNode.random = null;
			pNode.next = cNode;
			pNode = cNode.next;
		}

//		第二步，复制random指针
		pNode = head;
		while (pNode != null){
			RandomListNode cNode2 = pNode.next;
			if (pNode.random != null){
				cNode2.random = pNode.random.next;
			}
			pNode = cNode2.next;
		}

//		第三步，奇偶数节点拆分
		pNode = head;
		RandomListNode cHead = null;
		RandomListNode cNode3 = null;
		if (head != null){
			cHead = cNode3 = pNode.next;
			pNode.next = cNode3.next;
			pNode = pNode.next;
		}
		while (pNode != null){
			cNode3.next = pNode.next;
			cNode3 = cNode3.next;
			pNode.next = cNode3.next;
			pNode = pNode.next;
		}
		return cHead;
	}
}
