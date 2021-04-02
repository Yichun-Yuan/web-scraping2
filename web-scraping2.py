'''
Name: Yichun Yuan
Date: March 26th 2021
Description: Web-scraping
Use request and bs4 module to scrap infomation from a bookstore website, 
find all 1 star rating books on first 5 pages
then add them into a list
print books title and how many books in the end 
'''

import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# start by initiating an empty list that will hold our output.
one_star_titles = []

def web_scrapper(url:str):
  '''
  Input: url
  output:list contains books badage
  '''
  # Now iterate to get info from each page.
  # We want to include page_num, so index should go up to, but not include page_num+1,
  for n in range (1, 6):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    find_one_star(books, one_star_titles)
  #show_res(one_star_titles)
  return books
    
def find_one_star(books:list, title_li:list):
  '''
  Input: list contains books badges; a empty list  
  output: list contains one star books titles
  '''
  #create a loop to parse the books and select star rating one.
  for book in books:
    if len(book.select('.star-rating.One')) != 0: # if the list is not empty, then we do have a 1 star book. 
      book_title = book.select('a')[1]['title']
      title_li.append(book_title)    
  return title_li

def show_res(title_li):
  '''
  Input: list
  output: book_num: int 
  '''
  books_num = len(title_li)     
  for i in range(books_num):
    print(one_star_titles[i]) 
  print(f'There are {books_num} one star rating books on the first 5 pages.')
  return books_num
  

p = web_scrapper(base_url)
