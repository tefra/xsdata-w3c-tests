from dataclasses import dataclass, field
from lxml.etree import QName
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
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class FooType(MyType):
    """
    :ivar local_attributes:
    """
    class Meta:
        name = "fooType"

    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"