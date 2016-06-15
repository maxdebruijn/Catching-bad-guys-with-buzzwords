from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer("english", ignore_stopwords=True)
dutchStemmer = SnowballStemmer("dutch", ignore_stopwords=True)


def stringtofeatures(input):
    features = ""
    featuresList = []
    input = input.strip()
    #print line
    replaceList = ("\\", ",", "+", "-", "[", "]", "(", ")", "_", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    for item in replaceList:
        input = input.replace(item, " ")
    input = input.lower()
    #print line
    words = input.split()
    for word in words:
        stemmedWord = stemmer.stem(word)
        doubleStemmedWord = dutchStemmer.stem(stemmedWord)
        if not doubleStemmedWord.isdigit():
            #print doubleStemmedWord
            featuresList.append(doubleStemmedWord)

    features = " ".join(featuresList)
    # print features
    return features

def listtofeatures(input):
    featuresarray = []
    for item in input:
        processed_item = stringtofeatures(item)
        featuresarray.append(processed_item)
    return featuresarray
