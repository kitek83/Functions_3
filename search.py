from googlesearch import search

def search_query(query):
    count = 0
    for j in search(query,num=200,stop=200,pause=3):
        count += 1
        print(f'{count}.{j}')

