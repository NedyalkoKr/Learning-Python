# bytes is data type for representing sequences of bytes
# used to store and represent raw binary data

# creating new bytes object using literal form(notation)
print(b'data')

# encoding str object to bytes object
some_text = "this is the text that we want to convert to bytes."
some_text_encoded = some_text.encode("utf-8")
print(type(some_text_encoded))

# decode from bytes to string
some_text_decoded = some_text_encoded.decode("utf-8")
print(type(some_text_decoded))