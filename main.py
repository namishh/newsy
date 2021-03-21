from newsapi.newsapi_client import NewsApiClient
import tkinter as tk
import webbrowser
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)

API_KEY = os.getenv('API_KEY')


class Newsy:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("News App")

        self.newsapi = NewsApiClient(api_key=API_KEY)

        self.top_headlines = tk.StringVar()
        self.all_articles = tk.StringVar()

        self.query = None

        self.createAndDisplay()

    def exception_handler(func):

        def wrapper(self, *args, **kwargs):

            try:

                return func(self, *args, **kwargs)

            except:

                self.articles_list.config(
                    text=("There was error in processing your request."))

        return wrapper

    @exception_handler
    def createAndDisplay(self):

        self.articles_list = tk.Label(
            self.root, text="", font=('Helvetica', 15))
        self.articles_list.place(
            relx=0, rely=0.25, relheight='0.7', relwidth='1')

        title = tk.Label(self.root, text="News App", font=('Modern', 40))
        title.place(relx=0.6, rely=0.01)

        top_headlines = self.newsapi.get_top_headlines(
            language='en', country='in')
        all_articles = self.newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',
                                                   language='en', sort_by='relevancy', page=5)

        top_headlines = [news['url'] for news in top_headlines['articles']]
        all_articles = [news['url'] for news in all_articles['articles']]

        drop = tk.OptionMenu(self.root, self.top_headlines, *top_headlines)
        drop.place(relx=0, rely=0)

        drop2 = tk.OptionMenu(self.root, self.all_articles, *all_articles)
        drop2.place(relx=0, rely=0.1)

        url_button = tk.Button(self.root, text="Select", bd=1,
                               activebackground="#ffee96", command=self.get_url)
        url_button.place(relx=0.8, rely=0)

        headline = tk.Button(self.root, text="India News", bd=1,
                             activebackground="#ffee96", command=self.get_headlines)
        headline.place(relx=0.3, rely=0.2)

        all_news = tk.Button(self.root, text="World News", bd=1,
                             activebackground="#ffee96", command=self.get_news)
        all_news.place(relx=0.4, rely=0.2)

        self.query = tk.Entry(self.root, font=('Courier', 10), bd=0)
        self.query.place(relx=0.5, rely=0.2)

        search = tk.Button(self.root, text="Search", bd=1,
                           activebackground="#ffee96", command=self.search_query)
        search.place(relx=0.65, rely=0.2)

    @exception_handler
    def get_url(self):

        webbrowser.open(self.top_headlines.get())

        webbrowser.open(self.all_articles.get())

    @exception_handler
    def get_headlines(self):

        articles = self.newsapi.get_top_headlines(
            language='en', country='in')

        self.articles_list.config(
            text=(" ".join([news['title'] + "\n" for news in articles['articles']])))

    @exception_handler
    def get_news(self):

        articles = self.newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',
                                               language='en', sort_by='relevancy', page=5)

        self.articles_list.config(text=" ".join(
            [news['title'] + "\n" for news in articles['articles']]))

    @exception_handler
    def search_query(self):

        articles = self.newsapi.get_everything(
            q=self.query.get(), language='en')

        self.articles_list.config(
            text=(" ".join([news['title'] + "\n" for news in articles['articles']])))


if __name__ == "__main__":

    newsy = Newsy()

    newsy.root.mainloop()
