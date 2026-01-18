from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"

    default_attr: bool = field(
        metadata={
            "name": "defaultAttr",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "required": True,
        }
    )
    e1: Root.E1 = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    e2: Root.E2 = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class E1:
        default_attr: bool = field(
            metadata={
                "name": "defaultAttr",
                "type": "Attribute",
                "namespace": "http://xstest-tns/schema11_S3_4_2_4",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class E2:
        default_attr: bool = field(
            metadata={
                "name": "defaultAttr",
                "type": "Attribute",
                "namespace": "http://xstest-tns/schema11_S3_4_2_4",
                "required": True,
            }
        )
