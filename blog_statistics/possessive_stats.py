



#Prints Statistics on distribution of possessive words
#For male and female bloggers (Words ending in 's or s')
def print_possessive_info(possess):

	print("")
	fem_poss = sum(possess[0].values())
	mal_poss = sum(possess[1].values())
	tot_poss = float(fem_poss+mal_poss)
	print("Distribution of %d possessive words" % int(tot_poss))
	print("Male: %.2f%% \t Female: %.2f%%" %(100*fem_poss/tot_poss, 100*mal_poss/tot_poss))
	print("")
