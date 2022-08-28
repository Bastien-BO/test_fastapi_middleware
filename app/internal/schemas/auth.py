"""
User authentication classes
"""

from starlette.authentication import BaseUser


class AuthenticationUser(BaseUser):
    """
    user object added to request.user
    """

    def __init__(self, username: str, test1: str, test2: str) -> None:
        self.username = username
        self.test1 = test1
        self.test2 = test2

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        raise NotImplementedError()  # pragma: no cover

    @property
    def identity(self) -> str:
        raise NotImplementedError()  # pragma: no cover
