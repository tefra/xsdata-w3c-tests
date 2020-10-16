from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class B:
    """
    :ivar foo_foo:
    :ivar e1:
    :ivar foo:
    """
    foo_foo: List[bool] = field(
        default_factory=list,
        metadata={
            "name": "foo",
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 1000,
        }
    )
    e1: List[bool] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "max_occurs": 1000,
        }
    )
    foo: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 1000,
        }
    )


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Foo:
    """
    :ivar value:
    """
    class Meta:
        name = "foo"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root(B):
    class Meta:
        name = "root"
        namespace = "foo"
