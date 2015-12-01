
class Movie:
    """Movie class to be displayed in tiles on webpage """
    def __init__(self, title, release_date, image_url, trailer_url):
        """Constructor for move class. Takes the movie's title along with url's for its poster and trailer on youtube"""
        self.title = title
        self.release_date = release_date
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_url



