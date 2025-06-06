# -*- coding: utf-8 -*-
"""cleaner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a8wvZdStWn1xJ4t9xSb7tlL1ifrnZ0k2
"""

import re

def clean_transcript(text):
    """
    Cleans up transcript text:
    - Removes timestamps [00:01], (00:01:05), etc.
    - Removes filler words and extra whitespace
    - Removes speaker labels like 'Speaker 1:', 'Prof:', etc.
    """
    # Remove timestamps
    text = re.sub(r'\[?\(?\d{1,2}:\d{2}(:\d{2})?\)?\]?', '', text)

    # Remove speaker tags (basic)
    text = re.sub(r'(Speaker\s?\d+:|Prof(\.|essor)?\s?:)', '', text)

    # Remove common filler words
    filler_words = ['uh', 'um', 'you know', 'like', 'so', 'basically']
    for word in filler_words:
        text = re.sub(rf'\b{word}\b', '', text, flags=re.IGNORECASE)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

