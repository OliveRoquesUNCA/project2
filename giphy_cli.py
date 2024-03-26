import os

from giphy_api import GiphyAPI

API_KEY = os.environ["GIPHY_API_KEY"]


class GiphyCLI:

    def trending(self, count=5, markdown=False, lucky=False):
        i = 1
        if lucky:
            count = 1

        trends = GiphyAPI("trending", limit=str(count))
        results = trends.query(markdown)
        output = ""
        if not markdown:
            for name, result in results.items():
                if not lucky:
                    output += str(i) + ") "
                output += name + " (" + result + ")\n"
                i += 1
        else:
            for name, result in results.items():
                if not lucky:
                    output += str(i) + ") "
                output += "![" + name + "](" + result + ")\n"
                i += 1
        return output

    def search(self, query, count=5, markdown=False, lucky=False):
        i = 1
        if lucky:
            count = 1
        searches = GiphyAPI("search", limit=str(count), q=query)
        results = searches.query(markdown)
        output = ""
        if not markdown:
            for name, result in results.items():
                if not lucky:
                    output += str(i) + ") "
                output += name + " (" + result + ")\n"
                i += 1
        else:
            for name, result in results.items():
                if not lucky:
                    output += str(i) + ") "
                output += "![" + name + "](" + result + ")\n"
                i += 1
        return output
