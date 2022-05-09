
#1  function which create a list with key or keys that have the biggest value
def show_keys_with_biggest_value (dictionary):
    return [
            key
            for key, value in dictionary
            if (value == max(dictionary.values()))
            ]


#2 With that function u can transform a list into conjunction of parametres -  e.g. exmp. id=5&id=10 if myList = [5, 10]
def change_list_into_conj_of_param (myList, key = 'id'):

    conj = ""
    lastIteration = len(myList)
    numberOfIteration = 0
    
    for item in myList:
        numberOfIteration += 1
        if (numberOfIteration == lastIteration):
            conj += key + '=' + str(item)
        else:
            conj += key +'=' + str(item) + '&'


    return conj