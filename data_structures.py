#Exercise 1 - List
favorite_fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango'] #List of favorite fruits
print(favorite_fruits[1])       #Accessing the second element of the list

for fruit in favorite_fruits:   #Iterating over the list.
    print(fruit)

favorite_fruits.append('guava') #Adding a new element using append()
print(favorite_fruits)


#Exercise 2 - Dictionary
favorite_book = {               #Created a dictionary about my favorite book
    'Title' :'Checkmate',
    'Author': 'Steven James',
    'Genre': 'Mystery, Thriller, Suspense',
}
print(favorite_book['Genre'])