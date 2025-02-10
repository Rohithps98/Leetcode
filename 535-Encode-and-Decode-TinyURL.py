import random
import string
class Codec:
    def __init__(self):
        self.shortmap = {}
        self.urlmap = {}
        self.base = 'https://tinyurl.com'
    def genkey(self):
        return ''.join(random.choices(string.ascii_letters+string.digits,k=6))

    def encode(self, longUrl: str) -> str:
        \\\Encodes a URL to a shortened URL.
        \\\
        while longUrl in self.shortmap:
            return self.shortmap[longUrl]
        shortkey = self.genkey()
        while shortkey in self.urlmap:
            shortkey = self.genkey()
        shorturl = self.base+shortkey
        self.urlmap[shorturl] = longUrl
        self.shortmap[longUrl] = shorturl
        return shorturl

    def decode(self, shortUrl: str) -> str:
        \\\Decodes a shortened URL to its original URL.
        \\\
        return self.urlmap.get(shortUrl,'')

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))