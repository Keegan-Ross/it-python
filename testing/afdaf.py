#!/usr/bin/env python
# encoding: utf-8
import csv
from collections import Counter

import lxml.html


def create_test_html():
    """ Return a test HTML string. """
    return lxml.html.fromstring("""<html>
              <head>
              </head>
              <body>
              <div class="test">Some <em>text</em></div>
              <img src="some_location" alt="Alt text" width=540>
              More <b>text</b>
              </body>
              </html>""")


def get_html_elements(html):
    """ Take an lxml ElementTree; return Counter of elements; count once. """
    return Counter({element.tag for element in html.iter()})


def get_html_attributes(html):
    """ Take an lxml ElementTree; return Counter of attributes; count once. """
    attributes = set()
    for element in html.iter():
        for attribute in element.keys():
            element_attribute = ' '.join([element.tag, attribute])
            attributes.add(element_attribute)
    return Counter(attributes)


def write_csv_from_html_counter(counter, filename):
    """ Take a Counter and write a CSV from it. """
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['entity', 'count'])
        for entity, count in counter.most_common():
            writer.writerow([entity, count])


def main():
    """ Count elements in a HTML string once only. """
    html = create_test_html()
    elements = get_html_elements(html)
    attributes = get_html_attributes(html)
    write_csv_from_html_counter(elements, "elements.csv")
    write_csv_from_html_counter(attributes, "attributes.csv")


if __name__ == '__main__':
    main()