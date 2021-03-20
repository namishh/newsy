from newsapi.newsapi_client import NewsApiClient
import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("1920x1080")
root.title("News App")

newsapi = NewsApiClient(api_key='9319a21a7472491897d5efd548f290dc')

label = tk.Label(root, text="", font=('Helvetica', 15))
label.place(relx=0, rely=0.25, relheight='0.7', relwidth='1')

title = tk.Label(root, text="News App", font=('Modern', 40))
title.place(relx=0.6, rely=0.01)

top_headlines = newsapi.get_top_headlines(language='en', country='in')
all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',
                                      language='en', sort_by='relevancy', page=5)
text = tk.StringVar()
text.set("Label")

li = [news['url'] for news in top_headlines['articles']]
li2 = [news['url'] for news in all_articles['articles']]

clicked = tk.StringVar()
clicked2 = tk.StringVar()


def get_url():
    try:
        webpage = clicked.get()
        webpage2 = clicked2.get()
        webbrowser.open(webpage2)
        webbrowser.open(webpage)
    except Exception as e:
        pass


def get_headlines():
    try:

        top_headlines = newsapi.get_top_headlines(language='en', country='in')
        # print(top_headlines.keys())
        # print(top_headlines['articles'] )
        li = []
        for news in top_headlines['articles']:
            #print(news['title'] + " Url = " + news['url'])
            li.append(news['title'])

        # li2 = [news['title'] + " " + news['url'] for news in top_headlines['articles']]
        label.config(text=(" ".join([news['title'] + "\n" for news in top_headlines['articles']])))
    except Exception as e:
        label.config(text=("There was error in processing your request."))


def get_news():
    try:

        all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',
                                              language='en', sort_by='relevancy', page=5)

        li = []
        for news in all_articles['articles']:
            # print(news['title'] +  " Url = " + news['url'])
            li.append(news['title'])

        label.config(text=" ".join([news['title'] + "\n" for news in all_articles['articles']]))
    except Exception as e:
        label.config(text=("There was error in processing your request."))


def search_query():
    try:

        top_headlines1 = newsapi.get_everything(q=query.get(), language='en')
        li = []
        for news in top_headlines1['articles']:
            # print(news['title'] +  " Url = " + news['url'])
            li.append(news['title'])

        # li2 = [news['title'] + " " + news['url'] for news in top_headlines['articles']]

        label.config(text=(" ".join([news['title'] + "\n" for news in top_headlines1['articles']])))
    except Exception as e:
        label.config(text=("There was error in processing your request."))


drop = tk.OptionMenu(root, clicked, *li)
drop.place(relx=0, rely=0)

drop2 = tk.OptionMenu(root, clicked2, *li2)
drop2.place(relx=0, rely=0.1)

url_button = tk.Button(root, text="Select", bd=1, activebackground="#ffee96", command=lambda: get_url())
url_button.place(relx=0.8, rely=0)

headline = tk.Button(root, text="India News", bd=1, activebackground="#ffee96", command=lambda: get_headlines())
headline.place(relx=0.3, rely=0.2)

all_news = tk.Button(root, text="World News", bd=1, activebackground="#ffee96", command=lambda: get_news())
all_news.place(relx=0.4, rely=0.2)

query = tk.Entry(root, font=('Courier', 10), bd=0)
query.place(relx=0.5, rely=0.2)

search = tk.Button(root, text="Search", bd=1, activebackground="#ffee96", command=lambda: search_query())
search.place(relx=0.65, rely=0.2)

root.mainloop()
