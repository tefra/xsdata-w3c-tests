from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestElement:
    class Meta:
        name = "testElement"
        namespace = "http://www.tempuri.org"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_element: Optional[TestElement] = field(
        default=None,
        metadata={
            "name": "testElement",
            "type": "Element",
            "required": True,
        },
    )
