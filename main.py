import datetime
import pandas
import argparse

from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def create_parser():
    parser = argparse.ArgumentParser(description='Specify the path to the excel file.')
    parser.add_argument('-f', '--file', default='wine.xlsx',
                        help='Path to Excel file')
    return parser.parse_args()


def get_years():
    today = int(datetime.datetime.now().year)
    years = today - 1920
    return years


def get_catalog(file):
    catalog = pandas.read_excel(file, sheet_name='Лист1', na_values=None,
                                keep_default_na=False).to_dict(orient='records')
    categorized_catalog = defaultdict(list)
    for drink in catalog:
        categorized_catalog[drink['Категория']].append(drink)
    return sorted(categorized_catalog.items())


def main():
    args = create_parser()
    catalog = get_catalog(args.file)
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('template.html')
    rendered_page = template.render(
        years=f'Уже {get_years()} лет с вами',
        catalog=catalog
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()