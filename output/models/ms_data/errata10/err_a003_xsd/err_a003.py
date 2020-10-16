from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class RootType:
    """
    :ivar test_element:
    """
    class Meta:
        name = "rootType"

    test_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "testElement",
            "type": "Element",
            "namespace": "http://www.tempuri.org",
            "required": True,
        }
    )


@dataclass
class TestElement:
    """
    :ivar value:
    """
    class Meta:
        name = "testElement"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"
