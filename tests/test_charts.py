import io
import unittest
import unittest.mock

from colored import fg, attr, stylize
from charts import Options, Chart, HorizontalBarChart

class TestOptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.opts = Options()
        # cls.opts.graph_color = 'cyan'
        # cls.opts.header_style = 'underlined'
        # cls.opts.text_color = 'yellow'

    def test_symbol_setter(self):
        self.opts.symbol = '@'
        self.assertEqual(self.opts.fsymbol, '@')
        self.assertEqual(self.opts.msymbol, '>')
        self.assertEqual(self.opts.esymbol, '-')

    def test_check_color(self):
        self.opts.graph_color = 'cyan'
        self.assertEqual(
            fg('cyan'), self.opts.graph_color)

        self.assertEqual(
            'white', self.opts._check_color('notcolor'))
        self.assertEqual(
            fg('magenta'), self.opts._check_color('magenta'))

    def test_check_attr(self):
        self.opts.header_style = 'underlined'
        self.assertEqual(
            attr('underlined'), self.opts.header_style)

        self.assertEqual(
            'bold', self.opts._check_attr('notattr'))
        self.assertEqual(
            attr('blink'), self.opts._check_attr('blink'))


class TestChart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chart = Chart()

    def test_chart_init(self):
        # Test that if no Options arg given new is created
        self.assertIsInstance(self.chart.options, Options)


class TestHorizontalBarChart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.horizontal_chart = HorizontalBarChart()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.horizontal_chart.chart(
            title='Test Title',
            pre_graph_text='This looks sweet',
            post_graph_text=None,
            footer=None,
            maximum=10,
            current=5
        )

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_chart(self):
        compare = f"{stylize('Test Title', fg('red') + attr('bold'))}\n" \
            + f"{stylize('This looks sweet', fg('white'))}\n" \
            + f"{stylize('███████████████████▒░░░░░░░░░░░░░░░░░░░', fg('white'))}"
        
        self.assert_stdout(compare)

    def test_draw_horizontal_bar(self):
        compare = '███████████████████▒░░░░░░░░░░░░░░░░░░░'
        self.assertEqual(
            compare, self.horizontal_chart.draw_horizontal_bar(10, 5))

        compare_02 = '▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'
        self.assertEqual(
            compare_02, self.horizontal_chart.draw_horizontal_bar(10, 0)
        )


# class TestChartPrint(unittest.TestCase):
#     """Test Printing of Charts in the terminal"""

#     @classmethod
#     def setUpClass(cls):
#         cls.chart01 = ChartPrint(graph=Color.RED)
#         cls.chart02 = ChartPrint(symbol='@')

#     def test_grap_color(self):
#         self.assertIsInstance(self.chart01,
#                                 ChartPrint)
#         self.assertIsInstance(self.chart02,
#                                 ChartPrint)
#         self.assertEqual(self.chart01.graph,
#                                 fg('red'))
#         self.assertEqual(self.chart01.msymbol,
#                             stylize('▒', fg('red')))
#         self.assertEqual(self.chart02.fsymbol, '@')
#         self.assertEqual(self.chart02.esymbol, '-')
        
#     def test_draw_horizontal_bar(self):
#         compare = '[@@@@@@@@@@@@@@@@@@>------------------]'
#         self.assertEqual(
#             self.chart02.draw_horizontal_bar(10, 5),
#             compare
#         )

#     def test_draw_vertical_bar(self):
#         self.assertEqual(
#             self.chart02.draw_vertical_bar(10, 5)[:22],
#             '\n---------  \n---------'
#         )


if __name__ == '__main__':
    unittest.main()
