from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass(kw_only=True)
class TestElement:
    class Meta:
        name = "testElement"
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

    test_element: TestElement = field(
        metadata={
            "name": "testElement",
            "type": "Element",
            "required": True,
        }
    )
