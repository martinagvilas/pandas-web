import operator
import feedparser


SITES = ['https://wesmckinney.com/feeds/all.atom.xml',
         'https://tomaugspurger.github.io/feed',
         'https://jorisvandenbossche.github.io/feeds/all.atom.xml',
         'https://datapythonista.github.io/blog/atom.xml']


def get_posts():
    posts = []
    for feed_url in SITES:
        feed_data = feedparser.parse(feed_url)
        for entry in feed_data.entries:
            posts.append({'title': entry.title,
                          'author': entry.author,
                          'published': entry.published_parsed,
                          'feed': feed_data['feed']['title'],
                          'link': entry.link,
                          'description': entry.description,
                          'summary': entry.summary})
    posts.sort(key=operator.itemgetter('published'), reverse=True)
    return posts


if __name__ == '__main__':
    import pprint
    pprint.pprint(get_posts()[:3])
