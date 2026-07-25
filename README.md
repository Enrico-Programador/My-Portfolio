# Static Site Generator

## Overview:

This converts a .md file to html, the site works with git hub to make it easy to upload online, this is only a base that I have done by myself to build a portfolio.
Use the standard formatting for the .md file, the conversion will do all the work automatically and it will handle italic, bold, code, paragraph, heading, lists and quotes.

## Standard .md Syntax:

- Headings: Use the # symbol followed by a space. More hashtags create smaller headers.
- Bold: **text**
- Italics: *text*
- Link: [Click here](https://example.com)
- Image: ![Alt text] (image-url.jpg)
- Inline Code: Wrap words in single backticks like `code`.
- Fenced Blocks: Enclose multiple lines with three backticks (```) on a line above and below the block.
- Blockquote: Place a > before the text to indent it as a quote.
- Line Break: Leave an entirely blank line between two blocks of text to start a new paragraph.
- Lists: use - for each item in the list
- Ordered lists: use *1.)* for each subsequent numbers

## How it works:

The static site generator will extract the .md file into nodes then separate each node into blocks. Based on the type of syntax used it will use the **markdown to html** function to make a conversion based on the type of node presented. It will create the documents into the docs dir, recursively. Each dir is a page of the site. The images are inside the static dir.


This is a open source project with no financial intention, it was all created by me from scratch with the help of boot.dev project.
I did not use any AI to write this project, but I tried to optimize it my own way.


## Contact

If you liked the project you can contact me at:
enrico2015ap@gmail.com or +55 (19) 99773-2112
