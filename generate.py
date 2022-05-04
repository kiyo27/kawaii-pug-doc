from jinja2 import Environment, FileSystemLoader


class Pug:
    def __init__(self, no):
        self.serial_no = no
        self.attributes = [
            "3D glasses",
            "scurf",
            "pipe"
        ]


env = Environment(
    loader=FileSystemLoader("template")
)
template = env.get_template("child.html")
pug = Pug(1)
ctx = template.render(pug=pug)

with open("public/1/index.html", "w") as f:
    f.write(ctx)
