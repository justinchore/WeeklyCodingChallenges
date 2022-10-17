
import sys
sys.path.append('C:/Users/jchou/Desktop/WeeklyCodingChallenges')

from node_class import Node

def create_inter_linked_lists():
    
    #a -> b -> c ------>
    #                   d -> e
    #x -> y -> z -> q ->    
    a = Node("a")
    b = Node("b")
    a.next = b
    c = Node("c")
    b.next = c
    d = Node("d")
    c.next = d
    e = Node("e")
    d.next = e
    
    x = Node("x")
    y = Node("y")
    x.next = y
    z = Node("z")
    y.next= z
    q = Node("q")
    z.next = q
    q.next = d
    
    return [a, x]
    

'''
First method: 0(n+m) time, O(1) space

1. Find lengths of the two linked lists with 2 pointers (1, 2)
2. Get the difference between the two lengths
3. Traverse the longer list, de-incrementing the difference and setting the pointer to the node
4. Now the 2 pointers are the same distance away from the intersect node
5. Reset both pointers, then traverse both lists until equal node is found
6. If None appears, return False

'''
def find_intersecting_node_lengths(head1, head2):
    #find length of both lists:
    list_1_length = 0
    current1 = head1
    while current1 != None:
        list_1_length += 1
        current1 = current1.next
    
    list_2_length = 0
    current2 = head2
    while current2 != None:
        list_2_length += 1
        current2 = current2.next
    
    #Get Difference between lengths to find out how many nodes to skip! This will affect the longer list only. If the lists are same length, no skipping is needed
    diff = abs(list_1_length - list_2_length)

    #reset pointers to be at the beginning of respective lists
    current1 = head1
    current2 = head2
    
    #if list1 is longer, then we skip the number of nodes according to the "diff" , then set pointer1 to new location
    if list_1_length > list_2_length:
        # print("list1 greater")
        while diff > 0:
            current1 = current1.next
            diff -= 1
    #vice versa
    else:
    #     print("else")
        while diff > 0:
            current2 = current2.next
            diff -= 1
            
   
    #now that both pointers are in the same distance away from the intersecting node, traverse equally through the the lists until equality is found
    while current1 != current2:
        # print('current1', current1.val)
        # print('current2', current2.val)
        
        current1 = current1.next
        current2 = current2.next
        
        #If there is a none either both or one of the nodes before equality is found, that means that there is no intersection
        if current1 is None or current2 is None:
            return False
        
    
    return current1.val

'''
Second method: O(n+m) time, O(1) space

1. 2 pointers will start at their respective list heads
2. Once a pointer reaches the None (the end of the list), set the pointer to the head of the other list
3. Eventually, the two pointers will line up to be the same distance away from the intersect node

'''
def find_intersection_switch_pointers(head1, head2):
    
    current1 = head1
    current2 = head2
    
    while current1 != current2:
            
        if current1 is None and current2 is None:
            return False
        
        current1 = head2 if current1 == None else current1.next
        current2 = head1 if current2 == None else current2.next
                
    
    return current1.val
      
            


lists = create_inter_linked_lists()
lists[0].print_nodes() #a ->b ->c ->d ->e ->
lists[1].print_nodes() #x ->y ->z ->q ->d ->e ->
print(find_intersecting_node_lengths(lists[0], lists[1])) #Expect 'd'
print(find_intersection_switch_pointers(lists[0], lists[1]))#Expect 'd'
               