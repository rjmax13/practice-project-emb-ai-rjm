from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        #Test case for positive sentiment result
        result1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result1['label'], 'SENT_POSITIVE')
        #Test case for negative sentiment result
        result2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result2['label'], 'SENT_NEGATIVE')
        #Test case for neutral sentiment result
        result3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result3['label'], 'SENT_NEUTRAL')

unittest.main()
