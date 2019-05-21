mtwr - Multi-Threaded Web Requests [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=shazbits_mtwr&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=shazbits_mtwr)
==================================

Simple python module that exposes a single function to execute web requests in parallel.

It supports http, https, ftp. IPv4 can be forced in case IPv6 causes slow requests.

Tested with python 2.7.2.

## Usage

```python
import mtwr
urls = ['https://www.google.com', 'http://www.python.org', 'ftp://mirrors.kernel.org']
results = mtwr.request_urls(urls, timeout=15, force_ipv4=True)
# {url1: data1, url2: data2, ...}
```

## ISC License

https://github.com/shazbits/mtwr/blob/master/LICENSE.txt

Romain Dura

http://www.shazbits.com
