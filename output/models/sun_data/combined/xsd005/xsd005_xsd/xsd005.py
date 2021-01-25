from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Base:
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
class Ext(Base):
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


@dataclass
class Rst(Base):
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
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
