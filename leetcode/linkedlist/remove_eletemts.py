# Definition for singly-linked list.
"""
https://leetcode-cn.com/problems/remove-linked-list-elements/
203. 移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head


class Solution1(object):
    def removeElements(self, head, val):
        """
        虚拟头结点
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
                cur.next = None
            else:
                pre = pre.next

        return dummy_head.next


class Solution2(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            del_node = head
            head = head.next
            del_node.next = None

        if not head:
            return head

        pre = head
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
                cur.next = None
            else:
                pre = pre.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head = Solution1().removeElements(head, 1)
    print(head)
