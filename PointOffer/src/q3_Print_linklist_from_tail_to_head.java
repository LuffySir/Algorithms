/**
 * Created by Luffy on 2017/3/16.
 */

import java.util.ArrayList;
import java.util.Stack;

public class q3_Print_linklist_from_tail_to_head {
	ArrayList<Integer> arrayList = new ArrayList<Integer>();

	// µÝ¹é
	public ArrayList<Integer> printListFromTailtoHead(ListNode listNode){
		if(listNode != null){
			this.printListFromTailtoHead(listNode.next);
			arrayList.add(listNode.val);
		}
		return arrayList;
	}

	// Õ»
	public ArrayList<Integer> printListFromTailtoHead2(ListNode listNode){
		Stack<Integer> stack = new Stack<Integer>();
		while(listNode != null){
			stack.push(listNode.val);
			listNode = listNode.next;
		}

		while(! stack.isEmpty()){
			arrayList.add(stack.pop());
		}
		return arrayList;
	}
}

