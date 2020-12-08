def find(bt,sum):
	if(root==None):
		return []
	ret=[]
	queue=[(root,[],0)]
	while(len(queue)!=0):
		node,l,s=queue.pop(-1)
		if(node.left!=None):
			tmp1=l.copy()
			tmp1.append(node.val)
			queue.append((node.left,tmp1,s+node.val))
		if(node.right!=None):
			tmp2=l.copy()
			tmp2.append(node.val)
			queue.append((node.right,tmp2,s+node.val))
		elif(node.right==None and node.left==None and s+node.val==sum):
			tmp=l.copy()
			tmp.append(node.val)
			ret.append(tmp)
	return ret
