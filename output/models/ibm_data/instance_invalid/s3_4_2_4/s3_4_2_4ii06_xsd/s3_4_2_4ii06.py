from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class C1:
    class Meta:
        name = "c1"

    default_attr: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultAttr",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "required": True,
        },
    )
    element1: Optional[object] = field(
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
    element_added: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
        },
    )
