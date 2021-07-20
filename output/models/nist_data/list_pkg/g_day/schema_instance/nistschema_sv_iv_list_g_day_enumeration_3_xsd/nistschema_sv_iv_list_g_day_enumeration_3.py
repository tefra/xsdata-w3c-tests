from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-3-NS"


class NistschemaSvIvListGDayEnumeration3Type(Enum):
    VALUE_21_08_18_30_15_29_09_10_30_30 = (
            XmlPeriod("---21"),
            XmlPeriod("---08"),
            XmlPeriod("---18"),
            XmlPeriod("---30"),
            XmlPeriod("---15"),
            XmlPeriod("---29"),
            XmlPeriod("---09"),
            XmlPeriod("---10"),
            XmlPeriod("---30"),
            XmlPeriod("---30"),
        )
    VALUE_13_14_22_29_18_12 = (
            XmlPeriod("---13"),
            XmlPeriod("---14"),
            XmlPeriod("---22"),
            XmlPeriod("---29"),
            XmlPeriod("---18"),
            XmlPeriod("---12"),
        )
    VALUE_24_11_17_19_06_02 = (
            XmlPeriod("---24"),
            XmlPeriod("---11"),
            XmlPeriod("---17"),
            XmlPeriod("---19"),
            XmlPeriod("---06"),
            XmlPeriod("---02"),
        )
    VALUE_12_16_08_19_26_28_08_14_02_04 = (
            XmlPeriod("---12"),
            XmlPeriod("---16"),
            XmlPeriod("---08"),
            XmlPeriod("---19"),
            XmlPeriod("---26"),
            XmlPeriod("---28"),
            XmlPeriod("---08"),
            XmlPeriod("---14"),
            XmlPeriod("---02"),
            XmlPeriod("---04"),
        )
    VALUE_25_05_05_14_23_17_30 = (
            XmlPeriod("---25"),
            XmlPeriod("---05"),
            XmlPeriod("---05"),
            XmlPeriod("---14"),
            XmlPeriod("---23"),
            XmlPeriod("---17"),
            XmlPeriod("---30"),
        )
    VALUE_16_28_16_29_02_14 = (
            XmlPeriod("---16"),
            XmlPeriod("---28"),
            XmlPeriod("---16"),
            XmlPeriod("---29"),
            XmlPeriod("---02"),
            XmlPeriod("---14"),
        )
    VALUE_30_02_22_14_18_12_16_27 = (
            XmlPeriod("---30"),
            XmlPeriod("---02"),
            XmlPeriod("---22"),
            XmlPeriod("---14"),
            XmlPeriod("---18"),
            XmlPeriod("---12"),
            XmlPeriod("---16"),
            XmlPeriod("---27"),
        )
    VALUE_09_09_08_01_23_25_16_27_29 = (
            XmlPeriod("---09"),
            XmlPeriod("---09"),
            XmlPeriod("---08"),
            XmlPeriod("---01"),
            XmlPeriod("---23"),
            XmlPeriod("---25"),
            XmlPeriod("---16"),
            XmlPeriod("---27"),
            XmlPeriod("---29"),
        )
    VALUE_18_29_16_28_13_15_06_23_21 = (
            XmlPeriod("---18"),
            XmlPeriod("---29"),
            XmlPeriod("---16"),
            XmlPeriod("---28"),
            XmlPeriod("---13"),
            XmlPeriod("---15"),
            XmlPeriod("---06"),
            XmlPeriod("---23"),
            XmlPeriod("---21"),
        )


@dataclass
class NistschemaSvIvListGDayEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-3"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-3-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration3Type] = field(
        default=None
    )
