# -*- coding: utf-8 -*-
from scrapy import cmdline

name = 'tieba'
# cmd = 'scrapy crawl {0}'.format(name)
cmd = '/Library/Frameworks/Python.framework/Versions/3.4/bin/scrapy  runspider /Users/mugbya/object/B0009-bgdt-scrapy-python/distributed_crawler/distributed_crawler/spiders/{0}.py'.format(name)
# cmd = 'scrapy crawl {0} -o {1}.json'.format(name, name)
cmdline.execute(cmd.split())

