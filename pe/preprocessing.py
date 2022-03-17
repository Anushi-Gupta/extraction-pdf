def text_cleaning(text_data):#Text cleaning using regex so as to have required text data.
    import re
    import string
    text_data=re.sub(r'\s+', ' ', text_data)
    text_data=re.sub(r'[0-9]+', '', text_data)
    text_data=re.sub(r',','',text_data)
    text_data=re.sub('<[^>]+?>', '', text_data)
    text_data = "".join([ch for ch in text_data if ch.isalnum() or ch in string.punctuation or ch.isspace()])
    text_data = text_data.encode("ascii", "ignore")
    text_data = text_data.decode()
    return text_data