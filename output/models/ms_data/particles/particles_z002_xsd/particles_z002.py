from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional


@dataclass
class Base1:
    """
    :ivar foo:
    """
    foo: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Base2:
    """
    :ivar foo:
    :ivar local_attributes:
    """
    foo: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Base3:
    """
    :ivar foo:
    :ivar local_attributes:
    """
    foo: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    local_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local"
        )
    )


@dataclass
class Derived1(Base1):
    pass


@dataclass
class Derived2(Base2):
    """
    :ivar bar:
    """
    bar: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Derived3(Base3):
    pass


@dataclass
class Doc:
    """
    :ivar elem1:
    :ivar elem2:
    :ivar elem3:
    """
    class Meta:
        name = "doc"

    elem1: Optional[Derived1] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    elem2: Optional[Derived2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    elem3: Optional[Derived3] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
