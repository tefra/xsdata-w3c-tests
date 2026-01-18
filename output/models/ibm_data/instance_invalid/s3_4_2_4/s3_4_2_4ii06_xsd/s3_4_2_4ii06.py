from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass(kw_only=True)
class C1:
    class Meta:
        name = "c1"

    default_attr: bool = field(
        metadata={
            "name": "defaultAttr",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "required": True,
        }
    )
    element1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
        },
    )
    element2: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "min_occurs": 1,
        },
    )
    element_added: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
        },
    )
