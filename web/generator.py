from jinja2 import Environment, PackageLoader, select_autoescape

def problemsHtml(problems, showAnswer):
    env = Environment(
        loader=PackageLoader('web', 'templates'),
        autoescape=select_autoescape()
    )

    template = env.get_template('problemPrint.html')
    return template.render(problems=problems, showAnswer=showAnswer)