# lxml: XPath, CSS selectors, and high-performance XML/HTML parsing

from lxml import etree, html
from lxml.cssselect import CSSSelector

HTML = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Page</title>
</head>
<body>
    <div id="app" class="container">
        <header class="site-header" data-section="top">
            <h1 id="logo" class="brand large">My Site</h1>
            <nav id="main-nav" class="navigation">
                <a href="/" class="link active">Home</a>
                <a href="/about" class="link">About</a>
                <a href="/blog" class="link">Blog</a>
                <a href="/contact" class="link">Contact</a>
            </nav>
        </header>

        <main id="content" class="main-content" data-role="primary">
            <section class="featured">
                <article id="post-1" class="post python featured" data-category="python" data-views="500">
                    <h2 class="title">Python Async Patterns</h2>
                    <p class="summary">Deep dive into async/await.</p>
                    <div class="meta">
                        <span class="author" data-id="u1">Alice</span>
                        <time datetime="2026-01-15">Jan 15, 2026</time>
                    </div>
                    <div class="tags">
                        <a href="/tags/python" class="tag">python</a>
                        <a href="/tags/async" class="tag">async</a>
                    </div>
                </article>

                <article id="post-2" class="post javascript" data-category="javascript" data-views="120">
                    <h2 class="title">JS Closures</h2>
                    <p class="summary">Understanding closures.</p>
                    <div class="meta">
                        <span class="author" data-id="u2">Bob</span>
                        <time datetime="2026-02-20">Feb 20, 2026</time>
                    </div>
                    <div class="tags">
                        <a href="/tags/javascript" class="tag">javascript</a>
                        <a href="/tags/closures" class="tag">closures</a>
                    </div>
                </article>
            </section>

            <aside class="sidebar">
                <div class="widget popular" data-widget="popular">
                    <h3>Popular Posts</h3>
                    <ul>
                        <li><a href="/posts/1">Python Async</a></li>
                        <li><a href="/posts/2">JS Closures</a></li>
                    </ul>
                </div>
            </aside>
        </main>

        <footer class="site-footer">
            <p>&copy; 2026 My Site</p>
        </footer>
    </div>
</body>
</html>
"""

print("=" * 5, "Parsing HTML with lxml", "=" * 5)

# Parse HTML (automatically handles broken HTML)
doc = html.fromstring(HTML)
print(f"Root tag: {doc.tag}")  # html

# Parse from string with HTMLParser
parser = etree.HTMLParser()
tree = etree.fromstring(HTML.encode("utf-8"), parser)
print(f"Tree root: {tree.tag}")  # html

# Parse from bytes/str
doc2 = html.document_fromstring(HTML)
print(f"Document root: {doc2.tag}")  # html

print("=" * 5, "XPath — basic path expressions", "=" * 5)

# Absolute path
titles = doc.xpath("//h2")
print(f"All h2: {[t.text for t in titles]}")

# Relative path from element
header = doc.xpath("//header")[0]
nav_links = header.xpath(".//a")
print(f"Nav links in header: {[a.text for a in nav_links]}")

# Direct children only
children = doc.xpath("//nav/*")
print(f"Direct children of nav: {[c.tag for c in children]}")

# Parent
parent = doc.xpath("//h2/..")
print(f"Parent of h2: {[p.get('class', p.tag) for p in parent]}")

print("=" * 5, "XPath — predicates and conditions", "=" * 5)

# By index (1-based!)
first_article = doc.xpath("//article[1]")
print(f"First article: {first_article[0].get('id')}")

# Last
last_article = doc.xpath("//article[last()]")
print(f"Last article: {last_article[0].get('id')}")

# Position
second_article = doc.xpath("//article[position()=2]")
print(f"Second article: {second_article[0].get('id')}")

# By attribute value
python_post = doc.xpath("//article[@data-category='python']")
print(f"Python post: {python_post[0].get('id')}")

# By id
logo = doc.xpath("//*[@id='logo']")
print(f"Logo text: {logo[0].text}")

# Attribute contains
tags_with_href = doc.xpath("//a[contains(@href, '/tags')]")
print(f"Links with /tags in href: {len(tags_with_href)}")

# Starts with
links_starting_posts = doc.xpath("//a[starts-with(@href, '/posts')]")
print(f"Links starting with /posts: {len(links_starting_posts)}")

# Multiple conditions (AND)
python_featured = doc.xpath("//article[@data-category='python' and contains(@class, 'featured')]")
print(f"Python + featured: {python_featured[0].get('id')}")

# Multiple conditions (OR)
python_or_js = doc.xpath("//article[@data-category='python' or @data-category='javascript']")
print(f"Python or JavaScript: {[a.get('id') for a in python_or_js]}")

print("=" * 5, "XPath — text() and string manipulation", "=" * 5)

# text() — get text nodes
all_texts = doc.xpath("//h2/text()")
print(f"h2 texts: {[t.strip() for t in all_texts]}")

# string() — concatenate all text in element
article_text = doc.xpath("string(//article[@id='post-1'])")
print(f"Article 1 full text (first 80): {article_text.strip()[:80]}...")

# normalize-space — strip and collapse whitespace
nav_text = doc.xpath("normalize-space(//nav)")
print(f"Nav text normalized: {nav_text[:60]}...")

# concat
concat_text = doc.xpath("concat(//h1/text(), ' - ', //h2[1]/text())")
print(f"Concat: {concat_text}")

print("=" * 5, "XPath — numeric and comparison operators", "=" * 5)

# Greater than (attribute is string, need number())
high_views = doc.xpath("//article[number(@data-views) > 100]")
print(f"Articles with views > 100: {[a.get('id') for a in high_views]}")

# Less than or equal
low_views = doc.xpath("//article[number(@data-views) <= 120]")
print(f"Articles with views <= 120: {[a.get('id') for a in low_views]}")

# Count
article_count = doc.xpath("count(//article)")
print(f"Article count: {int(article_count)}")  # 2.0 → 2

# Sum (with number conversion)
views_sum = doc.xpath("sum(//article/@data-views)")
print(f"Total views: {int(views_sum)}")

print("=" * 5, "XPath — axes (advanced traversal)", "=" * 5)

# ancestor
ancestors = doc.xpath("//span[@class='author']/ancestor::*")
print(f"Author ancestors: {[a.tag for a in ancestors]}")

# ancestor-or-self
ancestors_self = doc.xpath("//span[@class='author']/ancestor-or-self::*")
print(f"Author ancestors-or-self: {[a.tag for a in ancestors_self]}")

# descendant
descendants = doc.xpath("//section[@class='featured']/descendant::a")
print(f"Featured section links: {[a.text for a in descendants]}")

# following-sibling
following = doc.xpath("//article[1]/following-sibling::article")
print(f"Articles after first: {[a.get('id') for a in following]}")

# preceding-sibling
preceding = doc.xpath("//article[last()]/preceding-sibling::article")
print(f"Articles before last: {[a.get('id') for a in preceding]}")

# following (all nodes after in document order)
following_all = doc.xpath("//header/following::*")
print(f"All elements after header: {len(following_all)}")

# child
children = doc.xpath("//nav/child::*")
print(f"Nav children: {[c.tag for c in children]}")

print("=" * 5, "XPath — functions", "=" * 5)

# contains() on text
python_refs = doc.xpath("//a[contains(text(), 'Python')]")
print(f"Links containing 'Python': {[a.text for a in python_refs]}")

# contains() on class
featured_els = doc.xpath("//*[contains(@class, 'featured')]")
print(f"Elements with 'featured' class: {len(featured_els)}")

# not()
non_posts = doc.xpath("//article[not(contains(@class, 'featured'))]")
print(f"Non-featured articles: {[a.get('id') for a in non_posts]}")

# name()
all_tags = doc.xpath("//*[name()='article']")
print(f"Elements named 'article': {len(all_tags)}")

# local-name() (useful with namespaces)
print(f"Local name of root: {doc.xpath('local-name(/*)')}")

# string-length
long_titles = doc.xpath("//h2[string-length(text()) > 15]")
print(f"Titles longer than 15 chars: {[t.text for t in long_titles]}")

print("=" * 5, "XPath — extracting attributes and values", "=" * 5)

# Get single attribute
href = doc.xpath("//a[@class='link active']/@href")[0]
print(f"Active link href: {href}")

# Get all hrefs
all_hrefs = doc.xpath("//nav/a/@href")
print(f"All nav hrefs: {all_hrefs}")

# Get all data-attributes
data_attrs = doc.xpath("//article/@data-category")
print(f"Data categories: {data_attrs}")

# Build structured data
articles = doc.xpath("//article")
for article in articles:
    aid = article.get("id")
    title = article.xpath(".//h2/text()")[0]
    category = article.get("data-category")
    views = article.get("data-views")
    author = article.xpath(".//span[@class='author']/text()")[0]
    tags = article.xpath(".//a[@class='tag']/text()")
    print(f"  {aid}: '{title}' by {author} [{category}] {views}v tags={tags}")

print("=" * 5, "CSS selectors with lxml.cssselect", "=" * 5)

# lxml supports CSS selectors via cssselect
# CSSSelector compiles CSS to XPath internally

# Basic CSS selectors
sel = CSSSelector("article.post")
articles = sel(doc)
print(f"CSS article.post: {len(articles)}")

# ID selector
sel = CSSSelector("#logo")
logo = sel(doc)
print(f"CSS #logo: {logo[0].text}")

# Class selector
sel = CSSSelector(".featured")
featured = sel(doc)
print(f"CSS .featured: {len(featured)}")

# Attribute selector
sel = CSSSelector('article[data-category="python"]')
python = sel(doc)
print(f'CSS article[data-category="python"]: {python[0].get("id")}')

# Descendant
sel = CSSSelector("article .tag")
tags = sel(doc)
print(f"CSS article .tag: {[t.text for t in tags]}")

# Direct child
sel = CSSSelector("nav > a")
direct = sel(doc)
print(f"CSS nav > a: {[a.text for a in direct]}")

# Pseudo-class
sel = CSSSelector("article:first-child")
first = sel(doc)
print(f"CSS article:first-child: {first[0].get('id')}")

# :not()
sel = CSSSelector("article:not(.draft)")
non_draft = sel(doc)
print(f"CSS article:not(.draft): {len(non_draft)}")

# Multiple selectors
sel = CSSSelector("h1, h2, h3")
headers = sel(doc)
print(f"CSS h1, h2, h3: {[h.text for h in headers]}")

print("=" * 5, "lxml tree manipulation and serialization", "=" * 5)

# Create new element
new_tag = etree.Element("span")
new_tag.set("class", "tag new")
new_tag.text = "new"
print(f"New element: {etree.tostring(new_tag, encoding='unicode')}")

# Append to existing
tags_div = doc.xpath("//div[@class='tags']")[0]
tags_div.append(new_tag)
print(f"After append: {etree.tostring(tags_div, encoding='unicode', method='html')[:120]}...")

# Insert at position
another_tag = etree.Element("span")
another_tag.set("class", "tag inserted")
another_tag.text = "inserted"
tags_div.insert(0, another_tag)
print(f"After insert: {etree.tostring(tags_div, encoding='unicode', method='html')[:120]}...")

# Remove element
tags_div.remove(another_tag)
print(f"After remove: {len(tags_div)} children")

# Serialize to string
html_str = etree.tostring(doc, encoding="unicode", method="html", pretty_print=True)
print(f"\nSerialized HTML (first 200 chars):\n{html_str[:200]}...")

# Serialize to bytes
html_bytes = etree.tostring(doc, encoding="utf-8", method="html")
print(f"\nSerialized bytes length: {len(html_bytes)}")

print("=" * 5, "lxml vs BeautifulSoup — when to use which", "=" * 5)

print("Use lxml directly when:")
print("  - Parsing XML/XSLT/SVG")
print("  - Need XPath 1.0 queries")
print("  - Performance is critical (10-100x faster)")
print("  - Working with large documents")
print("  - Need strict validation (DTD, XML Schema)")
print()
print("Use BeautifulSoup when:")
print("  - Parsing messy/broken HTML from the web")
print("  - Need simpler API (find/find_all)")
print("  - Want lenient error handling")
print("  - Prefer Pythonic API over XPath syntax")
print()
print("Combine both (best of both worlds):")
print("  - soup = BeautifulSoup(html, 'lxml')  # lxml parser + BS4 API")
print("  - Fast parsing + easy API")