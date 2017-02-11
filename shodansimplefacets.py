#!/user/bin/env python
import shodan
FACETS = [
    ('org',15),
    ('domain',15),
    ('port',15),
    ('asn',10),
    ('country',15),
]
FACETS_TITLES = {
    'org': 'Top 15 organizations',
    'domain': 'Top 15 domains',
    'port': 'Top 15 ports',
    'asn': 'Top 15 autonomous systems',
    'country': 'Top 15 countries',
}
try:
    api = shodan.Shodan("71xqxaeUdz62H4DoNC7LzaLwJ7RhrLBz")
    result = api.count("ngnix",facets=FACETS)
    print 'Total results: %s\n' % result['total']
    for facet in result['facets']:
        print FACETS_TITLES[facet]
        for term in result['facets'][facet]:
            print '%s: %s' %(term['value'],term['count'])
        print ''
except Exception, e:
    print 'Error %s' % e
