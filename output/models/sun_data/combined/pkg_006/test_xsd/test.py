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
class EB(B):
    class Meta:
        name = "eB"
        namespace = "foo"


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


@dataclass
class EDe(De):
    class Meta:
        name = "eDe"
        namespace = "foo"


@dataclass
class EDr(Dr):
    class Meta:
        name = "eDr"
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
class EDre(Dre):
    class Meta:
        name = "eDre"
        namespace = "foo"


@dataclass
class EDrr(Drr):
    class Meta:
        name = "eDrr"
        namespace = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    e_dee: List[EDee] = field(
        default_factory=list,
        metadata={
            "name": "eDee",
            "type": "Element",
        }
    )
    e_der: List[EDer] = field(
        default_factory=list,
        metadata={
            "name": "eDer",
            "type": "Element",
        }
    )
    e_de: List[EDe] = field(
        default_factory=list,
        metadata={
            "name": "eDe",
            "type": "Element",
        }
    )
    e_dre: List[EDre] = field(
        default_factory=list,
        metadata={
            "name": "eDre",
            "type": "Element",
        }
    )
    e_drr: List[EDrr] = field(
        default_factory=list,
        metadata={
            "name": "eDrr",
            "type": "Element",
        }
    )
    e_dr: List[EDr] = field(
        default_factory=list,
        metadata={
            "name": "eDr",
            "type": "Element",
        }
    )
    e_b: List[EB] = field(
        default_factory=list,
        metadata={
            "name": "eB",
            "type": "Element",
        }
    )
