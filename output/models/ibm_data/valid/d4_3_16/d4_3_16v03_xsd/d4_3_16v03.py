from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v03"


@dataclass(kw_only=True)
class ElDtimeListOptional:
    class Meta:
        name = "elDTimeListOptional"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "optional",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ElDtimeListProhibited:
    class Meta:
        name = "elDTimeListProhibited"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "prohibited",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class ElDtimeListRequired:
    class Meta:
        name = "elDTimeListRequired"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"

    value: list[XmlDateTime] = field(
        default_factory=list,
        metadata={
            "explicit_timezone": "required",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class DTimeRoot:
    class Meta:
        name = "dTimeRoot"

    el_dtime_et: XmlDateTime = field(
        metadata={
            "name": "elDTimeET",
            "type": "Element",
            "namespace": "",
            "explicit_timezone": "required",
        }
    )
    el_dtime_list_required: ElDtimeListRequired = field(
        metadata={
            "name": "elDTimeListRequired",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
        }
    )
    el_dtime_list_prohibited: ElDtimeListProhibited = field(
        metadata={
            "name": "elDTimeListProhibited",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
        }
    )
    el_dtime_list_optional: ElDtimeListOptional = field(
        metadata={
            "name": "elDTimeListOptional",
            "type": "Element",
            "namespace": "http://xstest-tns/schema11_F4_3_16_v03",
        }
    )


@dataclass(kw_only=True)
class Root(DTimeRoot):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v03"
