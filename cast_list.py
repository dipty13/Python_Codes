def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open(filename) as f:
        for name in f:
            cast_list.append(name.split(','))

    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
