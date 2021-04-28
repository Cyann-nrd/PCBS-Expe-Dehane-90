import random

random.seed(18, version=2)
def create_list():
	list_1 = list(range(11, 41))
	list_2 = list(range(41, 55))
	list_3 = list(range(56, 70))
	list_4 = list(range(70, 100))
	list_total = (list_1 * 2) + (list_2 * 4) + (list_3 * 4) + (list_4 * 2)
	list_final = random.sample(list_total, 232)
	return(list_final)

list_final=create_list()
print(list_final)





#TODO: mettre mes conditions pour ne pas prez deux fois de suite le même nombre
     # pas plus de 3x de suite le même bouton (inf ou sup à 55)



def check_list():
        for i in list_final:
                if i == i + 1:
                        create_list()

list_final=create_list()
print(list_final)
