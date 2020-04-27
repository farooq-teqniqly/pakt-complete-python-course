"""
How to avoid mutable default parameters issue.
"""
from typing import List


def create_account(account_type: str, holder: str, account_holders: List[str] = None):
    if account_holders is None:
        account_holders = []

    account_holders.append(holder)

    return {
        "type": account_type,
        "holder": holder,
        "account_holders": account_holders
    }


if __name__ == "__main__":
    account1 = create_account("checking", "Farooq")
    account2 = create_account("savings", "Emily")

    print(account2)
