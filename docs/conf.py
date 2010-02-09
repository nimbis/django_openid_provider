# -*- coding: utf-8 -*-
#

templates_path = ['.templates']

source_suffix = '.rst'
source_encoding = 'utf-8'

master_doc = 'index'

project = 'Django OpenID Provider'
_author = u"Roman Barczyński"
copyright = u"2010, %s" % _author

pygments_style = 'sphinx'


html_style = 'default.css'
html_title =  "%s documentation" % (project)
html_static_path = ['.static']
html_last_updated_fmt = '%b %d, %Y'

html_use_modindex = False
html_use_index = False
html_copy_source = False
html_file_suffix = '.html'

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  (master_doc, 'openid_provider.tex', '%s Documentation' % project, _author, 'manual'), # or 'howto'
]

latex_elements = {
	'papersize': 'a4paper,oneside',
	'fncychap': '\\usepackage{fancyhdr}'
}

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
