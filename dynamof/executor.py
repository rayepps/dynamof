from boto3 import resource, client

PROVIDERS = {
    'resource': lambda url: resource('dynamodb', endpoint_url=url),
    'client': lambda url: client('dynamodb', endpoint_url=url)
}


def execute(url, operation):
    description = operation.get('description')
    provider_name = operation.get('provider')
    runner = operation.get('runner')
    provider = PROVIDERS[provider_name]
    return runner(provider(url))