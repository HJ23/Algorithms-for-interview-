class Node:
	def __init__(self):
		self.val = "ROOT"
		self.next = []
	#def __str__(self):
	#	return self.val

class Trie:
	def __init__(self):
		self.head = Node()
	def insert(self,word):
		current = self.head
		found = False
		counter = 0 
		for index,letter  in enumerate(word):
			for node in current.next:
				if(node.val == letter):
					current = node
					found = True
					counter += 1
					break
			if(found):
				found = False
			else:
				break
		#print(word,counter,len(word))
		for i in range(counter,len(word)):
			tmp = Node()
			tmp.val = word[i]
			current.next.append(tmp)
			current = tmp
		a = Node()
		a.val  = "END"
		current.next.append(a)
		print(current)

	def search(self,word):
		current = self.head
		found = False
		for index,letter in enumerate(word):
			for node in current.next:
				if(letter == node.val):
					current = node
					found = True
					break
			if(found):
				found = False
			else:
				break
		for node in current.next:
			if(node.val == "END"):
				return True
		return False
	def startsWith(self,word):
		current = self.head
		counter = 0
		for index,letter in enumerate(word):
			for node in current.next:
				if(node.val == letter):
					current = node
					counter += 1
					break
		if(counter == len(word)):
			return True
		return False
	def print(self):
		queue = [self.head]
		while(queue.__len__()):
			current = queue.pop(0)
			print(f"NODE : {current.val} -> { ','.join([x.val for x in current.next]) }")
			for x in current.next:
				queue.insert(0,x)


a = Trie()
a.insert("apple")
a.insert("app")
a.insert("beta")
a.insert("gamma")
a.insert("application")

print(a.search("appl"))
print(a.startsWith("app"))
print(a.search("beta"))
print(a.search("bet"))
print(a.search("app"))

print(a.print())
