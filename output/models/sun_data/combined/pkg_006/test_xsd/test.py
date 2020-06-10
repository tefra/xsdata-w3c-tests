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
class EB(B):
    class Meta:
        name = "eB"
        namespace = "foo"


@dataclass
class EDr(Dr):
    class Meta:
        name = "eDr"
        namespace = "foo"


@dataclass
class EDrr(Drr):
    class Meta:
        name = "eDrr"
        namespace = "foo"


@dataclass
class Dee(De):
    pass


@dataclass
class Der(De):
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
class EDe(De):
    class Meta:
        name = "eDe"
        namespace = "foo"


@dataclass
class EDre(Dre):
    class Meta:
        name = "eDre"
        namespace = "foo"


@dataclass
class EDee(Dee):
    class Meta:
        name = "eDee"
        namespace = "foo"


@dataclass
class EDer(Der):
    class Meta:
        name = "eDer"
        namespace = "foo"


@dataclass
class Root:
    """
    :ivar e_dee:
    :ivar e_der:
    :ivar e_de:
    :ivar e_dre:
    :ivar e_drr:
    :ivar e_dr:
    :ivar e_b:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    e_dee: List[EDee] = field(
        default_factory=list,
        metadata=dict(
            name="eDee",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_der: List[EDer] = field(
        default_factory=list,
        metadata=dict(
            name="eDer",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_de: List[EDe] = field(
        default_factory=list,
        metadata=dict(
            name="eDe",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_dre: List[EDre] = field(
        default_factory=list,
        metadata=dict(
            name="eDre",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_drr: List[EDrr] = field(
        default_factory=list,
        metadata=dict(
            name="eDrr",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_dr: List[EDr] = field(
        default_factory=list,
        metadata=dict(
            name="eDr",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e_b: List[EB] = field(
        default_factory=list,
        metadata=dict(
            name="eB",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
