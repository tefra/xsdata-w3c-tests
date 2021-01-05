from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v04"


@dataclass
class Root:
    """
    :ivar eld_time_union_a:
    :ivar eld_time_union_b:
    :ivar eld_time_union_c: Tests the simpleType dateTime,
        explicitTimezone used in a unions
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v04"

    eld_time_union_a: List[Union[XmlDateTime, str]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeUnionA",
            "type": "Element",
            "namespace": "",
            "explicit_timezone": "required",
        }
    )
    eld_time_union_b: List[Union[XmlDateTime, int]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeUnionB",
            "type": "Element",
            "namespace": "",
            "explicit_timezone": "prohibited",
        }
    )
    eld_time_union_c: List[Union[str, int, XmlDateTime]] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeUnionC",
            "type": "Element",
            "namespace": "",
            "explicit_timezone": "optional",
        }
    )
