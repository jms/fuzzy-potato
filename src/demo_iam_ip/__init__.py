import boto3
import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig


def get_secret():
    client = botocore.session.get_session().create_client('secretsmanager')
    cache_config = SecretCacheConfig()
    cache = SecretCache(config=cache_config, client=client)
    secret = cache.get_secret_string('my-secret-name')
    print(secret)


def get_parameter():
    client = boto3.client('ssm')
    response = client.get_parameter(
        Name='/autocomplete/devops/api_password',
        WithDecryption=True,
    )
    print(response)


def main() -> int:
    print("Hello from demo-iam-ip!")
    get_parameter()
    return 0
