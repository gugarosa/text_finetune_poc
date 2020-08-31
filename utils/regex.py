import re


def clean_html(html):
    """Cleans an html-based string.

    Args:
        html (str): HTML string.

    Returns:
        A html-stripped string.

    """

    # Defines the regex to clean the HTML
    regex = re.compile('<.*?>')

    # Cleans the HTML
    text = re.sub(regex, '', html)

    return text
