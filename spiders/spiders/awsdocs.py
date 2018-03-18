import os
from scrapy.spiders import Spider
from scrapy.selector import Selector
from spiders.items import Website


class AwsDocsSpider(Spider):

    name = "awsdocs"
    scraped_commands = []
    commands = [
        'acm',
        'alexaforbusiness',
        'apigateway',
        'application-autoscaling',
        'appstream',
        'appsync',
        'athena',
        'autoscaling',
        'autoscaling-plans',
        'batch',
        'budgets',
        'ce',
        'cloud9',
        'clouddirectory',
        'cloudformation',
        'cloudfront',
        'cloudhsm',
        'cloudhsmv2',
        'cloudsearch',
        'cloudsearchdomain',
        'cloudtrail',
        'cloudwatch',
        'codebuild',
        'codecommit',
        'codepipeline',
        'codestar',
        'cognito-identity',
        'cognito-idp',
        'cognito-sync',
        'comprehend',
        'configservice',
        'configure',
        'cur',
        'datapipeline',
        'dax',
        'deploy',
        'devicefarm',
        'directconnect',
        'discovery',
        'dms',
        'ds',
        'dynamodb',
        'dynamodbstreams',
        'ec2',
        'ecr',
        'ecs',
        'efs',
        'elasticache',
        'elasticbeanstalk',
        'elastictranscoder',
        'elb',
        'elbv2',
        'emr',
        'es',
        'events',
        'firehose',
        'gamelift',
        'glacier',
        'glue',
        'greengrass',
        'guardduty',
        'health',
        'history',
        'iam',
        'importexport',
        'inspector',
        'iot',
        'iot-data',
        'iot-jobs-data',
        'kinesis',
        'kinesis-video-archived-media',
        'kinesis-video-media',
        'kinesisanalytics',
        'kinesisvideo',
        'kms',
        'lambda',
        'lex-models',
        'lex-runtime',
        'lightsail',
        'logs',
        'machinelearning',
        'marketplace-entitlement',
        'marketplacecommerceanalytics',
        'mediaconvert',
        'medialive',
        'mediapackage',
        'mediastore',
        'mediastore-data',
        'meteringmarketplace',
        'mgh',
        'mobile',
        'mq',
        'mturk',
        'opsworks',
        'opsworks-cm',
        'organizations',
        'pinpoint',
        'polly',
        'pricing',
        'rds',
        'redshift',
        'rekognition',
        'resource-groups',
        'resourcegroupstaggingapi',
        'route53',
        'route53domains',
        's3',
        's3api',
        'sagemaker',
        'sagemaker-runtime',
        'sdb',
        'serverlessrepo',
        'servicecatalog',
        'servicediscovery',
        'ses',
        'shield',
        'sms',
        'snowball',
        'sns',
        'sqs',
        'ssm',
        'stepfunctions',
        'storagegateway',
        'sts',
        'support',
        'swf',
        'transcribe',
        'translate',
        'waf',
        'waf-regional',
        'workdocs',
        'workmail',
        'workspaces',
        'xray',
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
