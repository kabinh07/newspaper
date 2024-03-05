import newspaper
from newspaper import Article

url = 'https://bangla.bdnews24.com/ctg/rchz8jlih4'
# url = 'https://www.prothomalo.com/bangladesh/1fmn9hdmqi'
# url = 'https://samakal.com/capital/article/225929/%E0%A6%9F%E0%A7%81%E0%A6%87%E0%A6%A8-%E0%A6%AA%E0%A6%BF%E0%A6%95-%E0%A6%AD%E0%A6%AC%E0%A6%A8%E0%A7%87%E0%A6%B0-%E0%A7%A7%E0%A7%A8-%E0%A6%B0%E0%A7%87%E0%A6%B8%E0%A7%8D%E0%A6%A4%E0%A7%8B%E0%A6%B0%E0%A6%BE%E0%A6%81-%E0%A6%B8%E0%A6%BF%E0%A6%B2%E0%A6%97%E0%A6%BE%E0%A6%B2%E0%A6%BE-%E0%A6%AD%E0%A7%87%E0%A6%99%E0%A7%87-%E0%A6%AB%E0%A7%87%E0%A6%B2%E0%A6%BE-%E0%A6%B9%E0%A6%B2%E0%A7%8B-%E0%A6%B0%E0%A7%81%E0%A6%AB%E0%A6%9F%E0%A6%AA-%C2%A0'
# url = 'https://www.kalerkantho.com/online/national/2024/03/04/1368722'
# url = 'https://bangla.bdnews24.com/world/ryhb4jvpfs'
# url = 'https://www.youtube.com/watch?v=ANWly8ElbTY'
# url = 'https://www.ntvbd.com/world/news-1368185'

article = Article(url)
article.download()
article.parse()

print(article.title)
print(article.meta_description)
