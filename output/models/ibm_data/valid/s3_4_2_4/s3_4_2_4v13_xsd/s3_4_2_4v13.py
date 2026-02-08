from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass(kw_only=True)
class AttrGoupType:
    class Meta:
        name = "attrGoupType"

    default_attr1: bool = field(
        metadata={
            "name": "defaultAttr1",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
        }
    )
    default_attr2: bool = field(
        metadata={
            "name": "defaultAttr2",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
        }
    )


@dataclass(kw_only=True)
class Root(AttrGoupType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"
