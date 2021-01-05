from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v03"


@dataclass
class DTimeRoot:
    class Meta:
        name = "dTimeRoot"

    el_dtime_et: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "elDTimeET",
            "type": "Element",
            "namespace": "",
            "required": True,
            "explicit_timezone": "required",
        }
    )
    el_dtime_list_required: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeListRequired",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
            "required": True,
            "explicit_timezone": "required",
            "tokens": True,
        }
    )
    el_dtime_list_prohibited: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeListProhibited",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
            "required": True,
            "explicit_timezone": "prohibited",
            "tokens": True,
        }
    )
    el_dtime_list_optional: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "name": "elDTimeListOptional",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
            "required": True,
            "explicit_timezone": "optional",
            "tokens": True,
        }
    )


@dataclass
class ElDtimeListOptional:
    class Meta:
        name = "elDTimeListOptional"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "optional",
            "tokens": True,
        }
    )


@dataclass
class ElDtimeListProhibited:
    class Meta:
        name = "elDTimeListProhibited"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "prohibited",
            "tokens": True,
        }
    )


@dataclass
class ElDtimeListRequired:
    class Meta:
        name = "elDTimeListRequired"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: List[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "required",
            "tokens": True,
        }
    )


@dataclass
class Root(DTimeRoot):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"
