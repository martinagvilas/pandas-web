"""
Step 1: Convert rst files to html
Step 2: Render templates with Jinja
"""
import argparse
import os
import shutil
import sys
import typing
import markdown
import jinja2


def get_source_files(source_path: str) -> typing.Generator[str, None, None]:
    for root, dirs, fnames in os.walk(source_path):
        root = os.path.relpath(root, source_path)
        for fname in fnames:
            yield os.path.join(root, fname)


def main(source_path: str, theme_path: str, target_path: str) -> int:
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(theme_path))

    for fname in get_source_files(source_path):
        print(fname)
        dirname = os.path.dirname(fname)
        os.makedirs(os.path.join(target_path, dirname), exist_ok=True)

        extension = os.path.splitext(fname)[-1]
        if extension in ('.html', '.md'):
            with open(os.path.join(source_path, fname)) as f:
                content = f.read()
            if extension == '.md':
                body = markdown.markdown(content,
                                         extensions=['fenced_code'])
                # XXX this is a bit tricky, probably there is a better way
                content = '{% extends "layout.html" %}'
                content += '{% block body %}'
                content += body
                content += '{% endblock %}'
            content = jinja_env.from_string(content).render()
            fname = os.path.splitext(fname)[0] + '.html'
            with open(os.path.join(target_path, fname), 'w') as f:
                f.write(content)
        else:
            shutil.copy(os.path.join(source_path, fname),
                        os.path.join(target_path, dirname))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Documentation builder.')
    parser.add_argument('--sources_path', default='source',
                        help='path to the directory with the markdown pages')
    parser.add_argument('--theme_path', default='theme',
                        help='path to the directory with the static files')
    parser.add_argument('--target_path', default='build',
                        help='directory where to write the output')
    args = parser.parse_args()
    sys.exit(main(args.sources_path, args.theme_path, args.target_path))
