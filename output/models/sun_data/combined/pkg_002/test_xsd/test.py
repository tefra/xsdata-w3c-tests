from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Empty:
    class Meta:
        name = "empty"


@dataclass
class B:
    foo: Optional[Empty] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass
class De(B):
    pass


@dataclass
class Dr(B):
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


@dataclass
class Dre(Dr):
    pass


@dataclass
class Drr(Dr):
    pass
