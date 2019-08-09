def in2post(s):
	stack=[]
	postfix=""
	operator_map={"(":0,"-":1,"+":2,"/":3,"*":4,"^":5}
	for i in range(len(s)):
		elem=s[i]
		if(elem.isnumeric()):
			postfix=postfix+elem+" "
		else:
			if(elem=="("):
				stack.append(elem)
			elif(elem==")"):
				popped_elem=")"
				while(popped_elem!="("):
					popped_elem=stack.pop()
					if(popped_elem!="("):
						postfix=postfix+popped_elem+" "
			else:
				if(len(stack)==0):
					stack.append(elem)
				else:
					stack_top=stack.pop()
					stack.append(stack_top)

					if(operator_map[elem]>operator_map[stack_top]):
						stack.append(elem)
					else:

						while(operator_map[elem]<=operator_map[stack_top] and len(stack)>0):
							postfix=postfix+stack_top+" "
							stack.pop()
							if(len(stack)>0):
								stack_top=stack.pop()
								stack.append(stack_top)


						
						stack.append(elem)

	while(len(stack)>0):
		stack_top=stack.pop()
		postfix=postfix+stack_top+" "
							
	return(postfix)




