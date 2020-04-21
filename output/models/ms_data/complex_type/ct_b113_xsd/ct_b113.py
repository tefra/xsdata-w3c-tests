from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class FooType:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "fooType"

    any_attributes: Dict[QName, str] = field(
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
