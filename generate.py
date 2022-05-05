from jinja2 import Environment, FileSystemLoader


class Pug:
    def __init__(self, no):
        self.serial_no = no
        self.group_count = 100
        self.attributes = [
            {"name": "3D glasses", "has": 20, "group_count": 100},
            {"name": "scurf", "has": 40, "group_count": 200},
            {"name": "pipe", "has": 300, "group_count": 300}
        ]
        self.attr_count = len(self.attributes)
        self.attr_group_count = 2000


env = Environment(
    loader=FileSystemLoader("template")
)
template = env.get_template("child.html")
pug = Pug(1)
ctx = template.render(pug=pug)

with open("public/details/1/index.html", "w") as f:
    f.write(ctx)
