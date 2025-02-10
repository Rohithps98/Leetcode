import random
import string
class Codec:
    def __init__(self):
        self.shortmap = {}
        self.urlmap = {}
        self.base = 'https://tinyurl.com'
    def shortkey(self):
        return ''.join(random.choices(string.ascii_letters+string.digits,k=6))
    def encode(self, longUrl: str) -> str:
        \\\Encodes a URL to a shortened URL.
        \\\
        if longUrl in self.shortmap:
            return self.shortmap[longUrl]
        short_key = self.shortkey()
        while short_key in self.urlmap:
            short_key = self.shortkey()
        short_url = self.base+short_key
        self.urlmap[short_url] = longUrl
        self.shortmap[longUrl] = short_url
        return short_url

    def decode(self, shortUrl: str) -> str:
        \\\Decodes a shortened URL to its original URL.
        \\\
        return self.urlmap.get(shortUrl,\\)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))