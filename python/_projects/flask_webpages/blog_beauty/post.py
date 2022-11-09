# post.py 
# Updated: cramos 28/oct/2022
# This is a class to be used in the Blog web page

class BlogPost:
    """ This class contains the structure of a blog post """
    def __init__(self, post_id, title, subtitle, body):
        self.post_id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body
