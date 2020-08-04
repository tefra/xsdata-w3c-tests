from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class FooType:
    """
    :ivar value:
    :ivar any_attributes:
    """
    class Meta:
        name = "fooType"

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
class Root(FooType):
    class Meta:
        name = "root"
