#Algorithms:

def ElementLocater(dr,l):
    curr_handler = dr
    for i in l:
        curr_handler = curr_handler.find_element_by_xpath(i)
    return curr_handler
    

def Union(lst1, lst2): 
    final_list = lst1 + lst2 
    return final_list 


def RoleParser(s):
	handler = s
	role = handler.split(",")[0]
	handler = handler.split(",")[1][1:]
	otpt = ""
	for i in handler:
		if(i == " "):
			break
		else:
			otpt = otpt + i
	return (role,int(otpt))

def RoleSorter(role_dict , members):
	mem_dict = {}
	for i in role_dict:
		n = role_dict.get(i)
		for j in range(0,n):
			if(i in list(mem_dict.keys())):
				mem_dict[i].append(members[j])
			else:
				mem_dict[i] = [members[j]]
		members = members[n:]
	return(mem_dict)






