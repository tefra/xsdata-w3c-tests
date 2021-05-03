from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class B:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Dr:
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class Drr:
    foo: Optional[object] = field(
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

    item: List[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Dee(De):
    pass


@dataclass
class Der(De):
    pass
