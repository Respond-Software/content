from typing import Dict, Tuple, List

import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *

import urllib3
import traceback

# Disable insecure warnings
urllib3.disable_warnings()


class Client:
    """
    bla bla
    """
    def __init__(self, params):
        self.cs_client = CrowdStrikeClient(params=params)

    def check_quota_status(self):
        return self.cs_client.check_quota_status()

    def file(self):
        pass

    def ip(self):
        pass

    def url(self):
        pass

    def domain(self):
        pass

    def cs_actors(self):
        pass

    def cs_indicators(self):
        pass

    def cs_reports(self):
        pass

    def cs_report_pdf(self):
        pass


def test_module(client: Client):
    """
    If a client was made then an accesses token was successfully reached,
    therefor the username and password are valid and a connection was made
    additionally, checks if not using all the optional quota
    :param client: the client object with an access token
    :return: ok if got a valid accesses token and not all the quota is used at the moment
    """
    output = client.check_quota_status()

    error = output.get("errors")
    if error:
        return error[0]

    meta = output.get("meta")
    if meta is not None:
        quota = meta.get("quota")
        if quota is not None:
            total = quota.get("total")
            used = quota.get("used")
            if total <= used:
                raise Exception(f"Quota limitation has been reached: {used}")
            else:
                return 'ok'
    raise Exception("Quota limitation is unreachable")


def file_command(client: Client):
    pass


def ip_command(client: Client):
    pass


def url_command(client: Client):
    pass


def domain_command(client: Client):
    pass


def cs_actors_command(client: Client):
    pass


def cs_indicators_command(client: Client):
    pass


def cs_reports_command(client: Client):
    pass


def cs_report_pdf_command(client: Client):
    pass


def main():
    params = demisto.params()
    try:
        command = demisto.command()
        LOG(f'Command being called in CrowdStrikeFalconX Sandbox is: {command}')
        client = Client(params=params)
        if command == 'test-module':
            return_results(test_module(client))
        elif command == 'file':
            return_results(file_command(client))
        elif command == 'ip':
            return_results(ip_command(client))
        elif command == 'url':
            return_results(url_command(client))
        elif command == 'domain':
            return_results(domain_command(client))
        elif command == 'cs-actors':
            return_results(cs_actors_command(client))
        elif command == 'cs-indicators':
            return_results(cs_indicators_command(client))
        elif command == 'cs-reports':
            return_results(cs_reports_command(client))
        elif command == 'cs-report-pdf':
            return_results(cs_report_pdf_command(client))  # Might not be needed
        else:
            raise NotImplementedError(f'{command} is not an existing CrowdStrike Falcon Intel command')
    except Exception as err:
        return_error(f'Unexpected error:\n{str(err)}', error=traceback.format_exc())


from CrowdStrikeApiModule import *  # noqa: E402

if __name__ in ['__main__', 'builtin', 'builtins']:
    main()
