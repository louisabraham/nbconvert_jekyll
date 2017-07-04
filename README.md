# nbconvert_jekyll

This extension for [Jupyter nbconvert ](https://github.com/jupyter/nbconvert) is useful when you manage a blog with Jekyll (for example on Github pages).

* It uses some [metadata](https://nbformat.readthedocs.io/en/latest/format_description.html#metadata) fields of the notebook (you can change them under "Edit" > "Edit Notebook Metadata") to fill the YAML [frontmatter](https://jekyllrb.com/docs/frontmatter/) of Jekyll:
  - If 'title' is defined, it is used for the 'title' field. You may have some issues if the title contains double quotation marks (`"`). It also changes the html title of the page.
  - If 'date' is defined, it is used for the 'date' field for Jekyll. As writted in the doc: "A date is specified in the format YYYY-MM-DD HH:MM:SS +/-TTTT; hours, minutes, seconds, and timezone offset are optional.".

* It adds a Liquid template (the templating system used by Jekyll) for Google Analytics that is activated if you define `google_analytics` in `_config.yml` (it works like that in the Github Themes).

  ## Installation
    
  `git clone https://github.com/louisabraham/nbconvert_jekyll`
  
  `pip install --upgrade nbconvert_jekyll`
  
  ## How to use
  
  `jupyter nbconvert file.ipynb --to jekyll`
  
