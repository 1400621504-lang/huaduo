class CircularlistNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # 指向下一个节点

# 尾插法：向循环链表添加节点
def append_Node(head, val):
    newNode = CircularlistNode(val)
    # 如果链表为空，自己指向自己，形成循环
    if head is None:
        head = newNode
        head.next = head
        return head

    # 找到最后一个节点
    cur = head
    while cur.next != head:
        cur = cur.next
    # 插入新节点
    cur.next = newNode
    newNode.next = head
    return head


# 打印循环链表
def print_Node(head):
    if head is None:
        return
    cur = head
    while True:
        print(cur.val, end="\t")
        cur = cur.next
        if cur == head:
            print()
            break


# 删除第 k 个节点（约瑟夫环专用）
# 删除第 m 个节点（从自己开始数，标准约瑟夫环）
def remove_node(head, m):
    cur = head

    # 走 m-1 步（因为从自己开始数1）
    for i in range(m - 1):
        cur = cur.next

    # cur 是第 m 个节点，删掉它
    tem = cur
    # 找到前一个节点
    pre = head
    while pre.next != tem:
        pre = pre.next

    pre.next = tem.next
    return tem


# 约瑟夫环主函数
def jose(n, m):
    # 1. 创建 n 个节点的循环链表
    head = None
    for i in range(1, n + 1):
        head = append_Node(head, i)

    print("初始链表：", end="")
    print_Node(head)

    print("依次出列的序号：", end="")
    # 2. 开始删除节点
    while head != head.next:  # 不止一个节点时继续
        del_node = remove_node(head, m - 1)
        print(del_node.val, end="\t")
        head = del_node.next  # 下一次从被删节点下一个开始

    # 打印最后一个幸存者
    print("\n最后幸存者：", head.val)


if __name__ == "__main__":
    jose(6, 5)  # 6个人，数5下删除