from requests import get, post, delete

print(delete('http://localhost:5000/api/v2/news/9').json())

