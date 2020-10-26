import xml.etree.ElementTree as ET
import sys

document =   """<response>
                <article>
                <title>A Novel Approach to Image Classification, in a Cloud Computing Environment stability.</title>
                <publicationtitle>IEEE Transactions on Cloud Computing</publicationtitle>
                <abstract>Classification of items within PDF documents has always been challenging.  This stability document will discuss a simple classification algorithm for indexing images within a PDF.</abstract>
                </article>
                <body>
                <sec>
                <label>I.</label>
                <p>Should Haven't That is a bunch of text pattern these classification and cyrptography.  These paragraphs are nothing but nonsense.  What is the statbility of your program to find neural nets. Throw in some numbers to see if you get the word count correct this is a classification this in my nd and rd words.  What the heck throw in cryptography.</p>
                <p>I bet diseases you can't find probability twice.  Here it is a again probability.  Just to fool you I added it three times probability.  Does this make any pattern classification? pattern classification! pattern classification.</p>
                <p>
                    <fig>
                    <label>FIGURE.</label>
                    <caption>This is a figure representing convolutional neural nets.</caption>
                    </fig>
                </p>
                </sec>
                </body>
                </response>"""

root = ET.fromstring(document)

L = 0
scores = {"title": 5, "abstract": 3, "body": 1}
words = {}

counter = 0

for child in root.iter():
    text = child.text.lower()

    if any(c.isalpha() for c in text):
        text = text.split(" ")

        for word in text:
            if len(word) < 2:
                continue

            if word not in words:
                words[word] = [1, child.tag]

            else:
                words[word][0] += 1
        
            L += 1

densities = {}

for word in words:
    tag = words[word][1]

    S = words[word][0]

    if tag in scores:
        S *= scores[tag]

    densities[word] = S / L * 100

densities = {k: v for k, v in sorted(densities.items(), key=lambda item: item[1], reverse=True)}

for word in list(densities.items()):
    print(word)

