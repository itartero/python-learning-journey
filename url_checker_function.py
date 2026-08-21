# You have many URLs that contain store IDs, but many of them are invalid&mdash;either because they use an invalid protocol (the beginning of the URL) or because the store ID is not seven characters long.
# * The correct URL protocol is `https:` Anything else is invalid.
# * A valid store ID must have exactly seven characters.

# Sample valid URL for reference while writing your function:
# url = 'https://exampleURL1.com/r626c36'

def url_checker(url):
    url = url.split('/')
    if url[0] != 'https:' and len(url[3]) < 7:
        return f'{url[0]} is an invalid protocol. \n{url[3]} is an invalid store id.'
    elif url[0] != 'https:':
        return f'{url[0]} is an invalid protocol.'
    elif len(url[3]) < 7:
        return f'{url[3]} is an invalid store id.'
    else:
        return url[3]

# RUN THIS CELL TO TEST YOUR FUCTION                   # Should return:
print(url_checker('http://exampleURL1.com/r626c3'))    # 'http: is an invalid protocol.'
                                                       # 'r626c3 is an invalid store ID.'
print(url_checker('ftps://exampleURL1.com/r626c36'))   # 'ftps: is an invalid protocol.
print(url_checker('https://exampleURL1.com/r626c3'))   # 'r626c3 is an invalid store ID.'
print(url_checker('https://exampleURL1.com/r626c36'))  # 'r626c36'