from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Base1:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Base2:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class Base3:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class Derived1(Base1):
    pass


@dataclass
class Derived2(Base2):
    bar: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Derived3(Base3):
    pass


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem1: Optional[Derived1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    elem2: Optional[Derived2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    elem3: Optional[Derived3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
