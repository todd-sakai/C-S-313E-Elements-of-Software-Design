class MinPriorityQueue:

	def __init__(self, node=None):
		self.list = []
		if node is not None:
			self.enqueue(node)

	def __str__(self):
		return self.list.__str__()

	def __repr__(self):
		return self.__str__()

	def enqueue(self, new_item):
		self.list.append(new_item)
		self.list.sort()

	def dequeue(self):            
		return self.list.pop(0) if not self.is_empty() else None

	def is_empty(self):
		return len(self.list) == 0

	def get_size(self):
		return len(self.list)
