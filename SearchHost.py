#!/user/bin/env python
import shodan
def ShodanTest():
    try:
        ShodanKeyString = ""
        ShodanApi = shodan.Shodan(ShodanKeyString)
        results = ShodanApi.host("8.8.8.8")
        for result in results:
            print '%s : %s' % (result, results[result])
    except shodan.APIError, e:
        print 'Error %s' % e
if __name__ == "__main__":
    ShodanTest()
