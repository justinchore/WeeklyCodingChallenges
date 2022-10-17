from node_class import Node

'''
 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''


def main():
    #Create intersected linked lists:
    head_1, head_2 = create_intersected_linked_list()
    result = find_intersection(head_1, head_2)
    print(result)
    node_1 = create_circular_linked_list()
    result2 = loop_detection(node_1)
    print(result2)
    


def create_intersected_linked_list():
    a = Node("a", b)
    b = Node("b", c)
    c = Node("c", c)
    d = Node("d", e)
    e = Node("e", None)
    
    x = Node("x", y)
    y = Node("y", d)
    
    return [a, x]

def create_circular_linked_list():
    node_1 = Node(1, node_2)
    node_2 = Node(2, node_3)
    node_3 = Node(3, node_4)
    node_4 = Node(4, node_2)
    
    return node_1



#########################################################################

#######FIND INTERSECTION ###############
def find_intersection(head_1, head_2):
    while head_2: #99
        temp = head_1 
        while temp:
            if temp == head_2:
                return head_2
            temp = temp.next
        head2 = head2.next
    
    return None

########LOOP DETECTION############

def loop_detection(node_1):
    node_dict = {}
    current = node_1
    while current is not None:
        if current not in node_dict:
            node_dict[current] = True
        else: 
            return current
        current = current.next
    
    return None


#  A = 3 ➔ 7 ➔ 8 ➔ 10
#  B = 99 ➔ 1 ➔ 8 ➔ 10
    
    






            
   
   

