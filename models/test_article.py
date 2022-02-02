import unittest
from news import Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of the NewsArticle class
    '''
    def setUp(self):
        '''
        Set up method to run before every test
        '''

        self.new_article = Article('mashable', 'Mashable', 'Karissa Bell', 'Amazon challenges Google with smaller, cheaper Echo Show', 'Amazon just ratcheted up the pressure on Google.', 'https://mashable.com/article/amazon-echo-show-5/', 'https://mondrian.mashable.com/2019%252F05%252F29%252F4d%252Fd91b4bcb383142c1b52ffbac16165110.01151.jpg%252F1200x630.jpg?signature=R9UT45RZefZ53JiuK0HJ5OQNCoU=', '2019-05-29T13:00:00Z', 'Amazon just ratcheted up the pressure on Google in a major way.\r\nThe company just unveiled its new Echo Show 5, a smaller and cheaper version of its Echo Show speaker. The $89.99 device is available … [+2026 chars]' )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))