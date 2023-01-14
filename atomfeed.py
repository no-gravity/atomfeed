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
    most_recent = "0000-00-00"
    for entry in data["entries"]:
        if entry["updated"] > most_recent: most_recent = entry["updated"]
        most_recent = max(most_recent, entry["updated"])
        feed += template_dict(entry_template, entry)
    data["entries"] = feed;
    # If no feed update time was provided, use the one of the most recent entry:
    if not data["updated"]: data["updated"] = most_recent
    return template_dict(atom_template, data)
