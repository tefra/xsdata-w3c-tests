from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


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
        metadata=dict(
            required=True
        )
    )


@dataclass
class RootType:
    """
    :ivar test_element:
    """
    class Meta:
        name = "rootType"

    test_element: Optional[TestElement] = field(
        default=None,
        metadata=dict(
            name="testElement",
            type="Element",
            namespace="http://www.tempuri.org",
            required=True
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"
