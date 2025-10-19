import emoji

# Works on emoji 1.x; TypeError on emoji 2.x (unknown argument 'use_aliases')
print(emoji.emojize("Python is :thumbs_up:", use_aliases=True))
