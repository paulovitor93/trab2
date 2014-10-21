##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


##########  Complete the following functions. ############

def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    
    >>> text = ['William Shakespeare\n', 'Paulo!!!, Pedro and Maria\n']
    6.0
    """
    # To do: Fill in this function's body to meet its specification.
    count = 0
    len_words = []
    
    for sentence in text:
        words = sentence.split()
        for word in words:
            clean_word = clean_up(word)
            len_words.append(len(clean_word))
            count += 1
    
    return sum(len_words)/count
    

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    >>> text = ['William Shakespeare\n', 'Paulo!!!, Paulo will and maria, Pedro and Maria\n']
    >>> type_token_ratio(text)
    0.7
    """
  
    # To do: Fill in this function's body to meet its specification.
    count = 0
    dif_words = []
    
    for sentence in text:
        words = sentence.split()
        for word in words:
            clean_word = clean_up(word)
            if clean_word in dif_words:
                count += 1
            else:
                dif_words.append(clean_word)
                count += 1
    
    return len(dif_words)/count
                
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    """
 
    # To do: Fill in this function's body to meet its specification.
    total_words = 0
    clean_words = []
    repeated_words = []    
    for sentence in text:
        words = sentence.split()
        for word in words:
            clean_words.append(clean_up(word))
            total_words +=1
    
    for i in range(len(clean_words)):
        for x in range(len(clean_words)):
            if(clean_words[i] == clean_words[x] and i != x):
                repeated_words.append(clean_words[i])
    return ((total_words - len(repeated_words)) / total_words)

def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    >>> split_on_separators("Hi, how are you? Fine, thanks.", ",?")
    ['Hi', 'how are you', 'Fine', 'thanks' ]
    """
    
    # To do: fill in this function's body to meet its specification.
    # You are not required to keep the two lines below but you may find
    # them helpful. (Hint)
    
    result = [original]
    for char in separators:
        pieces = []
        for substr in result:
            pieces.extend(substr.split(char))
        result = pieces
    return result
                
    
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    

def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """
    
    # To do: Fill in this function's body to meet its specification.
    
    
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """
    
    # To do: Fill in this function's body to meet its specification.
