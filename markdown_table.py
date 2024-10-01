# nice way of formatting the table for the README 

from prettytable import PrettyTable
from prettytable import MARKDOWN

def create_markdown_table():
    # Create a PrettyTable object
    table = PrettyTable()

    # Define the column headers
    table.field_names = ["Repo List", "Description"]

    # Add rows of data
    table.add_row(["Research Software", " "])
    table.add_row(["Computational SIs", " "])
    table.add_row(["Educational Material", " "])

    # Get the table in Markdown format
    table.set_style(MARKDOWN)
    markdown_table = table#.get_string(border=False, hrules=1)
    return markdown_table

# Print the markdown table to the console
markdown_table = create_markdown_table()
print(markdown_table)

