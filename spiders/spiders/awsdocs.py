import os
from scrapy.spiders import Spider
from scrapy.selector import Selector
from spiders.items import Website


class AwsDocsSpider(Spider):

    name = "awsdocs"
    scraped_commands = []
    commands = [
        'autoscaling',
        'cloudformation',
        'cloudfront',
        'cloudhsm',
        'cloudsearch',
        'cloudsearchdomain',
        'cloudtrail',
        'cloudwatch',
        'codecommit',
        'codepipeline',
        'cognito-identity',
        'cognito-sync',
        'configservice',
        'configure',
        'datapipeline',
        'deploy',
        'devicefarm',
        'directconnect',
        'ds',
        'dynamodb',
        'dynamodbstreams',
        'ec2',
        'ecs',
        'efs',
        'elasticache',
        'elasticbeanstalk',
        'elastictranscoder',
        'elb',
        'emr',
        'es',
        'glacier',
        'iam',
        'importexport',
        'kinesis',
        'kms',
        'lambda',
        'logs',
        'machinelearning',
        'opsworks',
        'rds',
        'redshift',
        'route53',
        'route53domains',
        's3',
        's3api',
        'sdb',
        'ses',
        'sns',
        'sqs',
        'ssm',
        'storagegateway',
        'sts',
        'support',
        'swf',
        'workspaces',
    ]
    global_options = [
        '--debug',
        '--endpoint-url',
        '--no-verify-ssl',
        '--no-paginate',
        '--output',
        '--profile',
        '--region',
        '--version',
        '--color',
        '--query',
        '--no-sign-request',
    ]
    resource_options = [
        '--instance-ids',
        '--bucket',
        '--cluster-states',
    ]
    base_url = 'http://docs.aws.amazon.com/cli/latest/reference/'
    index_url = '/index.html'
    start_urls = []
    for command in commands:
        start_urls.append(base_url + str(command) + index_url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="toctree-wrapper compound"]/ul/li')
        items = []
        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            items.append(item)
        self.scraped_commands.extend(items)
        return items

    def handle_closed(self):
        SOURCES_DIR = os.path.dirname(os.path.realpath(__file__))
        SOURCES_PATH = os.path.join(SOURCES_DIR, 'data/AWSDOCS.txt')
        with open(SOURCES_PATH, 'w') as f:
            commands = self.commands
            scraped_commands = []
            for item in self.scraped_commands:
                scraped_commands.append(str(item['name'][0]))
            commands = sorted(list(set(commands)))
            scraped_commands = sorted(list(set(scraped_commands)))
            global_options = sorted(list(set(self.global_options)))
            resource_options = sorted(list(set(self.resource_options)))
            f.write('[commands]: ' + \
                str(len(commands)) + '\n')
            for item in commands:
                f.write(item + '\n')
            f.write('[sub_commands]: ' + \
                str(len(scraped_commands)) + '\n')
            for item in scraped_commands:
                f.write(item + '\n')
            f.write('[global_options]: ' + \
                str(len(global_options)) + '\n')
            for item in global_options:
                f.write(item + '\n')
            f.write('[resource_options]: ' + \
                str(len(resource_options)) + '\n')
            for item in resource_options:
                f.write(item + '\n')
