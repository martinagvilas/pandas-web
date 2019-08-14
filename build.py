import argparse
import datetime
import operator
import os
import shutil
import sys
import time
import typing
import feedparser
import markdown
import jinja2


NUM_POSTS = 8
SITES = ['https://wesmckinney.com/feeds/all.atom.xml',
         'https://tomaugspurger.github.io/feed',
         'https://jorisvandenbossche.github.io/feeds/all.atom.xml',
         'https://datapythonista.github.io/blog/atom.xml']


def get_posts():
    posts = []
    for feed_url in SITES:
        feed_data = feedparser.parse(feed_url)
        for entry in feed_data.entries:
            published = datetime.datetime.fromtimestamp(
                time.mktime(entry.published_parsed))
            posts.append({'title': entry.title,
                          'author': entry.author,
                          'published': published,
                          'feed': feed_data['feed']['title'],
                          'link': entry.link,
                          'description': entry.description,
                          'summary': entry.summary})
    posts.sort(key=operator.itemgetter('published'), reverse=True)
    return posts[:NUM_POSTS]


def generate_blog(jinja_env: jinja2.Environment,
                  target_path: str):
    template = jinja_env.get_template('blog.html')
    content = template.render(posts=get_posts())
    with open(os.path.join(target_path, 'blog.html'), 'w') as f:
        f.write(content)


def get_source_files(source_path: str) -> typing.Generator[str, None, None]:
    for root, dirs, fnames in os.walk(source_path):
        root = os.path.relpath(root, source_path)
        for fname in fnames:
            yield os.path.join(root, fname)


def main(source_path: str,
         theme_path: str,
         target_path: str,
         base_url: str) -> int:
    shutil.rmtree(target_path, ignore_errors=True)
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(theme_path))

    for fname in get_source_files(source_path):
        dirname = os.path.dirname(fname)
        os.makedirs(os.path.join(target_path, dirname), exist_ok=True)

        extension = os.path.splitext(fname)[-1]
        if extension in ('.html', '.md'):
            with open(os.path.join(source_path, fname)) as f:
                content = f.read()
            if extension == '.md':
                body = markdown.markdown(content,
                                         extensions=['fenced_code'])
                content = '{% extends "layout.html" %}'
                content += '{% block body %}'
                content += body
                content += '{% endblock %}'
            content = (jinja_env.from_string(content)
                                .render(base_path=base_url))
            fname = os.path.splitext(fname)[0] + '.html'
            with open(os.path.join(target_path, fname), 'w') as f:
                f.write(content)
        else:
            shutil.copy(os.path.join(source_path, fname),
                        os.path.join(target_path, dirname))

    generate_blog(jinja_env, target_path)
    shutil.copytree(os.path.join(theme_path, 'static/'),
                    os.path.join(target_path, 'static'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Documentation builder.')
    parser.add_argument('--sources-path', default='source',
                        help='path to the directory with the markdown pages')
    parser.add_argument('--theme-path', default='theme',
                        help='path to the directory with the static files')
    parser.add_argument('--target-path', default='build',
                        help='directory where to write the output')
    parser.add_argument('--base-url', default='',
                        help='base url where the website is served from')
    args = parser.parse_args()
    sys.exit(main(args.sources_path,
                  args.theme_path,
                  args.target_path,
                  args.base_url))
