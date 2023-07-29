
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
def  word_cloud(data,bgcolor,title):
    plt.figure(figsize = (100,100))
    word_cloud = WordCloud(background_color = bgcolor, max_words = 1000,  max_font_size = 50)
    word_cloud.generate(' '.join(data))
    plt.imshow(word_cloud)
    plt.axis('off')


def word_count(str):
    counts = dict()
    words=str
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def entries_to_remove(entries, repeated_words):
    for key in entries:
        if key in repeated_words:
            del repeated_words[key]
