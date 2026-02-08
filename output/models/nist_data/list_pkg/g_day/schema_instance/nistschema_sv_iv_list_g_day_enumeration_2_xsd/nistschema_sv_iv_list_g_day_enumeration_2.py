from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-2-NS"


class NistschemaSvIvListGDayEnumeration2Type(Enum):
    VALUE_25_19_22_06_06_20_04 = (
        XmlPeriod("---25"),
        XmlPeriod("---19"),
        XmlPeriod("---22"),
        XmlPeriod("---06"),
        XmlPeriod("---06"),
        XmlPeriod("---20"),
        XmlPeriod("---04"),
    )
    VALUE_25_05_15_08_06_09_26_10_12_15 = (
        XmlPeriod("---25"),
        XmlPeriod("---05"),
        XmlPeriod("---15"),
        XmlPeriod("---08"),
        XmlPeriod("---06"),
        XmlPeriod("---09"),
        XmlPeriod("---26"),
        XmlPeriod("---10"),
        XmlPeriod("---12"),
        XmlPeriod("---15"),
    )
    VALUE_20_15_03_11_06_27_12_18 = (
        XmlPeriod("---20"),
        XmlPeriod("---15"),
        XmlPeriod("---03"),
        XmlPeriod("---11"),
        XmlPeriod("---06"),
        XmlPeriod("---27"),
        XmlPeriod("---12"),
        XmlPeriod("---18"),
    )
    VALUE_25_01_05_06_14_11_24_19 = (
        XmlPeriod("---25"),
        XmlPeriod("---01"),
        XmlPeriod("---05"),
        XmlPeriod("---06"),
        XmlPeriod("---14"),
        XmlPeriod("---11"),
        XmlPeriod("---24"),
        XmlPeriod("---19"),
    )
    VALUE_29_29_20_16_19_26 = (
        XmlPeriod("---29"),
        XmlPeriod("---29"),
        XmlPeriod("---20"),
        XmlPeriod("---16"),
        XmlPeriod("---19"),
        XmlPeriod("---26"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGDayEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-2"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-2-NS"

    value: NistschemaSvIvListGDayEnumeration2Type = field()
