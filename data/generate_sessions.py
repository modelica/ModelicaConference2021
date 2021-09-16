#!/usr/bin/env python3

import json
import os
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

with open("proceedings/sessions.md", "w") as fout_sessions:
  for session in data:
    num = session["session_number"].split(" ")[1]
    fout_sessions.write('* [%s - %s](/proceedings/sessions/%s)\n' % (session["session_number"],session["session_name"],num))
    with open("proceedings/sessions/%s.md" % num, "w") as fout_session:
      fout_session.write("## %s - %s\n" % (session["session_number"],session["session_name"]))
      fout_session.write("<table>\n")
      for i in range(1,6):
        if "title%d" % i not in session:
          break
        fout_session.write("<tr><th>Authors:</th>\n<td>\n")
        authors = session["author%d" % i]
        authors = authors.replace(" and ", ", ").split(", ")
        paper_html = ""
        for author in authors[:-2]:
          paper_html += '<a href="/proceedings/authors/%s">%s</a>, ' % (unidecode(author.replace(" ","")), author)
        if len(authors)>1:
          paper_html += '<a href="/proceedings/authors/%s">%s</a> and ' % (unidecode(authors[-2].replace(" ","")), authors[-2])
        paper_html += '<a href="/proceedings/authors/%s">%s</a>, ' % (unidecode(authors[-1].replace(" ","")), authors[-1])
        paper_html += "</td>\n"
        paper_html += "</tr>\n"
        paper_html += '<tr><th>Title:</th>\n'
        paper_html += '<td>%s</td></tr>' % session["title%d" % i]
        paper_html += '</tr>\n<tr><th>Paper:</th>\n'
        paper_html += '<td><a href="/abstracts/abstract_%s_%d">abstract</a> <a href="/proceedings/papers/Modelica2021session%s_paper%d.pdf">full paper</a></td>\n' % (num, i, num, i)
        paper_html += '</tr>\n'
        fout_session.write(paper_html)

        for author in authors:
          all_authors[author] = all_authors.get(author, []) + [paper_html]

      fout_session.write('</table>\n')
      fout_session.write('\n\n')

with open("proceedings/authors.md", "w") as fout_authors:
  for author in sorted(all_authors.keys(), key = lambda s: s.split(" ")[-1]):
    names = author.split(" ")
    last_name = names[-1]
    first_name = " ".join(names[0:-1])
    author_filename = unidecode(author.replace(" ", ""))
    fout_authors.write("* [/proceedings/authors/%s](%s, %s)\n" % (author_filename, last_name, first_name))
    with open("proceedings/authors/%s.md" % author_filename, "w") as fout_author:
      fout_author.write("## Papers by %s\n" % author)
      fout_author.write("<table>")
      fout_author.write("\n".join(all_authors[author]))
      fout_author.write("</table>")

