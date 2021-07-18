from definitions import CONFIG_PATH
import yaml

HOSTED_ZONE_ID = "hosted_zone_id"
FILE_NAME = "hosted_zone.yml"

class HostedZone:

    cached_hosted_zone = None

    def __init__(self) -> None:
        with open(CONFIG_PATH + FILE_NAME, 'r') as stream:
            try:
                self.cached_hosted_zone = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                raise Exception("Couldn't get hosted zone!" + exc)

    def get_hosted_zone_id(self) -> str:
        return self.cached_hosted_zone[HOSTED_ZONE_ID]
