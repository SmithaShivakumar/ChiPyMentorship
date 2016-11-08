import media
import fresh_tomatoes

avatar = media.Movie("Avatar", "Marine in an alien land","http://scifibloggers.com/wp-content/uploads/2010/01/Avatar-Poster.jpg" 
		,"https://www.youtube.com/watch?v=5PSNL1qE6VY" )
toy_story = media.Movie("Toy Story","Boy whose toys come to life", "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc" )
hangover = media.Movie("Hangover", "4 friends in Vegas for Bachelor Party", "http://cdn.collider.com/wp-content/uploads/the-hangover-part-2-movie-poster-01.jpg","https://www.youtube.com/watch?v=vhFVZsk3XEs" )
star_wars = media.Movie("Star Wars","Stars at Wars","http://3g28wn33sno63ljjq514qr87.wpengine.netdna-cdn.com/wp-content/uploads/2015/10/Star-Wars-Poster-700x1068.jpg","https://www.youtube.com/watch?v=frdj1zb9sMY" )


movies = [avatar, toy_story, hangover, star_wars]
# fresh_tomatoes.open_movies_page(movies)
# hangover.show_trailer()

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

# if __name__ == __main__() :
	# hangover.show_trailer()