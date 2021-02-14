if __name__=='__main__':
    movies_list = ["Avengers Endgame","Avengers Infinity war","The Avengers","Iron man 3"]
    user =str(input('Enter movie name: '))
    search_list =[]
    index = 0
    split_user = user.split(" ")
    for movies in movies_list:
        index += 1
        split_moviesList = movies.split(" ")
        for keyword1 in split_user:
            for keyword2 in split_moviesList:
                if keyword1 == keyword2:
                   search_list.append(index)

    print (len(search_list),"Results found \n")
    for index in search_list:
        print (movies_list[index-1]+"\n")
