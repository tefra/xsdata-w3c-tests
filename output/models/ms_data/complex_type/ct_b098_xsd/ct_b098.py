from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar attr_test:
    :ivar any_attributes:
    """
    class Meta:
        name = "fooType"

    attr_test: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attrTest",
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
