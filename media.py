import fresh_tomatoes

class Movie:

    def __init__(self, title, image_url, trailer_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_id = trailer_url


def make_page():
    mad_max = Movie("Mad Max: Fury Road",
                    "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY317_CR2,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=hEJnMQG9ev8")
    bad_boys = Movie("Bad Boys",
                     "http://www.gstatic.com/tv/thumb/movieposters/6963/p6963_p_v7_aa.jpg",
                     "https://www.youtube.com/watch?v=RRILgwNJNkI")
    enter_the_void = Movie("Enter the Void",
                           "https://upload.wikimedia.org/wikipedia/en/3/39/Enter-the-void-poster.png",
                           "https://www.youtube.com/watch?v=bKRxDP--e-Y")
    fresh_tomatoes.open_movies_page([mad_max, bad_boys, enter_the_void])