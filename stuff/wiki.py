import requests
from collections import deque
from collections import defaultdict
start = 'Albert Einstein'
end = 'Oprah Winfrey'

def recreate_path(start,end, parent):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path



def find_path(start, end):
    url = "https://en.wikipedia.org/w/api.php"
    q = deque()
    q.append(start)

    depth = 0
    seen = set()

    parent = {}
    while q:
        depth += 1
        for _ in range(len(q)):
            l = q.popleft()
            params = {
                'action' : 'query',
                'format' :'json',
                'titles' : l,
                'prop' : 'links',
                'pllimit' : 'max'
            }
            print(depth, l)

            response = requests.get(url,params=params)
            data = response.json()
            links = data['query']['pages']
            # links = [link['title'] for link in links]
            linkss = []
            for k, v in links.items():
                if k != '-1':
                    for ll in v['links']:
                        linkss.append(ll['title'])

            # links = [l['title']  for k, v in links.items() if k != -1 for l in v['links'] ]
            for link in linkss:
                if link == end:
                    print(f'found {end} in {depth} steps')
                    parent[link] = l

                    return recreate_path(start,link,parent)
                if link not in seen:
                    seen.add(link)
                    q.append(link)
                    parent[link] = l




if __name__ == '__main__':
    print(find_path('Albert Einstein', 'Oprah Winfrey'))