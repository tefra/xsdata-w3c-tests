from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BaseType:
    """
    :ivar base_element:
    :ivar attr:
    """
    class Meta:
        name = "baseType"

    base_element: List[object] = field(
        default_factory=list,
        metadata={
            "name": "baseElement",
            "type": "Element",
            "namespace": "",
        }
    )
    attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DerivedType:
    """
    :ivar base_element:
    :ivar attr:
    """
    class Meta:
        name = "derivedType"

    base_element: List[object] = field(
        default_factory=list,
        metadata={
            "name": "baseElement",
            "type": "Element",
            "namespace": "",
        }
    )
    attr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(DerivedType):
    class Meta:
        name = "root"
