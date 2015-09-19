# Scrapy settings for spiders project
SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'
DEFAULT_ITEM_CLASS = 'spiders.items.Website'
ITEM_PIPELINES = {'spiders.pipelines.FilterWordsPipeline': 1}
