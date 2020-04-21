from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class Empty:
    class Meta:
        name = "empty"


@dataclass
class B:
    """
    :ivar foo:
    """
    foo: Optional[Empty] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


@dataclass
class Der:
    """
    :ivar foo:
    """
    foo: Optional[Empty] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


@dataclass
class Dr:
    """
    :ivar foo:
    """
    foo: Optional[Empty] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


@dataclass
class Drr:
    """
    :ivar foo:
    """
    foo: Optional[Empty] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


@dataclass
class De(B):
    pass


@dataclass
class Dre(Dr):
    pass


@dataclass
class Root:
    """
    :ivar item:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    item: List[B] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Dee(De):
    pass
