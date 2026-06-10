SITENAME = "RNA Design"
AUTHOR = "Michael T. Wolfinger"
SITEURL = ""
THEME = "themes/rnadesign"
PAGE_SAVE_AS = "{slug}.html"
PAGE_URL = "{slug}.html"
TIMEZONE = "Europe/Vienna"
DEFAULT_LANG = "en"
DISPLAY_PAGES_ON_MENU = False

PATH = 'content'
IGNORE_FILES = ['.#*', '.venv*', '__pycache__', 'node_modules']

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GOOGLE_SCHOLAR_URL = "https://scholar.google.at/citations?user=w0PHGnEAAAAJ&hl=en"
CONTACT_EMAIL      = "michael.wolfinger@univie.ac.at"

EXPERTISE = [
    "ViennaRNA",
    "RNA Structure Prediction",
    "RNA Folding Kinetics",
    "Co-transcriptional Folding",
    "Energy Landscape Modeling",
    "Kinetic RNA Design",
    "De novo xrRNA Design",
    "Viral RNA Structure",
    "Flavivirus Bioinformatics",
    "AI-assisted RNA Design",
]

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME':       {'path': 'CNAME'},
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/robots.txt':  {'path': 'robots.txt'},
}

PLUGINS = ['pelican.plugins.sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes':  0.5,
        'pages':    0.8,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes':  'monthly',
        'pages':    'monthly',
    },
}

PUBLICATIONS_FULL = [
    {
        "year": "2026",
        "title": "Rational design of mechanically active RNAs: de novo engineering of functional exoribonuclease-resistant RNAs",
        "authors": "Jule Walter, Leonhard Sidl, Katrin Gutenbrunner, Denis Skibinski, Tim Kolberg, Ivo L. Hofacker, Hua-Ting Yao, Mario Mörl, <strong>Michael T. Wolfinger</strong>",
        "journal": "Nucleic Acids Res.",
        "citation": "54(9):gkag473 (2026)",
        "doi_url": "https://doi.org/10.1093/nar/gkag473",
        "doi_text": "10.1093/nar/gkag473",
        "type": "Journal article",
        "summary": "This paper reports the rational, de novo engineering of functional exoribonuclease-resistant RNAs (xrRNAs), establishing sequence–structure design principles that link mechanical RNA topology to XRN1 resistance and expanding the toolkit for programmable synthetic RNA biology.",
    },
    {
        "year": "2025",
        "title": "Identification of conserved RNA regulatory switches in living cells using RNA secondary structure ensemble mapping and covariation analysis",
        "authors": "Ivana Borovská, Chundan Zhang, Sarah-Luisa J. Dülk, Edoardo Morandi, Marta F. S. Cardoso, Billal M. Bourkia, Daphne A. L. van den Homberg, <strong>Michael T. Wolfinger</strong>, Willem A. Velema, Danny Incarnato",
        "journal": "Nature Biotechnology",
        "citation": "(2025)",
        "doi_url": "https://doi.org/10.1038/s41587-025-02739-0",
        "doi_text": "10.1038/s41587-025-02739-0",
        "type": "Journal article",
        "summary": "This paper reports the discovery of conserved RNA regulatory switches in living cells by integrating RNA secondary structure ensemble mapping with covariation analysis, revealing structural elements that control gene expression at the RNA level.",
    },
    {
        "year": "2025",
        "title": "From structure to function: Computational insights into Musashi-RNA complexes in the context of viral pathogenesis",
        "authors": "Nitchakan Darai, Leonhard Sidl, Thanyada Rungrotmongkol, Peter Wolschann, <strong>Michael T. Wolfinger</strong>",
        "journal": "Science Asia",
        "citation": "51S(1) 2025s013:1–10 (2025)",
        "doi_url": "https://doi.org/10.2306/scienceasia1513-1874.2025.s013",
        "doi_text": "10.2306/scienceasia1513-1874.2025.s013",
        "type": "Review article",
        "summary": "This paper reviews computational and structural insights into Musashi–RNA complexes, emphasising how Musashi proteins interact with viral RNAs to modulate replication and pathogenesis, and exploring implications for antiviral strategies and synthetic biology.",
    },
    {
        "year": "2025",
        "title": "KinPFN: Bayesian approximation of RNA folding kinetics using prior-data fitted networks",
        "authors": "Dominik Scheuer, Frederic Runge, Jörg K.H. Franke, Michael T. Wolfinger, Christoph Flamm, Frank Hutter",
        "journal": "ICLR 2025",
        "citation": "The Thirteenth International Conference on Learning Representations (2025)",
        "doi_url": "https://doi.org/10.5281/zenodo.15233965",
        "doi_text": "10.5281/zenodo.15233965",
        "type": "Conference article",
        "summary": "This paper presents KinPFN, a deep-learning method based on prior-data fitted networks that approximates RNA folding-time distributions from only a few simulated examples, enabling orders-of-magnitude faster and accurate modelling of RNA folding kinetics and related biological processes.",
    },
    {
        "year": "2025",
        "title": "Bayesian approximation of RNA folding times",
        "authors": "Dominik Scheuer, Frederic Runge, Jörg K.H. Franke, Michael T. Wolfinger, Christoph Flamm, Frank Hutter",
        "journal": "ICLR 2025 Workshop on AI for Nucleic Acids",
        "citation": "(2025)",
        "doi_url": "https://doi.org/10.5281/zenodo.15228717",
        "doi_text": "10.5281/zenodo.15228717",
        "type": "Conference article",
        "summary": "This paper highlights the methodological foundations of KinPFN by detailing its synthetic prior design and in-context learning strategy, and demonstrates how these innovations enable rapid, accurate approximation of RNA folding-time distributions as a lightweight extension to existing kinetic simulators.",
    },
    {
        "year": "2024",
        "title": "Pan-flavivirus analysis reveals sfRNA-independent, 3’UTR-biased siRNA production from an insect-specific flavivirus",
        "authors": "Benoit Besson, Gijs J. Overheul, <strong>Michael T. Wolfinger</strong>, Sandra Junglen, Ronald P. van Rij",
        "journal": "Journal of Virology",
        "citation": "e01215-24 (2024)",
        "doi_url": "https://doi.org/10.1128/jvi.01215-24",
        "doi_text": "10.1128/jvi.01215-24",
        "type": "Journal article",
        "summary": "This paper shows that mosquito-specific flaviviruses, such as Kamiti River virus, exploit their unusually long RNA tail to drive a distinct small-RNA immune reaction in mosquitoes, pointing to a novel way these viruses interact with insect hosts.",
    },
]

# First three entries drive the homepage teaser
PUBLICATIONS = [
    {
        "year": pub["year"],
        "title": pub["title"],
        "journal": pub["journal"],
    }
    for pub in PUBLICATIONS_FULL[:3]
]
