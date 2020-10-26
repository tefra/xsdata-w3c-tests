from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class B:
    """
    :ivar foo_or_e1_or_foo:
    """
    foo_or_e1_or_foo: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": bool,
                    "namespace": "foo",
                },
                {
                    "name": "e1",
                    "type": bool,
                    "namespace": "foo",
                },
                {
                    "name": "foo",
                    "type": int,
                    "namespace": "",
                },
            ),
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
