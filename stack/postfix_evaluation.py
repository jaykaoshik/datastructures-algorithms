from infix_to_postfix import in2post
infix=input().split()
postfix=in2post(infix)
s=postfix.split()

stack=[]
for i in range(len(s)):
	elem=s[i]
	if(elem.isnumeric()):
		stack.append(int(elem))
	else:
		if(elem=="+"):
			l=stack.pop()
			k=stack.pop()
			stack.append(k+l)

		if(elem=="*"):
			l=stack.pop()
			k=stack.pop()
			stack.append(k*l)

		if(elem=="-"):
			l=stack.pop()
			k=stack.pop()
			stack.append(k-l)

		if(elem=="/"):
			l=stack.pop()
			k=stack.pop()
			stack.append(k/l)

		if(elem=="^"):
			l=stack.pop()
			k=stack.pop()
			stack.append(k**l)

print(stack.pop())




