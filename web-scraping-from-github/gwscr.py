import requests
from pprint import pprint


def get_trading_repositories(language, num_repositories, search, sort):
    repositories = []
    page = 1

    while len(repositories) < page:
        if search == 'code' or search == 'topics' or search == 'marketplace':
            url = f"https://api.github.com/search/{search}?q=language:{language}&page={page}"
        else:
            url = f"https://api.github.com/search/{search}?q=language:{language}&sort={sort}&page={page}"

        print(url)
        # response = requests.get(url)
        #
        # if response.status_code == 200:
        #     date = response.json()
        #     pprint(date)
        #     page += 1


search_by = {
    '1': 'code',
    '2': 'repositories',
    '3': 'issues',
    '4': 'pullrequests',
    '5': 'users',
    '6': 'commits',
    '7': 'registrypackages',
    '8': 'wikis',
    '9': 'topics',
    '10': 'marketplace',
}
sorted_by = {
    '1': '&o=desc',
    '2': 'stars&o=desc',
    '3': 'stars&o=asc',
    '4': 'forks&o=desc',
    '5': 'forks&o=asc',
    '6': 'updated&o=desc',
    '7': 'updated&o=asc',
}
language = input('Enter language: ')
num_repositories = int(input('Enter number of repositories:'))
searchby = input('Search By choice a number :\n 1(code), 2(repositories), 3(issues), 4(pullrequests), 5(users),'
                 ' 6(commits), 7(registrypackages), 8(wikis), 9(topics), 10(marketplace)\n >>')

sortedby = input('Filter By choice a number: 1(Best match), 2(Most Star), 3(Fewest Star), 4(Most Forks),'
                 ' 5(Fewest Forks), 6(Recently updated), 7(Least recently updated)\n >>')

repositories = get_trading_repositories(language, num_repositories, search_by[searchby], sorted_by[sortedby])
