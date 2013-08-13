#!/usr/bin/env python

import mtwr

if __name__ == "__main__":
	test_urls = [
		'https://www.google.com',
		'https://www.yahoo.com',
		'http://www.flickr.com',
		'http://www.microsoft.com',
		'http://www.amazon.com',
		'http://www.python.org',
		'http://www.stackoverflow.com',
		'ftp://mirrors.kernel.org/'
	]

	import time
	start = time.clock()
	results = mtwr.request_urls(test_urls, timeout=15, force_ipv4=True)
	print '%d requests in %f seconds' % (len(test_urls), time.clock() - start)

	for url, data in results.iteritems():
		print '%s: [%s...] (%d bytes)' % (url, data[:8].replace('\r', '\\r').replace('\n', '\\n'), len(data))
