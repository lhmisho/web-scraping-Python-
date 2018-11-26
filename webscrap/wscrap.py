from urllib.request import  urlopen
from bs4 import BeautifulSoup



# global var

url_al      = 'https://www.aljazeera.com/' # for data collects
filepath    = 'html/al.html'

class Scrapper:
    __url   = ''
    __data  = ''
    __wlog  = None
    __soup  = None

    def __init__(self, url, wlog):
        self.__url  = url
        self.__wlog = wlog

    def retrieve_data(self):
        try:
            html = urlopen(self.__url)

        except Exception as e:
            print(e)
            self.__wlog.report(e)

        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("retrieved sucessfully")

    # for writing data as html
    def write_data_in_html(self, filepath = filepath, data = ''):
        try:
            with open(filepath, 'wb') as fp:
                if data:
                    fp.write(data)
                else:
                    fp.write(self.__data)

        except Exception as e:
            print(e)
            self.__wlog.report(str(e))


    # for reading data from html
    def read_data_from_html(self,filepath=filepath):
        try:
            with open(filepath) as fp:
                self.__data = fp.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    # change url
    def change_url(self,url):
        self.__url = url

    # print data
    def print_data(self):
        print(self.__data)

    # convert data to bs4
    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")

    # parse data
    def parse_data_to_bs4(self):
        news_list = self.__soup.find_all(['h1','h2','h3','h4'])
        #print(news_list)

        htmltext = '''
        <html>
            <head><title>Simple News Link Scrapper</title></head>
            <body>
                {NEWS_LINKS}
            </body>
        </html>
        '''

        news_links = '<ol>'
        for tag in news_list:
            if tag.parent.get('href'):
                # print (self.__url + tag.parent.get('href'), tag.string)
                link = self.__url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)

        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)

        # print(htmltext)
        self.write_data_in_html(filepath="html/simplenews.html", data=htmltext.encode())











