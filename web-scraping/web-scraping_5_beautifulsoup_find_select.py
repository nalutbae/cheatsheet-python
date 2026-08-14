# BeautifulSoup: find, find_all, find_parents, and advanced filtering

from bs4 import BeautifulSoup, Tag, NavigableString, Comment

HTML = """
<html>
<body>
    <div id="app" class="container">
        <header class="site-header" data-section="top">
            <h1 id="logo" class="brand large">My Site</h1>
            <p class="tagline">Learn, Build, Deploy</p>
            <nav class="main-nav" aria-label="Main">
                <a href="/" class="link active" data-page="home">Home</a>
                <a href="/about" class="link" data-page="about">About</a>
                <a href="/blog" class="link" data-page="blog">Blog</a>
                <a href="/contact" class="link" data-page="contact">Contact</a>
            </nav>
        </header>

        <main class="content" data-section="main">
            <article id="post-1" class="post python featured" data-category="python" data-views="500" data-level="advanced">
                <h2 class="title">Python Async Patterns</h2>
                <p class="excerpt">Deep dive into async/await patterns.</p>
                <div class="author-info">
                    <span class="author" data-user-id="u1">Alice</span>
                    <time datetime="2026-01-15">Jan 15, 2026</time>
                </div>
                <div class="body-content">
                    <p>First paragraph of the article.</p>
                    <p>Second paragraph with <strong>bold text</strong> and <em>italic</em>.</p>
                    <pre class="code-block"><code>async def fetch_data():
    await asyncio.sleep(1)</code></pre>
                </div>
                <div class="tags">
                    <a href="/tags/python" class="tag">python</a>
                    <a href="/tags/async" class="tag">async</a>
                    <a href="/tags/featured" class="tag highlight">featured</a>
                </div>
            </article>

            <article id="post-2" class="post javascript" data-category="javascript" data-views="120" data-level="intermediate">
                <h2 class="title">JS Closures</h2>
                <p class="excerpt">Understanding closures step by step.</p>
                <div class="author-info">
                    <span class="author" data-user-id="u2">Bob</span>
                    <time datetime="2026-02-20">Feb 20, 2026</time>
                </div>
                <div class="body-content">
                    <p>JavaScript closures explained.</p>
                </div>
                <div class="tags">
                    <a href="/tags/javascript" class="tag">javascript</a>
                    <a href="/tags/closures" class="tag">closures</a>
                </div>
            </article>

            <article id="post-3" class="post rust draft" data-category="rust" data-views="0" data-level="advanced">
                <h2 class="title">Rust Ownership</h2>
                <p class="excerpt">Memory safety without GC.</p>
                <div class="body-content">
                    <p>Coming soon...</p>
                </div>
            </article>
        </main>

        <aside class="sidebar" data-section="side">
            <div class="widget popular">
                <h3>Popular</h3>
                <ul>
                    <li><a href="/posts/1">Python Async</a></li>
                    <li><a href="/posts/2">JS Closures</a></li>
                </ul>
            </div>
        </aside>

        <footer class="site-footer">
            <p>&copy; 2026 My Site</p>
        </footer>
    </div>

    <!-- This is a comment -->
    Some loose text outside containers.
</body>
</html>
"""

soup = BeautifulSoup(HTML, "html.parser")

print("=" * 5, "find() — find first matching element", "=" * 5)

# By tag name
article = soup.find("article")
print(f"First article: {article.h2.string}")  # Python Async Patterns

# By id
logo = soup.find(id="logo")
print(f"Logo: {logo.string}")  # My Site

# By class (string or list)
featured = soup.find("article", class_="featured")
print(f"Featured: {featured.h2.string}")  # Python Async Patterns

# Multiple classes — matches elements with ALL specified classes
python_featured = soup.find("article", class_=["python", "featured"])
print(f"Python+featured: {python_featured.h2.string}")

# By attribute
post = soup.find(attrs={"data-category": "javascript"})
print(f"JavaScript post: {post.h2.string}")

# By string (exact match)
tag = soup.find(string="python")
print(f"Exact string: {tag}")  # python

# By regex
import re

heading = soup.find(re.compile(r"^h[12]$"))
print(f"First h1/h2: {heading.string}")

# By function
def has_data_views(tag):
    return tag.has_attr("data-views") and int(tag["data-views"]) > 100

popular = soup.find(has_data_views)
print(f"First post with views > 100: {popular.h2.string}")

print("=" * 5, "find_all() — find all matching elements", "=" * 5)

# All articles
all_articles = soup.find_all("article")
print(f"\nAll articles: {len(all_articles)}")  # 3

# Limit results
first_two = soup.find_all("article", limit=2)
print(f"First 2 articles: {len(first_two)}")

# Find all links with href
all_links = soup.find_all("a", href=True)
print(f"All links with href: {len(all_links)}")

# Find all elements with data-views attribute
with_views = soup.find_all(attrs={"data-views": True})
print(f"Elements with data-views: {len(with_views)}")

# Find all with specific data attribute value
python_posts = soup.find_all("article", attrs={"data-category": "python"})
print(f"Python posts: {[p.h2.string for p in python_posts]}")

print("=" * 5, "find_all() — string/text parameter options", "=" * 5)

# Exact string match
python_text = soup.find_all(string="python")
print(f"Exact 'python': {len(python_text)} strings")  # 2 (tag + sidebar)

# Regex match
import re
code_strings = soup.find_all(string=re.compile(r"async|await"))
print(f"Strings matching 'async|await': {len(code_strings)}")

# List of strings — matches any
multi = soup.find_all(string=["python", "javascript"])
print(f"Strings 'python' or 'javascript': {len(multi)}")

# Function filter
def long_strings(text):
    return isinstance(text, NavigableString) and len(text.strip()) > 20

long_text = soup.find_all(string=long_strings)
print(f"Strings longer than 20 chars: {len(long_text)}")
for t in long_text[:3]:
    print(f"  '{t.strip()[:50]}...'")

print("=" * 5, "find_all() — class_ parameter deep dive", "=" * 5)

# Single class
python_els = soup.find_all(class_="python")
print(f"Elements with class 'python': {len(python_els)}")

# Multiple classes (list) — element must have ALL classes
multi_class = soup.find_all(class_=["python", "featured"])
print(f"Elements with both 'python' AND 'featured': {len(multi_class)}")

# Regex for class
tag_links = soup.find_all("a", class_=re.compile(r"tag"))
print(f"Links with 'tag' in class: {len(tag_links)}")

# Function for class
def has_highlight_class(class_list):
    if isinstance(class_list, list):
        return "highlight" in class_list
    return class_list == "highlight"

highlighted = soup.find_all(class_=has_highlight_class)
print(f"Highlighted elements: {len(highlighted)}")

print("=" * 5, "find_next / find_previous / find_siblings", "=" * 5)

# find_next — next matching element after this one
first_article = soup.find("article")
second_article = first_article.find_next("article")
print(f"Next article after first: {second_article.h2.string}")  # JS Closures

# find_previous — previous matching element before this one
last_article = soup.find_all("article")[-1]
prev_article = last_article.find_previous("article")
print(f"Previous article before last: {prev_article.h2.string}")  # JS Closures

# find_next_sibling / find_previous_sibling
nav = soup.find("nav")
first_link = nav.find("a")
next_link = first_link.find_next_sibling("a")
print(f"Next nav link: {next_link.string}")  # About

# find_all_next / find_all_previous
excerpt = soup.find("p", class_="excerpt")
all_next_p = excerpt.find_all_next("p")
print(f"All <p> after first excerpt: {len(all_next_p)}")

# find_all_next with limit
next_two = excerpt.find_all_next("p", limit=2)
print(f"Next 2 <p>: {[p.get_text(strip=True)[:30] for p in next_two]}")

print("=" * 5, "find_parents / find_parent", "=" * 5)

# find_parent — first matching parent
author = soup.find("span", class_="author")
article = author.find_parent("article")
print(f"Author's article: {article.h2.string}")  # Python Async Patterns

# find_parents — all matching parents up the tree
all_parents = author.find_parents("div")
print(f"Author's div parents: {len(all_parents)}")

parent_names = [p.get("class", []) for p in all_parents]
print(f"Parent div classes: {parent_names}")

print("=" * 5, "select() vs find_all() — comparison", "=" * 5)

# find_all with class
by_find = soup.find_all("article", class_="post")
print(f"find_all(article.post): {len(by_find)}")

# select with CSS
by_css = soup.select("article.post")
print(f"select('article.post'): {len(by_css)}")

# find_all with attribute
by_attr = soup.find_all("article", attrs={"data-views": "500"})
print(f"find_all(data-views=500): {len(by_attr)}")

# select with attribute
by_css_attr = soup.select('article[data-views="500"]')
print(f"select([data-views=500]): {len(by_css_attr)}")

# Complex selectors — CSS is more concise
# find_all: multiple steps
articles = soup.find_all("article", class_="post")
python_articles = [a for a in articles if "python" in a.get("class", [])]
print(f"\nPython articles (find_all + filter): {len(python_articles)}")

# select: one step
python_by_css = soup.select("article.post.python")
print(f"Python articles (CSS selector): {len(python_by_css)}")

# :not() — CSS can exclude, find_all cannot directly
non_draft = soup.select("article:not(.draft)")
print(f"Non-draft (CSS :not): {len(non_draft)}")

# :has() — CSS can select parents
with_author = soup.select("article:has(.author)")
print(f"Articles with author (CSS :has): {len(with_author)}")

print("=" * 5, "extract() and decompose() — remove elements", "=" * 5)

# extract() — remove and return element
import copy
soup_copy = copy.copy(soup)  # Work on a copy
sidebar = soup_copy.find("aside")
extracted = sidebar.extract()
print(f"Extracted sidebar tag: {extracted.name}")  # aside
print(f"Sidebar removed from tree: {soup_copy.find('aside')}")  # None

# decompose() — remove and destroy (no return)
soup_copy2 = copy.copy(soup)
draft = soup_copy2.find("article", class_="draft")
draft.decompose()
print(f"After decompose draft: {len(soup_copy2.find_all('article'))}")  # 2

# Use extract() to rearrange
soup_copy3 = copy.copy(soup)
footer = soup_copy3.find("footer").extract()
header = soup_copy3.find("header")
header.append(footer)  # Move footer inside header (nonsensical, but demonstrates extract)
print(f"Footer now inside header: {bool(soup_copy3.find('header').find('footer'))}")

print("=" * 5, "NavigableString — working with text nodes", "=" * 5)

# Find text nodes directly
from bs4 import NavigableString

all_strings = soup.find_all(string=True)
visible_text = [s for s in all_strings if s.strip()]
print(f"Total visible text nodes: {len(visible_text)}")

# Filter text by content
import re
async_texts = soup.find_all(string=re.compile(r"(?i)async"))
print(f"Text containing 'async': {len(async_texts)}")
for t in async_texts:
    print(f"  '{t.strip()[:60]}'")

# Replace text
first_excerpt = soup.find("p", class_="excerpt")
old_text = first_excerpt.string
first_excerpt.string.replace_with("Updated excerpt text.")
print(f"\nReplaced text: '{old_text}' → '{first_excerpt.string}'")

# Insert text before/after
first_excerpt.insert_before(NavigableString("BEFORE. "))
first_excerpt.insert_after(NavigableString(" AFTER."))
print(f"With insertions: {first_excerpt.parent.get_text(strip=True)[:60]}")