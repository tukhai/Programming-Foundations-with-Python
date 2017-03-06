import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his sex toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=moSRMC5JNww")

#print(avatar.storyline)

#avatar.show_trailer()

old_school = media.Movie("Old School",
                     "A bunch of losers come back and contribute to their old University Club",
                     "http://www.movieposter.com/posters/archive/main/33/MPW-16722",
                     "https://www.youtube.com/watch?v=VqtymOtKr48")

old_boy = media.Movie("Old Boy",
                     "Incest is the main theme of the movie",
                     "https://s-media-cache-ak0.pinimg.com/originals/7b/ff/97/7bff97d959d5137765faa6cfb9681182.jpg",
                     "https://www.youtube.com/watch?v=2HkjrJ6IK5E")

no_country_for_old_man = media.Movie("No country for Old Man",
                     "While out hunting, Llewelyn Moss (Josh Brolin) finds the grisly aftermath of a drug deal. Though he knows better, he cannot resist the cash left behind and takes it with him. The hunter becomes the hunted when a merciless killer named Chigurh (Javier Bardem) picks up his trail.",
                     "http://www.impawards.com/2007/posters/no_country_for_old_men.jpg",
                     "https://www.youtube.com/watch?v=YBqmKSAHc6w")

the_40_year_old_virgin = media.Movie("The 40-Year_old Virgin",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2005/posters/forty_year_old_virgin.jpg",
                     "https://www.youtube.com/watch?v=YnDeJn-BX5Q")

movies = [toy_story, avatar, old_school, old_boy, no_country_for_old_man, the_40_year_old_virgin]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
