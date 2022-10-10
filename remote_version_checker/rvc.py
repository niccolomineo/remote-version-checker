"""Remote Version Checker."""

import sys

import httpx

from remote_version_checker.config import START_ID, URL

MAX_VERSIONS_TO_CHECK = 50

def check_version_remotely() -> None:
    """Check available versions from the remote URL."""
    versions_checked = 0
    msg_max_versions_to_check_reached = "A newer version seems not to be available."
    for i in range(START_ID):
        r = httpx.head(URL.format(i))
        if versions_checked == MAX_VERSIONS_TO_CHECK:
            sys.stdout.write(msg_max_versions_to_check_reached)
            exit()
        if r.status_code == 200:
            versions_checked = 0
            sys.stdout.write(URL.format(i))
        else:
            versions_checked += 1

if __name__ == "__main__":
    check_version_remotely()
