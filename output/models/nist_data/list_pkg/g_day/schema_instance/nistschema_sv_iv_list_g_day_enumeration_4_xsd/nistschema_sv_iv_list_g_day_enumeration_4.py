from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"


class NistschemaSvIvListGDayEnumeration4Type(Enum):
    VALUE_03_10_23_15_04_12 = (
        XmlPeriod("---03"),
        XmlPeriod("---10"),
        XmlPeriod("---23"),
        XmlPeriod("---15"),
        XmlPeriod("---04"),
        XmlPeriod("---12"),
    )
    VALUE_28_25_05_23_14_05_25 = (
        XmlPeriod("---28"),
        XmlPeriod("---25"),
        XmlPeriod("---05"),
        XmlPeriod("---23"),
        XmlPeriod("---14"),
        XmlPeriod("---05"),
        XmlPeriod("---25"),
    )
    VALUE_08_02_19_29_19_03_22_03 = (
        XmlPeriod("---08"),
        XmlPeriod("---02"),
        XmlPeriod("---19"),
        XmlPeriod("---29"),
        XmlPeriod("---19"),
        XmlPeriod("---03"),
        XmlPeriod("---22"),
        XmlPeriod("---03"),
    )
    VALUE_16_02_07_15_27_01_02_17 = (
        XmlPeriod("---16"),
        XmlPeriod("---02"),
        XmlPeriod("---07"),
        XmlPeriod("---15"),
        XmlPeriod("---27"),
        XmlPeriod("---01"),
        XmlPeriod("---02"),
        XmlPeriod("---17"),
    )
    VALUE_14_08_22_25_18 = (
        XmlPeriod("---14"),
        XmlPeriod("---08"),
        XmlPeriod("---22"),
        XmlPeriod("---25"),
        XmlPeriod("---18"),
    )
    VALUE_27_19_10_22_13 = (
        XmlPeriod("---27"),
        XmlPeriod("---19"),
        XmlPeriod("---10"),
        XmlPeriod("---22"),
        XmlPeriod("---13"),
    )


@dataclass(kw_only=True)
class NistschemaSvIvListGDayEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-4-NS"

    value: NistschemaSvIvListGDayEnumeration4Type = field()
