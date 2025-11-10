def move(my_list, direction):
    index_of_one = my_list.index(1)

    if direction == 'yemin':
      if index_of_one == len(my_list)-1:
        return my_list
      else:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'smoll':
      if index_of_one == 0:
        return my_list
      else:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
