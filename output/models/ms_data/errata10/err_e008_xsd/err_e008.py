from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_token: TestToken = field(
        metadata={
            "name": "testToken",
            "type": "Element",
            "required": True,
        }
    )
