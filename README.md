# atomfeed
A single file atom feed library with no dependencies

Based on code from <a href="https://github.com/gtlsgamr/htxyz">gtlsgamr/htxyz</a>. (In particular <a href="https://github.com/gtlsgamr/htxyz/blob/1260e36f74e35cce4e8891a2faef29fd44e075f2/htxyz.py#L166">this function</a>.)

Demo: The feed on www.gibney.org

License: GPL v3.0

Example usage:

```python
import atomfeed

data = {
    "title"      : "A wonderful feed",
    "id"         : "https://www.example.com",
    "link_web"   : "https://www.example.com",
    "link_feed"  : "https://www.example.com/atom.xml",
    "subtitle"   : "Everything about feeds and stuff",
    "updated"    : "2023-01-07",
    "author_name": "Mr. Example",
    "author_mail": "example@example.com",
}

data["entries"] = [{
    "title"  : "Hello World",
    "date"   : "2022-01-08",
    "updated": "2022-01-08",
    "link"   : "https://www.example.com/hello_world",
    "summary": "A greeting to the world",
    "content": "Bonjour!",
}]

feed = atomfeed.generate(data)
```
