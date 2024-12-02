from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v03"


@dataclass
class EldTimeStampListC:
    class Meta:
        name = "eldTimeStampListC"
        namespace = "http://xstest-tns/schema11_D3_4_28_v03"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "tokens": True,
        },
    )


@dataclass
class DTimeStampRoot:
    class Meta:
        name = "dTimeStampRoot"

    eld_time_stamp_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "eldTimeStampPattern",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
    eld_time_stamp_list_a: list[list[XmlDateTime]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampListA",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "tokens": True,
        },
    )
    eld_time_stamp_list_b: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampListB",
            "type": "Element",
            "namespace": "",
            "tokens": True,
        },
    )
    eld_time_stamp_list_c: Optional[EldTimeStampListC] = field(
        default=None,
        metadata={
            "name": "eldTimeStampListC",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_D3_4_28_v03",
            "required": True,
        },
    )


@dataclass
class Root(DTimeStampRoot):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v03"
