import io
import re
import sys

from lxml import etree


TEI_NS = {"TEI": "http://www.tei-c.org/ns/1.0"}


class TEIToFlatText:
    """
    Converts TEI XML to a flat-text file
    """

    def __init__(self, input_path):
        self.input_path = input_path

    def extract_text_parts(self, tree, stream):
        for letter in tree.xpath("//TEI:div[@subtype='letter']", namespaces=TEI_NS):
            letter_num = letter.attrib["n"]
            for poem in letter.xpath(".//TEI:div[@subtype='poem']", namespaces=TEI_NS):
                poem_num = poem.attrib["n"]
                for line in poem.xpath(".//TEI:l", namespaces=TEI_NS):
                    line_num = line.attrib["n"]
                    for seg in poem.xpath(".//TEI:seg", namespaces=TEI_NS):
                        seg_num = seg.attrib["n"]
                        text = re.sub(r"\s+", " ", seg.xpath("string()").strip())
                        stream.write(
                            f"{letter_num}.{poem_num}.{line_num}.{seg_num} {text}\n"
                        )

    def extract_flat_text(self):
        with open(self.input_path) as f:
            tree = etree.parse(f)
            stream = io.StringIO()
            self.extract_text_parts(tree, stream)
        stream.seek(0)
        return stream


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        raise IndexError("Provide input path")

    converter = TEIToFlatText(path)
    stream = converter.extract_flat_text()
    print(stream.read(), end="")


if __name__ == "__main__":
    main()
