import jsonpickle
import string

class SentimentAnalyzer:
    """
    A class to conduct natural language analysis (sentiment analysis) on stocktwits messages
    """
    def __init__(self):
        """
        initialize the structure
        sets up initial dictionaries
        """
        self.ratings_dict = dict()

        with open('word_dict', "r") as outputfile:
            self.custom_dict = jsonpickle.decode(outputfile.read())
        outputfile.close()

#       general positive and negative words lists
#       SOURCE:  Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews."
#       Proceedings of the ACM SIGKDD International Conference on Knowledge
#       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle,
#       Washington, USA
        posfile = open('/home/nathan/PycharmProjects/LeafTrade/src/positivewords.txt', 'r')
        self.positive_words = [word.strip() for word in posfile.readlines()]
        negfile = open('/home/nathan/PycharmProjects/LeafTrade/src/negativewords.txt')
        self.negative_words = [word.strip() for word in negfile.readlines()]

    def AnalyzeSentiment(self, message):
        """
        Analyze the sentiment of a given message
        :param message: message to analyze
        :param symbol: symbol that this message pertains to
        :return: a positive/negative sentiment rating
        """
        sentiment = 0
        message_words = string.split(message.lower())
        for word in message_words:
            if self.custom_dict.__contains__(word):
                sentiment += self.custom_dict[word]
            else:
                self.custom_dict[word] = 0
                if self.positive_words.__contains__(word):
                    sentiment += 1
                    self.custom_dict[word] += 1
                if self.negative_words.__contains__(word):
                    sentiment -= 1
                    self.custom_dict[word] -= 1

        for word in message_words:
            if 'bear' in word:
                if sentiment < 0:
                    sentiment *= -1
            if 'bull' in word:
                if sentiment > 0:
                    sentiment *= -1

        if sentiment > 5:
            self.__ModifyRatings(True, message_words)
        elif sentiment < -5:
            self.__ModifyRatings(False, message_words)

        with open('word_dict', "w") as outputfile:
            encoded = jsonpickle.encode(self.custom_dict)
            outputfile.write(encoded)

        return sentiment

    def __ModifyRatings(self, isPositive, message_words):
        """
        Modifies existing word rating, depending on previous context
        Is this machine learning? I thought it was cool
        :param isPositive: whether or not the context of the sentence was positive
        :param message_words: the words in the message
        :return: N/A
        """
        for word in message_words:
            if isPositive:
                self.custom_dict[word] += 1
            else:
                self.custom_dict[word] -= 1


