from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BaseType:
    """
    :ivar base_ely:
    :ivar base_attr:
    """
    class Meta:
        name = "baseType"

    base_ely: List[object] = field(
        default_factory=list,
        metadata={
            "name": "baseEly",
            "type": "Element",
            "namespace": "",
        }
    )
    base_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseAttr",
            "type": "Attribute",
        }
    )


@dataclass
class DerivedType(BaseType):
    """
    :ivar derived_attr:
    """
    class Meta:
        name = "derivedType"

    derived_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "derivedAttr",
            "type": "Attribute",
        }
    )


@dataclass
class Root(DerivedType):
    class Meta:
        name = "root"
