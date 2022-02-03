class News:
    '''
    News class to define news objects
    '''
    def __init__(self,description,url,category,language,country):
        description: description
        url:url 
        category: category 
        language: language
        country: country

class Article:
    '''
    Class to define News articles
    '''
    def __init__(self, author, title, description, url, urlToImage, publishedAt, content):
        
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
    
        
        