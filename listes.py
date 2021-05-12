import random

MIN_2DIGITS_NUMBER = 11
MAX_2DIGITS_NUMBER = 99
INTERVAL = 15
EXTREMAL_REPETITION = 2
CENTRAL_REPETITION = 4

MEAN_2DIGITS_NUMBER = int((MIN_2DIGITS_NUMBER +  MAX_2DIGITS_NUMBER) / 2)

                
def create_task_list(standard = MEAN_2DIGITS_NUMBER,
                                    minimal_number = MIN_2DIGITS_NUMBER,
                                    maximal_number = MAX_2DIGITS_NUMBER,
                                    interval = INTERVAL,
                                    extremal_repetiton = EXTREMAL_REPETITION,
                                    central_repetition = CENTRAL_REPETITION):
    
    intermediate_lower_bound =  (standard - interval) + 1
    intermediate_higher_bound = (standard + interval)

    lower_list =                        list(range(minimal_number                     , intermediate_lower_bound))
    intermediate_lower_list = list(range(intermediate_lower_bound   , standard))
    intermediate_higher_list= list(range(standard + 1                           , intermediate_higher_bound))
    higher_list =                       list(range(intermediate_higher_bound  , maximal_number + 1))

    task_list = (
        (lower_list * extremal_repetiton) +
        (intermediate_lower_list * central_repetition) +
        (intermediate_higher_list * central_repetition) +
        (higher_list * extremal_repetiton)
    )
    random.shuffle(task_list)
    return task_list


def create_training_list(my_list, training_list_length):
    training_list = random.sample(my_list, training_list_length)
    return training_list


def shuffle_list_from_index(my_list, index):
    end_of_list = my_list[index:]
    random.shuffle(end_of_list)
    my_list[index:] = end_of_list
    #We do not return the list to be consistent with ramdom.shuffle but it is modifided in my_list


def is_element_identical_to_previous_in_list(my_list, index):
    if index < 1:
        return False
    
    element = my_list[index]
    precedent_element = my_list[index -1]
    if (element == precedent_element):
        return True
    return False


def is_element_same_side_of_standard_as_previous_two_in_list(my_list, standard, index):
    if index < 2:
        return False

    element = my_list[index]
    precedent_element = my_list[index - 1]
    anteprecedent_element = my_list[index - 2]
    if (element < standard) and (precedent_element < standard) and (anteprecedent_element < standard):
        return True
    if (element > standard) and (precedent_element > standard) and (anteprecedent_element > standard):
        return True
    return False


def is_element_valid_at_index(my_list, index, standard):
    return not ( is_element_identical_to_previous_in_list(my_list, index) or is_element_same_side_of_standard_as_previous_two_in_list(my_list, standard, index) )


def try_gradually_shuffle_list_to_match_task_conditions(my_list, standard):
    for index in range(len(my_list)):
        iteration_number = 0
        while (not is_element_valid_at_index(my_list, index, standard)) and iteration_number < 100:
            shuffle_list_from_index(my_list, index)
            iteration_number += 1

        if iteration_number == 100:
            return False
    return True
    #We do not return the list to be consistent with ramdom.shuffle but it is modifided in my_list


def shuffle_list_until_match_task_conditions(my_list, standard):
    while not try_gradually_shuffle_list_to_match_task_conditions(my_list, standard):
        random.shuffle(my_list)
    #We do not return the list to be consistent with ramdom.shuffle but it is modifided in my_list

        
def create_valid_experimental_list(standard, training_list_length):
    task_list = create_task_list()
    training_list = create_training_list(task_list, training_list_length)
    shuffle_list_until_match_task_conditions(task_list, standard)
    experimental_list = training_list + task_list
    return experimental_list




################# Unused fonctions

def has_2_consecutive_elements_identical_in_list(my_list):
    my_list_without_first_element = my_list[1:]
    for index, element in enumerate(my_list_without_first_element):
        precedent_element = my_list[index]
        if (element == precedent_element):
            return True
    return False


def has_3_consecutive_elements_same_side_of_threshold_in_list(standard, my_list):
    my_list_without_first_two_elements = my_list[2:]
    for index, element in enumerate(my_list_without_first_two_elements):
        precedent_element = my_list[index + 1]
        anteprecedent_element = my_list[index]
        if (element < standard) and (precedent_element < standard) and (anteprecedent_element < standard):
            return True
        if (element > standard) and (precedent_element > standard) and (anteprecedent_element > standard):
            return True
    return False


################ Fonction that were used to verifie if the program was correct

def is_correct(my_list, standard):
    for index in range(len(my_list)):
        if is_correct_at_index(my_list,index, standard):
            return True
    return False
