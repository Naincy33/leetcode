class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary.sort(key=len)
        words=sentence.split(" ")
        result=[]
        for word in words:
            replaced= False

            for root in dictionary:
                if word.startswith(root):
                    result.append(root)
                    replaced = True
                    break

            if not replaced:
                result.append(word)

        return " ".join(result)
obj= Solution()
print(obj.replaceWords(["cat","catt","bat","rat"], "the cattle was rattled by the battery"))