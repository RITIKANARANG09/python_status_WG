menu_option="Enter 'a' to add movie, 's' to see your movies, 'f' to find movies, 'q' to quit"
movies=[]
title=input("Enter title of movie")
director=input("Enter movie director")
year=input("Enter movie release year")
def add_movie():
    movies.append(
        {
            "title":title,
            "director":director,
            "year":year
        }
    )

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title : {movie['Title']}")
    print(f"Director : {movie['Director']}")
    print(f"Year : {movie['Year']}")

my_student={
    'name':'r',
    'grades':[20,30,40,50]
}
def avg_student():
    grades=my_student['grades']
    print(sum(grades)/len(grades))
def find_movie():
    movie_title=input("Enter title of movie you are looking for : ")
    for movie in movies:
        if(movie['Title']==movie_title):
            print_movie(movie)
            break

user_options={
    'a':add_movie,
    's':show_movies,
    'f':find_movie
}

def menu():
    option_select=input(menu_option)
    while option_select!='q':
        if option_select in user_options:
           selected_option=user_options[option_select]
           selected_option();
        else:
            print("Enter valid input")

        option_select = input(menu_option)

menu()