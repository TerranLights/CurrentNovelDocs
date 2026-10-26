#!/usr/bin/env python3
"""Extract Andrew George's Penguin translation (2nd ed., 2020) from the EPUB into
plain-text section files for the play-by-play. The output is the full copyrighted
text, so it goes to a scratch folder, never into the repo.

Usage: python3 extract_epub.py <path-to-epub> <output-dir>

Conventions kept from the book:
  [square brackets]  George's restorations of broken text
  _underscores_      words in italics in the book (George: uncertain decipherment
                     or translation; see 00_note_on_translation.txt)
  {p.N}              the printed page N begins here
  {l.I 5}            George's line number in the margin (tablet I, line 5)
  two leading spaces a verse line George prints indented
"""
import html, os, re, sys, zipfile

epub, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
z = zipfile.ZipFile(epub)
read = lambda p: z.read("OEBPS/Text/" + p).decode("utf-8")

# (output name, file, start anchor or None, end anchor or None); anchors come from toc.ncx
SECTIONS = [
    ("00_preface_2nd_edition", "part0007.xhtml", None, None),
    ("00_note_on_translation", "part0008.xhtml", None, None),
    ("00_time_chart", "part0010.xhtml", None, None),
    ("00_dramatis_personae", "part0011.xhtml", None, None),
    ("00_introduction", "part0012.xhtml", None, None),
    ("SB_01_Tablet_I", "part0013.xhtml", "epi0000483", "epi0000792"),
    ("SB_02_Tablet_II", "part0013.xhtml", "epi0000792", "epi0001073"),
    ("SB_03_Tablet_III", "part0013.xhtml", "epi0001073", "epi0001236"),
    ("SB_04_Tablet_IV", "part0013.xhtml", "epi0001236", "epi0001453"),
    ("SB_05_Tablet_V", "part0013.xhtml", "epi0001453", "epi0001756"),
    ("SB_06_Tablet_VI", "part0013.xhtml", "epi0001756", "epi0001940"),
    ("SB_07_Tablet_VII", "part0013.xhtml", "epi0001940", "epi0002139"),
    ("SB_08_Tablet_VIII", "part0013.xhtml", "epi0002139", "epi0002335"),
    ("SB_09_Tablet_IX", "part0013.xhtml", "epi0002335", "epi0002476"),
    ("SB_10_Tablet_X", "part0013.xhtml", "epi0002476", "epi0002801"),
    ("SB_11_Tablet_XI", "part0013.xhtml", "epi0002801", "epi0003141"),
    ("SB_12_Tablet_XII", "part0013.xhtml", "epi0003141", None),
    ("SUM_0_chapter_intro", "part0014.xhtml", None, "epi0003160"),
    ("SUM_1_Gilgamesh_and_Akka", "part0014.xhtml", "epi0003160", "epi0003287"),
    ("SUM_2_Gilgamesh_and_Huwawa", "part0014.xhtml", "epi0003287", "epi0003741"),
    ("SUM_3_Gilgamesh_and_the_Bull_of_Heaven", "part0014.xhtml", "epi0003741", "epi0003964"),
    ("SUM_4_Gilgamesh_and_the_Netherworld", "part0014.xhtml", "epi0003964", "epi0004455"),
    ("SUM_5_The_Death_of_Gilgamesh", "part0014.xhtml", "epi0004455", None),
    ("OB_all_fragments", "part0015.xhtml", None, None),
    ("MISC_all_fragments", "part0016.xhtml", None, None),
    ("APP_from_tablet_to_translation", "part0017.xhtml", None, None),
    ("GLOSSARY_proper_nouns", "part0018.xhtml", None, None),
]

def cut(s, start, end):
    i = s.find('id="%s"' % start) if start else s.find("<body")
    i = s.rfind("<", 0, i)
    j = s.find('id="%s"' % end) if end else len(s)
    if end:
        j = s.rfind("<", 0, j)
    return s[i:j]

def to_text(h):
    h = re.sub(r'<span id="pg(\w+)" epub:type="pagebreak"></span>', r"{p.\1}", h)
    # The margin number is always the last thing in its verse line; it may end in a
    # prime (e.g. "Nc 4´"), so match up to the line's closing </div>.
    h = re.sub(r'<span class="line_number">(.*?)</span>\s*</div>',
               lambda m: " {l." + re.sub(r"<[^>]+>", "", html.unescape(m.group(1))).strip() + "}</div>", h)
    # Keep George's indentation: indented verse lines start with two spaces.
    h = re.sub(r'<div class="poetry_line_indented"[^>]*>', "\n\u00a0\u00a0", h)
    h = re.sub(r"</?em>", "_", h)
    h = re.sub(r"<(div|p|h\d)[^>]*>", "\n", h)
    h = re.sub(r"<br\s*/?>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t]+", " ", h).replace("\u00a0", " ")
    return re.sub(r"\n\s*\n+", "\n\n", h).strip() + "\n"

for name, f, a, b in SECTIONS:
    t = to_text(cut(read(f), a, b))
    open(os.path.join(out, name + ".txt"), "w", encoding="utf-8").write(t)
    print("%-45s %7d words" % (name, len(t.split())))
