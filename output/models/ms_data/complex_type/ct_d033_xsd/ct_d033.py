from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MyType:
    """
    :ivar value:
    :ivar any_attributes:
    """
    class Meta:
        name = "myType"

    value: Optional[str] = field(
        default=None,
    )
    any_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class FooType(MyType):
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "fooType"

    local_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
