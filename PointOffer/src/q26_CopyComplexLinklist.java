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
//		��һ��������ԭʼ����ڵ㲢����ԭʼ�ڵ��next
		RandomListNode pNode = head;
		while (pNode != null){
			RandomListNode cNode = new RandomListNode(pNode.val);
			cNode.next = pNode.next;
			cNode.random = null;
			pNode.next = cNode;
			pNode = cNode.next;
		}

//		�ڶ���������randomָ��
		pNode = head;
		while (pNode != null){
			RandomListNode cNode2 = pNode.next;
			if (pNode.random != null){
				cNode2.random = pNode.random.next;
			}
			pNode = cNode2.next;
		}

//		����������ż���ڵ���
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
