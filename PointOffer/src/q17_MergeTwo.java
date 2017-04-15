/**
 * Created by Luffy on 2017/3/20.
 */
public class q17_MergeTwo {
//	µÝ¹é
	public ListNode Merge(ListNode list1, ListNode list2){
		if (list1 == null)
			return list2;
		else if (list2 == null){
			return list1;
		}
		ListNode mergehead = null;
		if (list1.val < list2.val){
			mergehead = list1;
			mergehead.next = Merge(list1.next, list2);
		}else{
			mergehead = list2;
			mergehead.next = Merge(list1, list2.next);
		}
		return mergehead;
	}

//	·ÇµÝ¹é
	public ListNode Merge_no_Recur(ListNode list1, ListNode list2){
		if (list1 == null)
			return list2;
		else if (list2 == null){
			return list1;
		}
		ListNode mergeHead = null;
		ListNode curr = null;
		while (list1 != null && list2 != null){
			if (list1.val < list2.val){
				if (mergeHead == null){
					mergeHead = curr =list1;
				}else{
					curr.next = list1;
					curr = curr.next;
				}
				list1 = list1.next;
			}else{
				if (mergeHead == null){
					mergeHead = curr = list2;
				}else{
					curr.next = list2;
					curr = curr.next;
				}
				list2 = list2.next;
			}
		}
		if (list1 == null){
			curr.next = list2;
		}else{
			curr.next = list1;
		}
		return mergeHead;
	}
}
