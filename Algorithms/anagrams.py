anagram = []
words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']

# construct a words_dict = { key:value } = { key:sorted(key),...}
# (ex) { 'fired':'deirf', 'alert':'aelrt',...}
words_dict = {}
for w in words:
   words_dict[w] = ''.join(sorted(w))

print words_dict
# make a list of groups with the same value
new_words = sorted(words_dict.values())

print new_words

# make a new dic with sorted keys
# (ex)
#  {'aegllry': ['allergy', 'gallery'],
#   'defir': ['fried', 'fired'], ..........}
anagram = {}
for s in set(new_words):
   anagram[s]=[]
   for k,v in words_dict.items():
      if s == v:
         anagram[s].append(k)


print anagram

# make list of anagrams
# (ex)
# [['allergy', 'gallery'],
#  ['abets', 'baste', 'beast', 'beats'],
#  ['fried', 'fired'], ['remain'], ['alter', 'alert']]
anagram_list = []
for k,v in anagram.items():
   anagram_list.append(v)

print anagram_list