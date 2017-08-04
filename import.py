import sys
import xml.etree.ElementTree as ET


article_template = """\
---
title: {title}
slug: {slug}
layout: post
---
{content}
"""

def import_xml(export_fn):

    for article in ET.parse(export_fn).iter('article'):
        title = article.find('title').text
        slug = title.lower().replace(' ', '-')
        content = article.find('content').text
        publish_date = None
        published = article.find('publish').text == 'true'
        if published:
            publish_date = article.find('publish-date').text.split('T')[0]

        open(f'{publish_date}-{slug}.md', 'w').write(
            article_template.format(
                title=title,
                content=content,
                slug=slug,
            )
        )

if __name__ == '__main__':
    import_xml(sys.argv[-1])