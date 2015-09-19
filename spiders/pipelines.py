from scrapy import signals


class FilterWordsPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
         pipeline = cls()
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        spider.handle_closed()

    def process_item(self, item, spider):
        return item