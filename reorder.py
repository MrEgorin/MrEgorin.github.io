import re

html_path = 'C:/docs/mysite/news/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

missing_blocks = {
    '20th All-Ukrainian Conference of Young Scientists of IMBG': """<section class="glass-panel mb-4">
                    <h2>20th All-Ukrainian Conference of Young Scientists of IMBG</h2>
                    <p class="timeline-date">May 2026 | Kyiv, Ukraine</p>
                    <p>
                        I presented at the <strong>20th All-Ukrainian Conference of Young Scientists of the Institute of Molecular Biology and Genetics, NAS of Ukraine</strong>, on the topic <em>“Structure-oriented design of small molecules as potential inhibitors of the long non-coding RNA ANRASSF1.”</em>
                    </p>
                    <p>
                        Today, determining the structure of long non-coding RNAs is a real challenge; computational methods rarely yield high-quality results. The use of various software tools and molecular dynamics simulations allows for the generation of an acceptable model with high-quality geometry. Docking evaluation functions for RNA are often still in beta testing within specialized software, but nevertheless already allow for the accurate assessment of RNA electrostatics and the refinement of RNA-ligand binding free energy using MMGBSA or FEP methods.
                    </p>
                    <p style="font-weight: 500; color: var(--accent-cyan);">
                        #FEP #RNA #ligand #CADD #drugdesign #prostate #cancer
                    </p>
                    <div class="row justify-content-center mt-3">
                        <div class="col-md-6 text-center">
                            <img src="../i1.jpg" alt="IMBG Conference presentation slide" class="gallery-photo">
                        </div>
                    </div>
                </section>""",
    'Kyiv IT Cluster: CADD Integration in HealthTech': """<section class="glass-panel mb-4">
                    <h2>Kyiv IT Cluster: CADD Integration in HealthTech</h2>
                    <p class="timeline-date">May 2026 | Kyiv, Ukraine</p>
                    <p>
                        The FAZENA team recently visited the <strong>Kyiv IT Cluster</strong>. We engaged in productive discussions regarding the integration of advanced technology in healthcare and shared our progress in Computer-Aided Drug Design (CADD). As we continue to develop scalable solutions for accelerated drug discovery, collaborations within the tech ecosystem remains a core driver of our growth.
                    </p>
                    <p>
                        Thank you to the Kyiv School of Economics for this opportunity.
                    </p>
                    <p style="font-weight: 500; color: var(--accent-cyan);">
                        #FAZENA #KyivITCluster #DrugDesign #Biotech #CADD #Bioinformatics #DeepTech #HealthTech #Innovation
                    </p>
                    <div class="row justify-content-center mt-3">
                        <div class="col-md-6 text-center">
                            <img src="../i2.jpg" alt="Kyiv IT Cluster Visit" class="gallery-photo">
                        </div>
                    </div>
                </section>""",
    'Completion of Igor Sikorsky KPI Startup School (Season 13)': """<section class="glass-panel mb-4">
                    <h2>Completion of Igor Sikorsky KPI Startup School (Season 13)</h2>
                    <p class="timeline-date">April 2026 | Kyiv, Ukraine</p>
                    <p>
                        Our team successfully completed the 13th season of the <strong>КПІ ім. Ігоря Сікорського Startup School</strong>. We plan to participate in the “Sikorsky Challenge UK” (September 2026) and the “Sikorsky Challenge” (October 2026).
                    </p>
                    <p>
                        We have presented <strong>RNA Hunter</strong>, a platform for designing drugs that target regulatory RNAs. Naturally, the product currently offers only basic functionality, and modern technology is constantly evolving. We will continue to grow alongside our product.
                    </p>
                    <p class="text-center mt-3">
                        <a href="https://lnkd.in/dEp7Z_8q" target="_blank" class="nav-button">View Graduation Update ↗</a>
                    </p>
                    <div class="row justify-content-center mt-3">
                        <div class="col-md-6 text-center">
                            <img src="../i3.jpg" alt="KPI Startup School Graduation" class="gallery-photo">
                        </div>
                    </div>
                </section>"""
}

order = [
    '20th All-Ukrainian Conference of Young Scientists of IMBG',
    'KSE Startup Ecosystem Vol. 3 Demo Day',
    'Kyiv IT Cluster: CADD Integration in HealthTech',
    'Completion of Igor Sikorsky KPI Startup School (Season 13)',
    '9th Advanced in Silico Drug Design Workshop 2026',
    '27th Bologna Winter School on Bioinformatics and Rare Diseases',
    'KSE & Genesis MVP Camp Winter School',
    'Google DevFest 2025',
    'First Place in the NeuroImpact Challenge 2025',
    'BioGENext Lecture: Prof. Janusz M. Bujnicki',
    'BioGENext Series 2: Fluorescence Imaging',
    'Bioinformatics School CRABS 2025',
    'Explogen LLC & Bacterial Conjugation',
    '20th International Summer School "Molecular Biology, Biotechnology and Biomedicine"',
    'Uzhhorod Bioinformatics & Data Science Summer School (UBDS³)',
    'Illumina Day 2025',
    'Lectures by BioGENex',
    'Ukrainian School in Evolutionary Biology (USEB2025)',
    'Genome Editing using CRISPR/Cas System'
]

dates = [
    'May 2026 | Kyiv, Ukraine',
    'May 2026 | Kyiv School of Economics',
    'May 2026 | Kyiv, Ukraine',
    'April 2026 | Kyiv, Ukraine',
    'February 2026 | Prague, Czech Republic',
    'February 2026 | Università di Bologna, Italy',
    'December 2025 | Kyiv, Ukraine',
    'December 2025 | GDG Kyiv, Ukraine',
    'December 2025 | Ministry of Education and Science of Ukraine',
    'November 2025 | Kyiv, Ukraine',
    'October 2025 | Kyiv, Ukraine',
    'August 2025 | Kyiv School of Economics',
    'August 2025 | Carpathian Mountains, Ukraine',
    'June-July 2025 | Odesa I.I.Mechnikov National University',
    'June 2025 | Uzhhorod National University',
    'April 2025 | Kyiv, Ukraine',
    'March 2025 | Kyiv, Ukraine',
    'February 2025 | V.N. Karazin Kharkiv National University & Uzhhorod National University',
    'December 2024 | YP Biotech'
]

# extract main section
main_start = html.find('<!-- 1. ')
if main_start == -1:
    main_start = html.find('<main')
    main_start = html.find('<section', main_start)
    
main_end = html.find('</div>\n        </div>\n    </main>')

sections_html = html[main_start:main_end]

sections = re.findall(r'(<section.*?</section>)', sections_html, flags=re.DOTALL)

blocks_by_title = {}
for s in sections:
    match = re.search(r'<h2>(.*?)</h2>', s)
    if match:
        title = match.group(1).replace('&amp;', '&')
        # match strictly
        for ot in order:
            if title.strip() == ot.strip():
                blocks_by_title[ot] = s
                break
        else:
            print("No match for:", title)

# add missing blocks back in
for missing_title, missing_html in missing_blocks.items():
    if missing_title not in blocks_by_title:
        blocks_by_title[missing_title] = missing_html

new_sections_html = ''
for i, ot in enumerate(order):
    if ot not in blocks_by_title:
        print('Missing block for', ot)
        continue
    content = blocks_by_title[ot]
    
    # fix date
    content = re.sub(r'<p class=\"timeline-date\">.*?</p>', f'<p class=\"timeline-date\">{dates[i]}</p>', content, count=1)
    
    # adjust images for CRABS and Explogen
    if 'CRABS 2025' in ot or 'Explogen LLC' in ot:
        content = content.replace('object-fit: cover;', 'object-fit: contain;')
        
    new_sections_html += f'<!-- {i+1}. {ot} -->\n{content}\n\n'

new_html = html[:main_start] + new_sections_html + html[main_end:]
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Done successfully')
