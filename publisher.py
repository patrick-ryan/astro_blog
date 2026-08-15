import dateutil.parser
import markdown
import pathlib
import re


PUBLISHED_PATH = pathlib.Path("~/Documents/personal/web/blog/published/").expanduser()

BLOG_PATH = pathlib.Path("~/projects/blog/src/content/blog/").expanduser()


def slug(path: pathlib.Path):
    match = next(re.finditer(r"\d{4}-\d{2}-\d{2}_(.+)", path.name), None)
    if match:
        return match.group()
    else:
        return path.name


if __name__ == "__main__":

    current_blog_post_paths = set(BLOG_PATH.iterdir())
    print(f"Current posts: {current_blog_post_paths}")

    new_blog_post_paths: set[pathlib.Path] = set()
    copy_map: dict[pathlib.Path, pathlib.Path] = {}
    for published_post_path in PUBLISHED_PATH.iterdir():
        md = markdown.Markdown(extensions=['meta'])
        md.convert(published_post_path.read_text())

        pub_date = dateutil.parser.parse(md.Meta["pubdate"][0])

        blog_post_filename = f"{pub_date.strftime("%Y-%m-%d")}_{published_post_path.name}"
        blog_post_path = BLOG_PATH / blog_post_filename

        new_blog_post_paths.add(blog_post_path)
        copy_map[blog_post_path] = published_post_path

    to_write = new_blog_post_paths - current_blog_post_paths
    print(f"New paths to write: {to_write}")

    to_delete = current_blog_post_paths - new_blog_post_paths
    print(f"Paths to delete: {to_delete}")

    answer = input("continue? ")
    should_continue = answer.lower() in ('y', 'yes', '1')

    if should_continue:
        for blog_post_path in to_write:
            copy_map[blog_post_path].copy(blog_post_path)

        for blog_post_path in to_delete:
            blog_post_path.unlink()

        print("done")
    else:
        print("skipped")
