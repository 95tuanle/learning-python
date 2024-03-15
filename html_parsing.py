from html.parser import HTMLParser

paragraphs = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered start tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        global paragraphs
        if tag == "p":
            paragraphs += 1

        if attrs.__len__() > 0:
            print("\tAttributes: ")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_endtag(self, tag):
        print("Encountered end tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

    print("Number of paragraphs: ", paragraphs)


if __name__ == "__main__":
    main()
