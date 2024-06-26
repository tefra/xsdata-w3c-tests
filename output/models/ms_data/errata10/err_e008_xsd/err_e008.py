from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestToken:
    class Meta:
        name = "testToken"
        namespace = "http://www.tempuri.org"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_token: Optional[TestToken] = field(
        default=None,
        metadata={
            "name": "testToken",
            "type": "Element",
            "required": True,
        },
    )
