#!/usr/bin/env python3

import json
import os
import openpyxl
from html import escape
import string

wookbook = openpyxl.load_workbook("data/conference_meta_data_liu_epress.xlsx")
worksheet = wookbook.active

from unidecode import unidecode

with open("data/sessions.json") as fin:
  data = json.load(fin)

try:
  os.mkdir("proceedings/sessions")
except FileExistsError:
  pass
try:
  os.mkdir("proceedings/authors")
except FileExistsError:
  pass

all_authors = {}
all_bibtex = [
"""
@InProceedings{modelica2021,
  doi = {10.3384/ecp21181},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\\"{o}ping, Sweden},
  editor = {Martin Sjölund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Linköping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Linköping University Electronic Press},
  year = {2021}
}
""".strip()
]

paperNum=2

lastNames = dict()
for i in range(1, worksheet.max_row):
  lastName = worksheet[i][1].value.split(" and ")[0].split(",")[0].split(" ")[-1]
  if lastName in lastNames:
    lastNames[lastName] = 0
  else:
    lastNames[lastName] = None

with open("proceedings/sessions.md", "w") as fout_sessions:
  for session in data:
    num = session["session_number"].split(" ")[1]
    fout_sessions.write('* [%s - %s](/proceedings/sessions/%s)\n' % (session["session_number"],session["session_name"],num))
    with open("proceedings/sessions/%s.md" % num, "w") as fout_session:
      fout_session.write("## %s - %s\n" % (session["session_number"],session["session_name"]))
      for i in range(1,6):
        if "title%d" % i not in session:
          break
        allAuthors = session["author%d" % i]
        authors = allAuthors.replace(" and ", ", ").split(", ")
        if (worksheet[paperNum][1].value != allAuthors):
          raise Exception("\n%s\n%s" % (worksheet[paperNum][1].value, session["author%d" % i]))
        abstract = worksheet[paperNum][5].value
        keywords = worksheet[paperNum][6].value
        numPages = int(worksheet[paperNum][4].value)
        firstPage = int(worksheet[paperNum][7].value)
        lastPage = firstPage + numPages - 1
        firstAuthorLastName = authors[0].split(" ")[-1]

        paper_html = ""
        paper_html += "<table>"
        paper_html += '<tr><th>Title:</th>\n'
        paper_html += '<td>%s</td>\n' % session["title%d" % i]
        paper_html += '</tr>\n'
        paper_html += "<tr><th>Authors:</th>\n<td>\n"
        for author in authors[:-2]:
          paper_html += '<a href="/proceedings/authors/%s">%s</a>, ' % (unidecode(author.replace(" ","")), author)
        if len(authors)>1:
          paper_html += '<a href="/proceedings/authors/%s">%s</a> and ' % (unidecode(authors[-2].replace(" ","")), authors[-2])
        paper_html += '<a href="/proceedings/authors/%s">%s</a>' % (unidecode(authors[-1].replace(" ","")), authors[-1])
        paper_html += "</td>\n"
        paper_html += "</tr>\n"
        paper_html += '<tr><th>Abstract:</th>\n'
        paper_html += "<td>%s</td></tr>\n" % escape(abstract.strip()).replace("\n\n","<br>\n\n")
        paper_html += '<tr><th>Keywords:</th>\n'
        paper_html += "<td>%s</td></tr>\n" % escape(", ".join(keywords.split("\n")))
        paper_html += '<tr><th>Paper:</th>\n'
        paper_html += '<td><a href="https://doi.org/10.3384/ecp21181%d">full paper</a>' % firstPage
        if "library%d" % i in session:
          paper_html += ' / <a href="%s">library</a>' % session["library%d" % i]
        paper_html += '</td>\n'
        paper_html += '</tr>\n'
        handleMultiKey = ""
        if lastNames[firstAuthorLastName] is not None:
          handleMultiKey = string.ascii_lowercase[lastNames[firstAuthorLastName]]
          lastNames[firstAuthorLastName] += 1
        paperNum += 1
        bibtex = ""
        bibtex += """
@InProceedings{modelica.org:%s:2021%s,
  title = {%s},
  author = {%s},
  pages = {%d--%d},
  doi = {10.3384/ecp21181%d},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\\"{o}ping, Sweden},
  editor = {Martin Sjölund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Linköping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Linköping University Electronic Press},
  year = {2021}
}          
""" % (firstAuthorLastName, handleMultiKey, session["title%d" % i], allAuthors.replace(", ", " and "), firstPage, lastPage, firstPage)
        paper_html += '<tr><th>Bibtex:</th>\n'
        paper_html += '''<td><pre>
%s
</pre></td></tr>\n''' % escape(bibtex.strip())
        paper_html += "</table><br>\n"
        fout_session.write(paper_html)
        all_bibtex += [bibtex]

        for author in authors:
          all_authors[author] = all_authors.get(author, []) + [paper_html]

with open("proceedings/authors.md", "w") as fout_authors:
  for author in sorted(all_authors.keys(), key = lambda s: s.split(" ")[-1]):
    names = author.split(" ")
    last_name = names[-1]
    first_name = " ".join(names[0:-1])
    author_filename = unidecode(author.replace(" ", ""))
    fout_authors.write("* [%s, %s](/proceedings/authors/%s)\n" % (last_name, first_name, author_filename))
    with open("proceedings/authors/%s.md" % author_filename, "w") as fout_author:
      fout_author.write("## Papers by %s\n" % author)
      fout_author.write("\n".join(all_authors[author]))
with open("proceedings/modelica2021.bib", "w") as fout:
  for entry in all_bibtex:
    fout.write(entry.strip())
    fout.write("\n")
