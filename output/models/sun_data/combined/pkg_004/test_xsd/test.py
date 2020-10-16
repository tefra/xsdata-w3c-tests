from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class B:
    """
    :ivar foo:
    """
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
    """
    :ivar foo:
    """
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
    """
    :ivar foo:
    """
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
    """
    :ivar item1:
    :ivar item2:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    item1: List[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item2: List[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Dee(De):
    pass


@dataclass
class Der(De):
    """
    :ivar foo:
    """
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )
