from typing import Union

from fastapi.openapi.models import HTTPBase as HTTPBaseModel
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.security.base import SecurityBase


class HTTPBaseLight(SecurityBase):
    """
    Generate an openapi
    """

    def __init__(
        self,
        scheme: str,
        scheme_name: Union[str, None] = None,
        description: Union[str, None] = None,
    ):
        """
        Used to generate openapi documentation
        :param scheme: scheme name
        :param scheme_name: scheme openapi display name
        :param description: Small description displayed in open api documentation
        """
        print("toto")
        # is called at openapi generation (at api start)
        self.description = description
        if scheme == "basic":
            self.model = HTTPBaseModel(scheme="basic", description=description)
        elif scheme == "bearer":
            self.model = HTTPBearerModel(scheme="bearer", description=description)
        else:
            raise ValueError("scheme vaue should be equal to 'basic' or 'bearer'")
        self.scheme = scheme
        self.scheme_name = scheme_name or scheme

    def __call__(self):
        print("tata")
        # Is called every route call
        pass
