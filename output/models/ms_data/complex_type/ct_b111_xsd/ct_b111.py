from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar attr_test1:
    :ivar attr_test2:
    :ivar any_attributes:
    """
    class Meta:
        name = "fooType"

    attr_test1: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest1",
            type="Attribute"
        )
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest2",
            type="Attribute"
        )
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
