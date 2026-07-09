import re

# Fix news/index.html
with open('C:/docs/mysite/news/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove duplicate footer
duplicate_footer = '''</div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>© 2026 Yehor Franchuk. All rights reserved.</p>
        </div>
    </footer>

    <script src="../scripts.js"></script>
</body>
</html>'''

if html.count(duplicate_footer) > 1:
    html = html.replace(duplicate_footer, '', 1)

# 2. KSE: object-fit: contain
# Find KSE section
def replace_kse(m):
    return m.group(0).replace('object-fit: cover;', 'object-fit: contain;')
html = re.sub(r'(<h2>KSE &amp; Genesis MVP Camp Winter School</h2>.*?</section>)', replace_kse, html, flags=re.DOTALL)

# 3. Remove border from CRABS bottom photo (cr2.jpg)
# Find CRABS section
def replace_crabs(m):
    return m.group(0).replace('class="img-fluid rounded border border-secondary"', 'class="img-fluid rounded"')
html = re.sub(r'(<h2>Bioinformatics School CRABS 2025</h2>.*?</section>)', replace_crabs, html, flags=re.DOTALL)

# 4. Remove border from Explogen bottom photo (ce2.jpg)
def replace_explogen(m):
    return m.group(0).replace('class="img-fluid rounded border border-secondary"', 'class="img-fluid rounded"')
html = re.sub(r'(<h2>Explogen LLC &amp; Bacterial Conjugation</h2>.*?</section>)', replace_explogen, html, flags=re.DOTALL)

with open('C:/docs/mysite/news/index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Fix index.html profile photo
with open('C:/docs/mysite/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()
index_html = index_html.replace('<img src="your-photo.jpg" alt="Yehor Franchuk" class="profile-footer-photo">',
                                '<img src="new1.jpg" alt="Yehor Franchuk" class="profile-footer-photo">')
with open('C:/docs/mysite/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)


# Fix styles.css for burger menu
with open('C:/docs/mysite/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make burger menu relative and high z-index
css = css.replace('.burger-menu {\n    display: none;', '.burger-menu {\n    display: none;\n    position: relative;\n    z-index: 10001;')

# Make nav-links high z-index when on mobile
css = css.replace('.nav-links {\n        display: none;', '.nav-links {\n        display: none;\n        z-index: 10000;')

with open('C:/docs/mysite/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('All fixes applied!')
