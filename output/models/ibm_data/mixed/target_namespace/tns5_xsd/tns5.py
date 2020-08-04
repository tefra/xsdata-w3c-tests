from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class TestType:
    """
    :ivar value:
    :ivar any_attributes:
    """
    class Meta:
        name = "TEST_TYPE"

    value: Optional[str] = field(
        default=None,
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class X(TestType):
    """
    :ivar a:
    """
    class Meta:
        name = "x"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://test1"
        )
    )
