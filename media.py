import fresh_tomatoes

#This module specifies class Movie that instantiates objects with certain movie's information including 
#title, poster image, and youtube trailer.

class Movie():
    """ 
        This class makes instances of movie that has title, poster image, and trailer attributes.

        Attributes:
            title: string of the movie title
            image: string of poster image url
            trailer: string of youtube trailer url
    """
    def __init__(self,title,image,trailer):
        """ 
            Inits Movie with title, image, and trailer information
        """    
        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """
            Opens a webbrowser with youtube trailer that's specified in the trailer_youtube_url
        """
        webbrowser.open(self.trailer_url)
#three objects created by Movie class.
Avengers = Movie('The Avengers',
    'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
    'https://www.youtube.com/watch?v=eOrNdBpGMv8')
Iron_man = Movie('Iron Man',
    'https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG',
    'https://www.youtube.com/watch?v=8hYlB38asDY')
Beautiful_mind = Movie('Beautiful Mind',
    'https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg',
    'https://www.youtube.com/watch?v=YWwAOutgWBQ')

movies = [Avengers, Iron_man, Beautiful_mind]

fresh_tomatoes.open_movies_page(movies) #creates an html page based on the movie objects created and opens it.