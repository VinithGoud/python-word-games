import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
internet = response.content.splitlines()

simple = ['dinosaurs',
         'friendship',
         'sausage',
         'eggs',
         'breakfast',
         'hamburgers',
         'drink',
         'hook',
         'chauffeur',
         'dragonfly']

tech = ['javascript',
         'python',
         'proxy',
         'class',
         'integer',
         'string',
         'pipe',
         'java',
         'linux',
         'hackerman']