class Solution(object):
    def encode(self, strs):
        encoded_string = ""

        for i in range(len(strs)):                              # O(1) time because 1 <= strs.length <= 200
            lofstring = len(strs[i])                            # O(1) time because 0 <= strs[i].length <= 200 -> len() is also O(1)
            encoded_string += "*" + str(lofstring) + "*"        # wrap delimiter around size of word and append to encoded string
            encoded_string += strs[i]
        
        return encoded_string

    def decode(self, encoded):
        decoded_strs = []

        i = 0
        while i < len(encoded):                                 # use while loop instead of range loop since we need to increment i within loop
            i += 1                                              # skip first "*"
            lofstring = ""
            decoded_string = ""

            while encoded[i] != "*":                            # extract the size of the word
                lofstring += encoded[i]
                i += 1
            i += 1                                              # skip second "*"

            lofstring = int(lofstring)
            for j in range(lofstring):                          # extract the original string from the encoded string
                decoded_string += encoded[i]
                i += 1
            
            decoded_strs.append(decoded_string)
        
        return decoded_strs

    # hint: define a delimiter such as * and wrap it around the size of the word

# For Testing Purposes
''' ===============================================
dummy_input = [["Hello","Worlds"]]
estring = encode(dummy_input)
print(estring)
dstrings = decode(estring)
print(dstrings)
=============================================== '''



        
