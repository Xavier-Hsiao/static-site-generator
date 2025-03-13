import unittest
from generate_pages import extract_title

class TestGeneratePages(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts
"""
        self.assertEqual(
            extract_title(md),
            "Tolkien Fan Club"
        )
    
    def test_extract_title_without_title(self):
        md = """
## Lonely text

Hey... I am just a lonely text without my **H1 Title**.
"""
        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()