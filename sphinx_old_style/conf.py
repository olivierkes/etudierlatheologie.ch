# -*- coding: utf-8 -*-

import sys, os

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Étudier la théologie (?)'
copyright = u'2011, Nicolas Friedli'
version = '0.9.3'
release = '0.9.3'
language = 'fr'
today_fmt = '%d.%m.%Y'
exclude_patterns = ['_build']

html_theme = 'elt'
html_theme_path = ['_themes']
html_title = u'Étudier la théologie'
html_logo = '_static/etudier-theologie.png'
html_favicon = '_static/favicon.ico'
html_static_path = ['_static']
html_last_updated_fmt = '%d.%m.%Y'
html_use_index = True
html_show_sourcelink = False
html_show_copyright = True
html_use_opensearch = 'http://www.etudierlatheologie.ch'
htmlhelp_basename = 'etudierlathologiedoc'

latex_paper_size = 'a4'
latex_font_size = '11pt'
latex_documents = [
  ('index', 'etudierlathologie.tex', u'Étudier la théologie (?)',
   u'Nicolas Friedli', 'manual'),
]

epub_title = u'Étudier la théologie (?)'
epub_author = u'Nicolas Friedli'
epub_publisher = u'Nicolas Friedli'
epub_copyright = u'2011, Nicolas Friedli'
epub_identifier = 'http://www.etudierlatheologie.ch'

# rst_epilog = """
# .. |pub| raw:: html
# 
#     <script type="text/javascript"><!--
#     google_ad_client = "ca-pub-5977407574976624";
#     /* etudierlatheologie horizontal */
#     google_ad_slot = "8526856721";
#     google_ad_width = 468;
#     google_ad_height = 60;
#     //-->
#     </script>
#     <script type="text/javascript"
#     src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
#     </script>
# """
