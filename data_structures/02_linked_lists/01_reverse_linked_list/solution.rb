class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

def reverse_list(head)
  prev = nil
  current = head

  while !current.nil?
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
  end

  prev
end
