class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = SLNode(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, value):
        new_node = SLNode(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self


class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()

print()
test1 = SList()
test1.add_to_front("f_first").add_to_front("f_second").add_to_front("f_third").print_values()

print()
test2 = SList()
test2.add_to_front("need something in front").add_to_back("b_first").add_to_back("b_second").add_to_back("b_third").print_values()