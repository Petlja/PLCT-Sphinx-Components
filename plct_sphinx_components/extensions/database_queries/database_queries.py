__author__ = 'petlja'

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from ..python_kernel import setup_py_kernel
import html



def setup(app):
    setup_py_kernel(app)
    app.add_css_file('database-queries.css')
    app.add_js_file('database-queries.js')
    app.add_directive('db-query', DBComponentDirective)
    app.add_node(DBComponentNode, html=(visit_DBComponent_node, depart_DBComponent_node))


TEMPLATE_START = '''
  <db-query id="3" check-colum-name show-expected-result>
    <file>../_static/it3_biblioteka.sql</file>
    <name>biblioteka</name>
    <solution-query>insert into autori values (201, 'test' , 'test')</solution-query>
    <check-query>select * from autori</check-query>
    <hint>select * from autor ??? </hint>
    <textarea>insert into autori values (201, 'test' , 'test')
    </textarea>
  </db-query>
    '''


TEMPLATE_END = '''
    '''


class DBComponentNode(nodes.General, nodes.Element):
    def __init__(self, content):
        super(DBComponentNode, self).__init__()
        self.note = content


def visit_DBComponent_node(self, node):
    node.delimiter = "_start__{}_".format("info")
    self.body.append(node.delimiter)
    res = TEMPLATE_START % node.note
    self.body.append(res)


def depart_DBComponent_node(self, node):
    res = TEMPLATE_END
    self.body.append(res)
    self.body.remove(node.delimiter)


class DBComponentDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    has_content = True
    option_spec = {}
    option_spec.update({
        'packages': directives.unchanged,
        'opt-in-ai': directives.unchanged,
    })


    def run(self):
        """
        generate html to include note box.
        :param self:
        :return:
        """
        self.options['divid'] = self.arguments[0]
        innode = DBComponentNode(self.options)

        return [innode]
    

def encode(html_code):
    return html.escape(html_code)