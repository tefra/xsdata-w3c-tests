from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class B:
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Dr:
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Drr:
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Empty:
    class Meta:
        name = "empty"


@dataclass
class De(B):
    pass


@dataclass
class Dre(Dr):
    pass


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    item1_or_item2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "item1",
                    "type": B,
                },
                {
                    "name": "item2",
                    "type": B,
                },
            ),
        }
    )


@dataclass
class Dee(De):
    pass


@dataclass
class Der(De):
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
