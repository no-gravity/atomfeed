from datetime import datetime

atom_template = """
    <?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
        <title>{title}</title>
        <id>{id}</id>
        <subtitle>{subtitle}</subtitle>
        <link href="{link_web}"/>
        <link href="{link_feed}" rel="self"/>
        <updated>{updated}</updated>
        <author>
            <name>{author_name}</name>
            <email>{author_mail}</email>
        </author>
        {entries}
    </feed>
"""

entry_template = """
    <entry>
        <title>{title}</title>
        <link href='{link}'/>
        <id>{link}</id>
        <updated>{updated}</updated>
        <summary>{summary}</summary>
        <content type="html">
            {content}
        </content>
    </entry>

"""

def template_dict(template, data):
    r = template
    for tag in data.keys():
        r = r.replace('{'+tag+'}',data[tag])
    return r

def generate(data):
    feed = ""
    data["updated"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    for entry in data["entries"]:
        feed += template_dict(entry_template, entry)
    data["entries"] = feed
    return template_dict(atom_template, data)
