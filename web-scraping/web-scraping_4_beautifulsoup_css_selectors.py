# BeautifulSoup: CSS selectors — comprehensive deep dive

from bs4 import BeautifulSoup

HTML = """
<html lang="en">
<head>
    <link rel="stylesheet" href="/css/main.css" />
    <link rel="stylesheet" href="/css/print.css" media="print" />
    <link rel="icon" href="/favicon.ico" />
</head>
<body>
    <header id="site-header" class="site-header dark">
        <h1 id="logo">My Blog</h1>
        <nav id="main-nav" data-section="primary">
            <ul class="nav-list">
                <li class="nav-item active"><a href="/" class="link primary">Home</a></li>
                <li class="nav-item"><a href="/about" class="link">About</a></li>
                <li class="nav-item"><a href="/blog" class="link secondary">Blog</a></li>
                <li class="nav-item"><a href="/contact" class="link">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main id="content">
        <section class="featured" data-type="highlight">
            <article class="post featured-post" data-category="python" data-views="500">
                <h2 class="title"><a href="/posts/python-async">Python Async Deep Dive</a></h2>
                <p class="summary">Master async/await in Python 3.12+.</p>
                <div class="post-meta">
                    <span class="author" data-id="1">Alice</span>
                    <span class="date">2026-01-10</span>
                    <span class="views">500 views</span>
                </div>
                <div class="tags">
                    <a href="/tags/python" class="tag-link">python</a>
                    <a href="/tags/async" class="tag-link">async</a>
                    <a href="/tags/featured" class="tag-link highlight">featured</a>
                </div>
            </article>
        </section>

        <section class="posts" data-type="listing">
            <article class="post" data-category="javascript" data-views="120">
                <h2 class="title"><a href="/posts/js-closures">JS Closures Explained</a></h2>
                <p class="summary">Understanding closures step by step.</p>
                <div class="post-meta">
                    <span class="author" data-id="2">Bob</span>
                    <span class="date">2026-02-05</span>
                </div>
                <div class="tags">
                    <a href="/tags/javascript" class="tag-link">javascript</a>
                    <a href="/tags/closures" class="tag-link">closures</a>
                </div>
            </article>

            <article class="post draft" data-category="rust" data-views="0">
                <h2 class="title"><a href="/posts/rust-ownership">Rust Ownership Model</a></h2>
                <p class="summary">Memory safety without garbage collection.</p>
                <div class="tags">
                    <a href="/tags/rust" class="tag-link">rust</a>
                </div>
            </article>
        </section>

        <aside class="sidebar">
            <div class="widget popular-posts">
                <h3>Popular Posts</h3>
                <ul>
                    <li><a href="/posts/python-async">Python Async</a></li>
                    <li><a href="/posts/js-closures">JS Closures</a></li>
                </ul>
            </div>
            <div class="widget tags-widget">
                <h3>Tags</h3>
                <a href="/tags/python" class="sidebar-tag">python</a>
                <a href="/tags/javascript" class="sidebar-tag">javascript</a>
            </div>
        </aside>
    </main>

    <footer id="site-footer">
        <p class="copyright">&copy; 2026 My Blog</p>
        <p class="powered-by">Powered by <a href="https://example.com" class="external">Example</a></p>
    </footer>
</body>
</html>
"""

soup = BeautifulSoup(HTML, "html.parser")

print("=" * 5, "Basic CSS selectors", "=" * 5)

# Tag selector
articles = soup.select("article")
print(f"Total articles: {len(articles)}")  # 3

# Class selector (.)
featured = soup.select(".featured")
print(f"Featured elements: {len(featured)}")  # section.featured + article.featured-post

# ID selector (#)
logo = soup.select("#logo")
print(f"Logo: {logo[0].string}")  # My Blog

# Descendant selector (space)
titles = soup.select("article .title")
print(f"Article titles: {[t.string for t in titles]}")

# Direct child selector (>)
nav_items = soup.select("ul > li")
print(f"Nav items: {len(nav_items)}")  # 4

# Adjacent sibling selector (+)
second_article = soup.select("article + article")
print(f"Articles with preceding sibling: {len(second_article)}")  # 2

# General sibling selector (~)
siblings_after_h3 = soup.select("h3 ~ *")
print(f"Elements after h3: {len(siblings_after_h3)}")

print("=" * 5, "Attribute selectors", "=" * 5)

# [attr] — has attribute
elements_with_data = soup.select("[data-category]")
print(f"With data-category: {len(elements_with_data)}")  # 3

# [attr=value] — exact match
python_posts = soup.select('[data-category="python"]')
print(f"Python posts: {python_posts[0].h2.a.string}")  # Python Async Deep Dive

# [attr^=value] — starts with
links_to_posts = soup.select('a[href^="/posts"]')
print(f"Links starting with /posts: {len(links_to_posts)}")  # 3

# [attr$=value] — ends with
css_links = soup.select('link[href$=".css"]')
print(f"CSS links: {len(css_links)}")  # 2

# [attr*=value] — contains
links_with_tag = soup.select('a[href*="/tags"]')
print(f"Links containing /tags: {len(links_with_tag)}")  # 6 tag-links + 2 sidebar

# [attr~=value] — word in space-separated list
class_draft = soup.select('[class~="draft"]')
print(f"Draft articles: {len(class_draft)}")  # 1

# [attr|=value] — value or value- (language codes)
# Example: [lang|="en"] matches "en", "en-US", "en-GB"
html_tag = soup.select('[lang|="en"]')
print(f"Lang=en or en-*: {len(html_tag)}")  # 1

print("=" * 5, "Pseudo-classes — :first-child, :last-child, :nth-child", "=" * 5)

# :first-child
first_li = soup.select("ul > li:first-child")
print(f"First li in each ul: {[li.a.string if li.a else li.get_text(strip=True)[:20] for li in first_li]}")

# :last-child
last_li = soup.select("ul > li:last-child")
print(f"Last li in each ul: {[li.a.string if li.a else li.get_text(strip=True)[:20] for li in last_li]}")

# :nth-child(n)
second_li = soup.select("ul.nav-list > li:nth-child(2)")
print(f"Second nav item: {second_li[0].a.string}")

# :nth-child(odd/even)
odd_items = soup.select("ul.nav-list > li:nth-child(odd)")
print(f"Odd nav items: {[li.a.string for li in odd_items]}")

even_items = soup.select("ul.nav-list > li:nth-child(even)")
print(f"Even nav items: {[li.a.string for li in even_items]}")

# :nth-of-type
first_article = soup.select("article:nth-of-type(1)")
print(f"First article of type: {first_article[0].h2.a.string}")

# :only-child
only_h3 = soup.select(".widget h3:only-child")
print(f"h3 as only child: {len(only_h3)}")

print("=" * 5, "Pseudo-classes — :not(), :empty, :has()", "=" * 5)

# :not() — exclude elements
non_draft = soup.select("article:not(.draft)")
print(f"Non-draft articles: {len(non_draft)}")  # 2

# :not() with multiple selectors
non_draft_featured = soup.select("article:not(.draft, .featured-post)")
print(f"Non-draft, non-featured: {len(non_draft_featured)}")  # 1

# :empty — elements with no children
empty_tags = soup.select("li:empty")
print(f"Empty li elements: {len(empty_tags)}")  # 0

# :has() — parent selector (select elements that contain specific children)
articles_with_views = soup.select("article:has(.views)")
print(f"Articles with .views: {len(articles_with_views)}")  # 1

articles_with_highlight_tag = soup.select("article:has(.highlight)")
print(f"Articles with .highlight: {len(articles_with_highlight_tag)}")  # 1

# :has() with descendant
sections_with_article = soup.select("section:has(article)")
print(f"Sections containing article: {len(sections_with_article)}")  # 2

print("=" * 5, "Combinator selectors", "=" * 5)

# Descendant (space): all <a> inside <nav>
nav_links = soup.select("nav a")
print(f"All nav links: {[a.string for a in nav_links]}")

# Child (>): direct children only
direct_nav_links = soup.select("nav > ul > li > a")
print(f"Direct nav links: {[a.string for a in direct_nav_links]}")

# Adjacent sibling (+)
after_h2 = soup.select("h2 + p")
print(f"<p> right after <h2>: {[p.get_text(strip=True)[:40] for p in after_h2]}")

# General sibling (~)
after_h3_sidebar = soup.select("h3 ~ *")
print(f"Elements after <h3> in sidebar: {len(after_h3_sidebar)}")

print("=" * 5, "Multiple selectors and union", "=" * 5)

# Comma-separated selectors (union)
headers = soup.select("h1, h2, h3")
print(f"All headers: {[h.string for h in headers]}")

# Combine class + attribute
featured_python = soup.select("article.featured-post[data-category='python']")
print(f"Featured Python post: {featured_python[0].h2.a.string}")

# Combine tag + :not()
active_nav = soup.select("li.nav-item:not(.active)")
print(f"Non-active nav items: {[li.a.string for li in active_nav]}")

print("=" * 5, "select_one vs select", "=" * 5)

# select() — returns list (possibly empty)
all_posts = soup.select("article.post")
print(f"All posts (select): {len(all_posts)}")

# select_one() — returns first match or None
first_post = soup.select_one("article.post")
print(f"First post (select_one): {first_post.h2.a.string}")

# select_one returns None if no match
missing = soup.select_one(".nonexistent")
print(f"Missing element: {missing}")  # None

print("=" * 5, "Extracting data with CSS selectors", "=" * 5)

# Build structured data from HTML
posts = soup.select("article.post")
data = []
for post in posts:
    title_tag = post.select_one("h2.title a")
    author_tag = post.select_one("span.author")
    date_tag = post.select_one("span.date")
    tags = [a.string for a in post.select("a.tag-link")]
    data.append({
        "title": title_tag.string if title_tag else None,
        "url": title_tag["href"] if title_tag else None,
        "author": author_tag.string if author_tag else None,
        "author_id": author_tag.get("data-id") if author_tag else None,
        "date": date_tag.string if date_tag else None,
        "category": post.get("data-category"),
        "views": int(post.get("data-views", 0)),
        "tags": tags,
        "is_draft": "draft" in post.get("class", []),
    })

for item in data:
    print(f"  {item['title']}: {item['category']} by {item['author']} ({item['views']} views)")
    print(f"    tags={item['tags']}, draft={item['is_draft']}")

print("=" * 5, "Advanced CSS selector patterns", "=" * 5)

# Select elements where class contains a word
all_links_with_class = soup.select("a[class]")
print(f"Links with class attr: {len(all_links_with_class)}")

# Select by multiple classes
featured_tag_links = soup.select("a.tag-link.highlight")
print(f"Highlighted tag links: {[a.string for a in featured_tag_links]}")

# Select by partial href match
all_tag_links = soup.select('a[href^="/tags/"]')
print(f"All tag links: {[a.string for a in all_tag_links]}")

# Select sidebar tags (specific context)
sidebar_tags = soup.select("aside .sidebar-tag")
print(f"Sidebar tags: {[a.string for a in sidebar_tags]}")

# Select external links
external = soup.select("a.external")
print(f"External links: {len(external)}")  # 1

# Select copyright text
copyright_text = soup.select_one(".copyright")
print(f"Copyright: {copyright_text.get_text(strip=True)}")