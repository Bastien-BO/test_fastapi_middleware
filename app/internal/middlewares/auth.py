"""
All classes related to authentication
"""

import base64

from starlette.authentication import AuthCredentials
from starlette.authentication import AuthenticationBackend
from starlette.authentication import AuthenticationError

from app.internal.schemas.auth import AuthenticationUser


class AuthBasicOrBearerBackend(AuthenticationBackend):
    """
    Authentication middlewares
    """

    async def authenticate(self, conn) \
            -> tuple[AuthCredentials, AuthenticationUser] | None:
        """
        Verify both authentication method and create User()
        :param conn: Connexion object
        :return: AuthCredentials, SimpleUserTest
        """
        if "Authorization" not in conn.headers:
            # If no authentication header is present
            if conn.scope.get("path") in {"/docs", "/redoc", "/openapi.json"}:
                # No authentication needed
                return
            else:
                raise AuthenticationError('No authentication headers given')

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() == 'bearer':
                # check bearer content and return valid User
                user: dict = {
                    "username": "bearer",
                    "test1": "test1",
                    "test2": "test2"
                }

            elif scheme.lower() == 'basic':

                decoded = base64.b64decode(credentials).decode("ascii")
                username, _, password = decoded.partition(":")
                if username:
                    # check redis here and return User
                    user: dict = {
                        "username": "basic auth",
                        "test1": "test1",
                        "test2": "test2"
                    }
                else:
                    print("error should raise")
                    raise AuthenticationError("You need to provide a username")
            else:
                raise AuthenticationError(
                    "Authentication type is not supported"
                )

        except Exception:
            raise AuthenticationError(
                'Unable to validate given authentication'
            )

        return AuthCredentials(["authenticated"]), AuthenticationUser(**user)
