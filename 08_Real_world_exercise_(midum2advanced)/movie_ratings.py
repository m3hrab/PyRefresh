"""### Exercise 8: **Movie Ratings**
You are given a list of movies and the ratings given by multiple users. Write a function that:
- Finds the movie with the highest average rating.
- Identifies movies rated by all users.
"""

movies_ratings = {
    'Inception': [5, 4, 4, 5],
    'The Matrix': [5, 5, 5, 4],
    'Interstellar': [4, 4, 4]
}

# def avg(n):
#     n = n[1]
#     if len(n)> 0:
#         return sum(n)/len(n)
#     else:
#         return 0
    

# new = []
# for movie, ratings in movies_ratings.items():
#     new.append((movie, ratings))

# new.sort(key=avg, reverse=True)
# print(f"Higest Average rated movie: {new[0][0]}, Average rating: {sum(new[0][1])/len(new[0][1]):.2f}")

# another solution
highest_rated_movie = None
highest_avg_rate = 0
 
for movie, ratting in movies_ratings.items():
    avg = sum(ratting) / len(ratting)
    if highest_avg_rate < avg:
        highest_rated_movie = movie
        highest_avg_rate = avg 
        
print(f"Higest Average Rated Movie: {highest_rated_movie}, Average Rating: {highest_avg_rate}")


# All user count 
all_user = len(max(movies_ratings.values(), key=len))
movies_rated_by_all_user = [movie for movie, ratings in movies_ratings.items() if len(ratings)==all_user]
print(f"Movies Rated by all users: {movies_rated_by_all_user}")
