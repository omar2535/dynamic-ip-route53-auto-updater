from definitions import CONFIG_PATH
import yaml

ASSUMED_ROLE_ARN_KEY = "assumed_role_arn"
AWS_ACCESS_KEY_ID = "aws_access_key_id"
AWS_SECRET_ACCESS_KEY = "aws_secret_access_key"
AWS_SESSION_TOKEN = "aws_session_token"
FILE_NAME = "creds.yml"

class Credentials:

    cached_credentials = None

    def __init__(self) -> None:
        with open(CONFIG_PATH + FILE_NAME, 'r') as stream:
            try:
                self.cached_credentials = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise Exception("Couldn't get credentials!" + exc)

    def get_assumed_role_arn(self) -> str:
        return self.cached_credentials[ASSUMED_ROLE_ARN_KEY]

    def get_aws_access_key_id(self) -> str:
        return self.cached_credentials[AWS_ACCESS_KEY_ID]

    def get_aws_secret_access_key(self) -> str:
        return self.cached_credentials[AWS_SECRET_ACCESS_KEY]
    
    def get_aws_session_token(self) -> str:
        return self.cached_credentials[AWS_SESSION_TOKEN]
