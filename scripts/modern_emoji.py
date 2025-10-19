import emoji

# Works on emoji 2.x; TypeError on emoji 1.x (unknown argument 'language')
print(emoji.emojize("Python is :thumbs_up:", language="alias"))
