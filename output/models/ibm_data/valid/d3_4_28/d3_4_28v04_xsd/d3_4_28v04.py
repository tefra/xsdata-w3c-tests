from dataclasses import dataclass, field
from typing import Union

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v04"


@dataclass
class Root:
    """
    :ivar eld_time_stamp_union_a:
    :ivar eld_time_stamp_union_b:
    :ivar eld_time_stamp_union_c: Tests the simpleType dateTimeStamp
        used in a unions
    """

    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v04"

    eld_time_stamp_union_a: list[Union[XmlDateTime, str]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampUnionA",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    eld_time_stamp_union_b: list[Union[XmlDateTime, int]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampUnionB",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    eld_time_stamp_union_c: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampUnionC",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
