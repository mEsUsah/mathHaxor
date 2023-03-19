from jinja2 import Environment, PackageLoader, select_autoescape
class WebGenerator:
    @staticmethod
    def generateHtml(problems, showAnswer):
        env = Environment(
            loader=PackageLoader('utils', 'templates'),
            autoescape=select_autoescape()
        )

        template = env.get_template('problemPrint.html')

        return template.render(problems=problems, showAnswer=showAnswer)