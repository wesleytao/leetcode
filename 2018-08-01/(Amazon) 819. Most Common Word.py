class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        newparagraph = [i.strip("!?',;.") for i in paragraph.lower().split()]
        corpus = {w:0 for w in newparagraph if w not in banned}
        for i in newparagraph:
            if i in corpus:
                corpus[i] +=1
                
        return max(corpus, key = corpus.get)
        