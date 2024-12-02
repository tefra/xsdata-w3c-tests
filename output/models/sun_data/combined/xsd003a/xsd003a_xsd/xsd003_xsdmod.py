from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    root: list["Root"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    g_att: Optional[str] = field(
        default=None,
        metadata={
            "name": "gAtt",
            "type": "Attribute",
            "namespace": "foo",
        },
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
