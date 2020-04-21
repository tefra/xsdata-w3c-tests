from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class FooType:
    """
    :ivar value:
    :ivar attr_test1:
    :ivar attr_test2:
    """
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
    )
    attr_test1: Optional[int] = field(
        default=None,
        metadata=dict(
            name="attrTest1",
            type="Attribute",
            namespace="a"
        )
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest2",
            type="Attribute",
            namespace="a"
        )
    )


@dataclass
class Mytype1:
    """
    :ivar value:
    :ivar attr_test1:
    :ivar attr_test2:
    """
    class Meta:
        name = "mytype1"

    value: Optional[str] = field(
        default=None,
    )
    attr_test1: Optional[int] = field(
        default=None,
        metadata=dict(
            name="attrTest1",
            type="Attribute",
            namespace="a"
        )
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest2",
            type="Attribute",
            namespace="a"
        )
    )
