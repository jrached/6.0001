# Problem Set 4B
# Name: Juan Rached
# Collaborators: Marissa Abbott
# Time Spent: 7:00 
# Late Days Used: 0 used (using 3 now)

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_digit_shift(input_shift, decrypt):
    '''
    calculate the digit shift based on if decrypting or not
    decrypt: boolean, if decrypting or not
    Returns: digit_shift, the digit shift based on if decrypting or not
    '''
    if decrypt:
        digit_shift = 10 - (26-input_shift)%10
    elif input_shift > 20:
        digit_shift = input_shift - 20
    elif input_shift > 10:
        digit_shift = input_shift - 10
    else:
        digit_shift = input_shift
        
#Modified function to correct shift for digits
        
    return digit_shift

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # delete this line and replace with your code here
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        # delete this line and replace with your code here
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        # delete this line and replace with your code here
        valid_words_copy = self.valid_words[:]
        return valid_words_copy

    def make_shift_dict(self, input_shift, decrypt=False):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter and number.

        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift, as well as
        every number to one shifted down by the same amount. If 'a' is
        shifted down by 2, the result is 'c' and '0' shifted down by 2 is '2'.

        The dictionary should contain 62 keys of all the uppercase letters,
        all the lowercase letters, and all numbers mapped to their shifted values.

        input_shift: the amount by which to shift every letter of the
        alphabet and every number (0 <= shift < 26)

        decrypt: if the shift dict will be used for decrypting. affects digit shift function

        Returns: a dictionary mapping letter/number (string) to
                 another letter/number (string).
        '''
        # delete this line and replace with your code here
        
        #CReate strings for upper/lower cases and digits
        upperString = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        lowerString = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
        digitString = "0 1 2 3 4 5 6 7 8 9"
        
        #Convert each string into a list
        list1 = upperString.split(' ')
        list2 = lowerString.split(' ')
        list3 = digitString.split(' ')
        
        #if the shift is larger than 26 by x amount
        #convert the shift to that x amount 
        if input_shift > 26:
            input_shift = input_shift%26
        
        #Call digit_shift function
        digit_shift = get_digit_shift(input_shift, decrypt)
        
        #Create an empty dictionary that will map each letter and digit to its corresponding
        #letter/digit to create the cipher
        cipherMap = {}
        
        #For each element on list1, create a key in the dictionary with the same 
        #name as in list1 and set its value to its index in list1. This works as to "index"
        #the dictionary.
        
        for i in range(len(list1)):
            cipherMap[list1[i]] = i
        
        #The following for loop maps the element in the cipherMap dictionary
        #To its corresponding cipher element based on the input_shift. The if statement 
        #checks if the position of the original element plus the shift maps to an element 
        #that is not inside the list, i.e. produces an index error. If so, comes back to the 
        #beggining of the list and maps to an object shifted from a certain amount from the
        #beggining of the list that is whatever is left of the shift after it shifted the original
        #element all the way to the end of the list. This proccess repeats for list2 and list3.
        for i in range(len(list1)):
            if len(list1) - i <= input_shift:
                cipherMap[list1[i]] = input_shift - (len(list1) - i)
            else:
                cipherMap[list1[i]] = i + input_shift
        
        #Assing the ith element of list1, where i is the value of cipherMap
        #at list1[i], to a key of cipherMap. Essentially, since we "indexed" the dictionary
        #and then we shifted the index based on the input_shift, now the element of list1 of i
        #index are gonna be mapped to the elements i + input_shift index. This repeats for list2
        #and list3 creating a dictionary mapping all elements of all three lists to their 
        #corresponding cipher element.
        for i in range(len(list1)):
            cipherMap[list1[i]] = list1[cipherMap[list1[i]]] 
            
        
        #For each element on list2, create a key in the dictionary with the same 
        #name as in list2 and set its value to its index in list2. This works as to "index"
        #the dictionary.
        
        for i in range(len(list2)):
            cipherMap[list2[i]] = i
        
        for i in range(len(list2)):
            if len(list2) - i <= input_shift:
                cipherMap[list2[i]] = input_shift - (len(list2) - i)
            else:
                cipherMap[list2[i]] = i + input_shift
                
        for i in range(len(list2)):
            cipherMap[list2[i]] = list2[cipherMap[list2[i]]] 
    
        
        #For each element on list3, create a key in the dictionary with the same 
        #name as in list3 and set its value to its index in list3. This works as to "index"
        #the dictionary.
        
        for i in range(len(list3)):
            cipherMap[list3[i]] = i
        
        for i in range(len(list3)):
            if len(list3) - i <= digit_shift:
                cipherMap[list3[i]] = digit_shift - (len(list3) - i)
            else:
                cipherMap[list3[i]] = i + digit_shift
                
        for i in range(len(list3)):
            cipherMap[list3[i]] = list3[cipherMap[list3[i]]] 
        
        return cipherMap            
            

    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with the shift
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down by some number of characters, determined by the shift
        value that shift_dict was built with.

        shift_dict: a dictionary with 62 keys, mapping
            lowercase and uppercase letters and numbers to their new letters
            (as built by make_shift_dict)

        Returns: the message text (string) with every letter/number shifted using
            the input shift_dict

        '''
        # delete this line and replace with your code here
       
        textList = []
        
        #This for loop gets letters from the message_text, 
        #finds the value corresponding to it in the cipherMap
        #and appends it to an empty list. It tries this for letters
        #and numbers, but when it finds a symbol, which are not included 
        #in the dictionary, it raises an exception and simply appends
        #the symbol without modifying it.
        for i in range(len(self.message_text)):
            try:
                textList.append(shift_dict[self.message_text[i]])
            except KeyError:
                textList.append(self.message_text[i])
            
        #Turns list into a string which I call cipherText
        cipherText = ''.join(textList)
        
        return cipherText
            
        
        
            
        
 
class PlaintextMessage(Message):
    def __init__(self, input_text, input_shift):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        input_shift: the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using the shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        # delete this line and replace with your code here
        #Message.__init__(self, message_text, valid_words, shift, encryption_dict, encrypted_message_text)
        
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = input_shift
        self.encryption_dict = self.make_shift_dict(self.shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict) 
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        # delete this line and replace with your code here
        return self.shift 

    def get_encryption_dict(self):
        '''
        Used to safely access a copy of self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        # delete this line and replace with your code here
        dict_copy = self.encryption_dict.copy()
        return dict_copy

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        # delete this line and replace with your code here
        return self.encrypted_message_text

    def modify_shift(self, input_shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by the shift.

        input_shift: an integer, the new shift that should be associated with this message.
        [0 <= shift < 26]

        Returns: nothing
        '''
        # delete this line and replace with your code here
        
        #Simple setter function. Biggest differences is to change all the values
        #That depend on self.shift as well, which is why I haeve the two extra lines.
        self.shift = input_shift
        self.encryption_dict = self.make_shift_dict(self.shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict) 


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the message's text

        an EncryptedMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # delete this line and replace with your code here
        self.message_text = input_text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value and
        finding the "best" one.

        We will define "best" as the shift that creates the max number of
        valid English words when we use apply_shift(shift) on the message text.
        If a is the original shift value used to encrypt the message, then
        we would expect (26 - a) to be the  value found for decrypting it.

        Note: if shifts are equally good, such that they all create the
        max number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to originally encrypt
        the message (a) and the decrypted message text using that shift value
        '''
        # delete this line and replace with your code here
        
        #Similarity will keep score of how many letters matched a real word for each shift
        similarity = []
        
        #This for loop searches through all possible shifts, thus creates 26 possible cipherMaps.
        #The map ommits symbols adjacent to words so that only the word itself is looked for 
        #in the 'words.txt' file.
        
        for i in range(26):
            dictio = self.make_shift_dict(i, True)
            trial = (self.apply_shift(dictio)).strip("!@#$%^&*()-_+={}[]|\:;'<>?,./\"").split() 
            
            #This loop increases a counter by one for each word match, then appends the counter
            #to similarity
            counter = 0
            for i in trial:
                if i in self.valid_words:
                    counter +=1
            similarity.append(counter)
        
        #bestMatch is the actual best score, whereas bestShift is the shift that 
        #score pertains to.
        bestMatch = 0 
        bestShift = 0
        
        #For loop to find the best score and identify which shift did it.
        for i in range(26):
            if similarity[i] > bestMatch:
                bestMatch = similarity[i]
                bestShift = i
                
        #Now knowing the best shift, we find the dictionary correspondong to that shift,
        #and use it on the cipher. We use True as an argument as we are deciphering.
        dictio = self.make_shift_dict(bestShift, True)
        trial = self.apply_shift(dictio)
        
        #Return 26 - bestShift as what we found is the 
        #decription shift which is 26 - encryptionShift
        #and return the decrypted message as well.
        return (26 - bestShift, trial) 
    
    #Xj ATY td 23456 dz dpnfcp!
    #'My PIN is 78901 so secure!' != 'My PIN is 12345 so secure!
                
                
def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', 2)
#    print('Expected Output: jgnnq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())
    
    #This test checks for encryption for shift values above 26
    ptm = PlaintextMessage("Hello darkness my old friend, I come to talk to you again", 31)
    print('\nExpected Output: Mjqqt ifwpsjxx rd tqi kwnjsi, N htrj yt yfqp yt dtz flfns')
    print('\nActual Output:', ptm.get_encrypted_message_text())
    
    #This test checks if numbers and upper-case letters are
    #encrypted properly
    ptm = PlaintextMessage("DUDE! I got her phone number look: $123456.46... No dude, that's just tonight's tab",5)
    print("\nExpected Output: IZIJ! N lty mjw umtsj szrgjw qttp: $678901.91... St izij, ymfy'x ozxy ytsnlmy'x yfg")
    print('\nActual Output:', ptm.get_encrypted_message_text())
    

    pass # delete this line and replace with your code here

def test_encrypted_message():
    '''
    Write two test cases for the EncryptedMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (EncryptedMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    encrypted = EncryptedMessage('jgnnq!')
#    print('Expected Output:', (2, 'hello!'))
#    print('Actual Output:', encrypted.decrypt_message())

    # delete this line and replace with your code here
    
    #This test is checking is if periods, question marks,
    #and exclamation marks are decrypted properly
    e = EncryptedMessage("Khoor gdzj, pb qdph lv Mxdq. Zkdw'v brxuv? Zrz ... wkdw'v ehdxwlixo!")
    print('\nExpected Output:', (3, "Hello dawg, my name is Juan. What's yours? Wow ... that's beautiful!"))
    print('\nActual Output:', e.decrypt_message())
    
    #This test is checking if upper-case letters and numbers 
    #are decrypted properly.
    e = EncryptedMessage("L olyh lq 45wk Vwuhhw Ehooylhz, Rwwdzd. Zkhuh gr brx olyh? Li brx whoo ph brxu krph dgguhvv zh frxog eh EHVW IULHQGV...")
    print('\nExpected Output:', (3, 'I live in 12th Street Bellview, Ottawa. Where do you live? If you tell me your home address we could be BEST FRIENDS...'))
    print('\nActual Output:', e.decrypt_message())
def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your EncryptedMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    
    # delete this line and replace with your code here
    
    #Get the story in a string. Create a EncryptedMessage object with that
    #string. Then decrypted using the self.decrypt_message() method and return
    #that string.
    storyCipher = EncryptedMessage(get_story_string())
    story = storyCipher.decrypt_message()
    return story

if __name__ == '__main__':

    # # Uncomment these lines to try running your test cases
    # test_plaintext_message()
    # test_encrypted_message()

    # # Uncomment these lines to try running decode_story_string()
    # best_shift, story = decode_story()
    # print("Best shift:", best_shift)
    # print("Decoded story: ", story)
    pass
