from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-5-NS"


class NistschemaSvIvListGDayEnumeration5Type(Enum):
    VALUE_25_07_16_11_11_23_19 = (
        XmlPeriod("---25"),
        XmlPeriod("---07"),
        XmlPeriod("---16"),
        XmlPeriod("---11"),
        XmlPeriod("---11"),
        XmlPeriod("---23"),
        XmlPeriod("---19"),
    )
    VALUE_26_28_21_11_16_02_03_25 = (
        XmlPeriod("---26"),
        XmlPeriod("---28"),
        XmlPeriod("---21"),
        XmlPeriod("---11"),
        XmlPeriod("---16"),
        XmlPeriod("---02"),
        XmlPeriod("---03"),
        XmlPeriod("---25"),
    )
    VALUE_30_24_06_08_30_23_02 = (
        XmlPeriod("---30"),
        XmlPeriod("---24"),
        XmlPeriod("---06"),
        XmlPeriod("---08"),
        XmlPeriod("---30"),
        XmlPeriod("---23"),
        XmlPeriod("---02"),
    )
    VALUE_12_25_26_29_13_24_26_01_26 = (
        XmlPeriod("---12"),
        XmlPeriod("---25"),
        XmlPeriod("---26"),
        XmlPeriod("---29"),
        XmlPeriod("---13"),
        XmlPeriod("---24"),
        XmlPeriod("---26"),
        XmlPeriod("---01"),
        XmlPeriod("---26"),
    )
    VALUE_24_16_12_07_10_27_18_28 = (
        XmlPeriod("---24"),
        XmlPeriod("---16"),
        XmlPeriod("---12"),
        XmlPeriod("---07"),
        XmlPeriod("---10"),
        XmlPeriod("---27"),
        XmlPeriod("---18"),
        XmlPeriod("---28"),
    )
    VALUE_18_10_19_18_06_21_17_14_17_22 = (
        XmlPeriod("---18"),
        XmlPeriod("---10"),
        XmlPeriod("---19"),
        XmlPeriod("---18"),
        XmlPeriod("---06"),
        XmlPeriod("---21"),
        XmlPeriod("---17"),
        XmlPeriod("---14"),
        XmlPeriod("---17"),
        XmlPeriod("---22"),
    )


@dataclass
class NistschemaSvIvListGDayEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-5-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration5Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
