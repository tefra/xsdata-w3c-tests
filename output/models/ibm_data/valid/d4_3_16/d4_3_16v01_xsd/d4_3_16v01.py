from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v01"

    el_dtime_type: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeType",
            "type": "Element",
            "namespace": "",
        }
    )
    el_dtime_etprohibited: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeETProhibited",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "explicit_timezone": "prohibited",
        }
    )
    el_dtime_etrequired: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeETRequired",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "explicit_timezone": "required",
        }
    )
    el_dtime_etoptional: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeETOptional",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "explicit_timezone": "optional",
        }
    )
