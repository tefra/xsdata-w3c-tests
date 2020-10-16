from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Base:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "base"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Rst:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "rst"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Ext(Base):
    """
    :ivar d:
    :ivar e:
    """
    class Meta:
        name = "ext"

    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar item:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    item: List[Base] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
