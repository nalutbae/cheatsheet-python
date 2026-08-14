# BeautifulSoup: parsing, navigation, and tree manipulation

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

# ─────────────────────────────────────────────
# Sample HTML for all examples
# ─────────────────────────────────────────────
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample Page</title>
    <style>body { font-family: sans-serif; }</style>
</head>
<body>
    <!-- Main navigation -->
    <nav id="main-nav" class="navigation">
        <a href="/" class="nav-link active">Home</a>
        <a href="/about" class="nav-link">About</a>
        <a href="/contact" class="nav-link">Contact</a>
    </nav>

    <div id="content" class="main-content" data-role="primary">
        <article class="post" data-category="python" data-views="150">
            <h2 class="title">Python Basics</h2>
            <p class="summary">Learn Python from scratch.</p>
            <div class="tags">
                <span class="tag">beginner</span>
                <span class="tag">python</span>
                <span class="tag highlight">featured</span>
            </div>
            <div class="meta">
                <span class="author">Alice</span>
                <time datetime="2026-01-15">Jan 15, 2026</time>
            </div>
        </article>

        <article class="post" data-category="javascript" data-views="80">
            <h2 class="title">Advanced JavaScript</h2>
            <p class="summary">Deep dive into JS closures.</p>
            <div class="tags">
                <span class="tag">advanced</span>
                <span class="tag">javascript</span>
            </div>
            <div class="meta">
                <span class="author">Bob</span>
                <time datetime="2026-02-20">Feb 20, 2026</time>
            </div>
        </article>

        <article class="post draft" data-category="rust" data-views="0">
            <h2 class="title">Rust for Systems</h2>
            <p class="summary">Memory safety without GC.</p>
            <div class="tags">
                <span class="tag">systems</span>
                <span class="tag">rust</span>
            </div>
        </article>
    </div>

    <footer id="footer">
        <p>&copy; 2026 Example Blog</p>
    </footer>
</body>
</html>
"""

print("=" * 5, "Creating a BeautifulSoup object", "=" * 5)

# Three parsers: html.parser (built-in), lxml (fast), html5lib (lenient)
soup = BeautifulSoup(HTML, "html.parser")

# lxml parser — faster, handles broken HTML better
# soup = BeautifulSoup(HTML, "lxml")

# html5lib parser — most lenient, slowest
# soup = BeautifulSoup(HTML, "html5lib")

print(f"Parser: {soup.parser}")
print(f"Type: {type(soup)}")

# Prettify — format HTML with indentation
print(f"Title tag: {soup.title}")
print(f"Title string: {soup.title.string}")

print("=" * 5, "Navigating the tree — parents, children, siblings", "=" * 5)

# Access specific elements
title_tag = soup.title
print(f"Title: {title_tag}")
print(f"Title parent: {title_tag.parent.name}")  # head
print(f"Title parent's parent: {title_tag.parent.parent.name}")  # html

# Children vs descendants
body = soup.body
print(f"\nBody's direct children (tags only):")
for child in body.children:
    if isinstance(child, Tag):
        print(f"  <{child.name}>")

print(f"\nAll descendants count: {len(list(body.descendants))}")
tag_descendants = [d for d in body.descendants if isinstance(d, Tag)]
print(f"Tag descendants: {len(tag_descendants)}")

# Next/previous siblings
first_article = soup.find("article")
print(f"\nFirst article: {first_article.h2.string}")
next_article = first_article.find_next_sibling("article")
print(f"Next article: {next_article.h2.string}")
prev_article = next_article.find_previous_sibling("article")
print(f"Previous article: {prev_article.h2.string}")

# Next/previous element (including text nodes)
first_link = soup.find("a")
print(f"\nFirst link: {first_link.string}")
print(f"Next sibling link: {first_link.find_next_sibling('a').string}")

print("=" * 5, "Navigating with .next_sibling / .previous_sibling", "=" * 5)

nav = soup.find("nav")
links = nav.find_all("a")
print(f"Nav links: {[link.string for link in links]}")

# next_element / previous_element — any node (text, tag, etc.)
h2 = soup.find("h2")
print(f"\nAfter h2, next element type: {type(h2.next_element).__name__}")
print(f"After h2, next element: {repr(h2.next_element.string or h2.next_element.strip()[:30])}")

print("=" * 5, "Navigating with .parents", "=" * 5)

tag = soup.find("span", class_="highlight")
print(f"Highlight tag: {tag}")
path = " > ".join(parent.name for parent in tag.parents if isinstance(parent, Tag))
print(f"Path to root: {path}")

print("=" * 5, "String and text properties", "=" * 5)

# .string — single text child
print(f"Title .string: {soup.title.string}")
print(f"First h2 .string: {soup.find('h2').string}")

# .strings — all text nodes within a tag
footer = soup.find("footer")
all_text = footer.get_text(separator=" ", strip=True)
print(f"Footer text: {all_text}")

# .get_text() options
article = soup.find("article")
print(f"Article text (strip): {article.get_text(strip=True)[:60]}...")
print(f"Article text (separator): {article.get_text(separator=' | ', strip=True)[:80]}...")

# Get text from specific descendants only
authors = soup.find_all("span", class_="author")
print(f"Authors: {[a.string for a in authors]}")

print("=" * 5, "Modifying the tree", "=" * 5)

# Create new tag
new_tag = soup.new_tag("span", class_="tag new-tag")
new_tag.string = "new"
print(f"New tag: {new_tag}")

# Append to existing element
tags_div = soup.find("div", class_="tags")
tags_div.append(new_tag)
print(f"Tags after append: {[t.string for t in tags_div.find_all('span')]}\n")

# Insert at specific position
second_tag = soup.new_tag("span", class_="tag inserted")
second_tag.string = "inserted"
tags_div.insert(1, second_tag)
print(f"Tags after insert: {[t.string for t in tags_div.find_all('span')]}")

# Replace string
title = soup.find("h2")
title.string.replace_with("Modified Title")
print(f"Modified title: {title.string}")

# Clear all contents
footer = soup.find("footer")
footer_copy = str(footer)  # save before clearing
footer.clear()
print(f"Footer after clear: {footer}")

# Restore footer
footer.append(BeautifulSoup(footer_copy, "html.parser").find("footer").contents[0])

# Decompose — remove tag and its contents entirely
highlight = soup.find("span", class_="highlight")
highlight_text = highlight.string  # save before decompose
highlight.decompose()
print(f"After decompose 'highlight': {highlight_text} removed from tree")

# Unwrap — remove tag but keep contents
tag_new = soup.find("span", class_="tag new-tag")
if tag_new:
    tag_new.unwrap()
    print(f"After unwrap 'new-tag': tag removed, text preserved")

print("=" * 5, "Extracting and replacing attributes", "=" * 5)

article = soup.find("article")
print(f"Article classes: {article.get('class')}")
print(f"Article data-category: {article.get('data-category')}")
print(f"Article data-views: {article.get('data-views')}")
print(f"Non-existent attr: {article.get('data-missing', 'default')}")

# Modify attributes
article["data-views"] = "200"
print(f"Updated data-views: {article['data-views']}")

# Remove attribute
del article["data-views"]
print(f"After deletion: {article.get('data-views', 'removed')}")

# Multi-valued attributes (class)
nav = soup.find("nav")
print(f"Nav classes: {nav.get('class')}")
nav["class"].append("sticky")
print(f"After append: {nav.get('class')}")

# Check attribute existence
print(f"Has href?: {soup.find('a').has_attr('href')}")  # True
print(f"Has data-views?: {article.has_attr('data-views')}")  # False (deleted)

print("=" * 5, "Working with comments and processing instructions", "=" * 5)

# Find HTML comments
for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
    print(f"Comment: {comment.strip()}")

# Extract and replace
first_comment = soup.find(string=lambda text: isinstance(text, Comment))
print(f"First comment: {first_comment.strip()}")

print("=" * 5, "Encoding and output", "=" * 5)

# Different output formats
print(f"prettify (first 200 chars):\n{soup.prettify()[:200]}...")

# Get specific element's HTML
article = soup.find("article")
print(f"\nOuter HTML: {str(article)[:100]}...")
print(f"Inner HTML: {article.decode_contents()[:100]}...")

# Encode to bytes
print(f"Encoded: {len(soup.encode('utf-8'))} bytes (UTF-8)")
print(f"Encoded: {len(soup.encode('ascii'))} bytes (ASCII)")