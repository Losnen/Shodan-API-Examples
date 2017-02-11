#!/user/bin/env python
import shodan
def ShodanTest():
    try:
        ShodanKeyString = ""
        ShodanApi = shodan.Shodan(ShodanKeyString)
        info = ShodanApi.info()
        for inf in info:
            print '%s: %s' % (inf,info[inf])
    except shodan.APIError, e:
        print 'Error %s' % e
if __name__ == "__main__":
    ShodanTest()
