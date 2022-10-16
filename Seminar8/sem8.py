# my_dict = {'Иванов': 123, 'Ахапкин':435, 'Романов': 2234}

# for person in sorted(my_dict):
#     print(person, my_dict[person])
    
# for person, number in sorted(my_dict.items()):
#     print(person, number)

import pickle 


test_list = ['cucumber', 'pumpkin', 'carrot'] 
with open('test_pickle.pkl', 'wb') as pickle_out: 
    pickle.dump(test_list, pickle_out)


with open('test_pickle.pkl', 'rb') as pickle_in: 
    unpickled_list = pickle.load(pickle_in) 
    print(unpickled_list)
