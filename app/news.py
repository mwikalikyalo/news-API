class News:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        id:id 
        name: name 
        description: description
        url:url 
        category: category 
        language: language
        country: country

class Article:
    '''
    Class to define News articles
    '''
    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
    
        
        