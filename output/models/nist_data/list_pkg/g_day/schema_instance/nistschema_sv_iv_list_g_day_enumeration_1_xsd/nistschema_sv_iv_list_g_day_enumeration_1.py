from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-enumeration-1-NS"


class NistschemaSvIvListGDayEnumeration1Type(Enum):
    VALUE_17_30_09_01_05_09_09_30 = (
        XmlPeriod("---17"),
        XmlPeriod("---30"),
        XmlPeriod("---09"),
        XmlPeriod("---01"),
        XmlPeriod("---05"),
        XmlPeriod("---09"),
        XmlPeriod("---09"),
        XmlPeriod("---30"),
    )
    VALUE_21_30_16_07_18_25_02 = (
        XmlPeriod("---21"),
        XmlPeriod("---30"),
        XmlPeriod("---16"),
        XmlPeriod("---07"),
        XmlPeriod("---18"),
        XmlPeriod("---25"),
        XmlPeriod("---02"),
    )
    VALUE_26_04_07_18_19 = (
        XmlPeriod("---26"),
        XmlPeriod("---04"),
        XmlPeriod("---07"),
        XmlPeriod("---18"),
        XmlPeriod("---19"),
    )
    VALUE_13_16_08_16_04 = (
        XmlPeriod("---13"),
        XmlPeriod("---16"),
        XmlPeriod("---08"),
        XmlPeriod("---16"),
        XmlPeriod("---04"),
    )
    VALUE_23_20_28_28_07_09_25_11_06 = (
        XmlPeriod("---23"),
        XmlPeriod("---20"),
        XmlPeriod("---28"),
        XmlPeriod("---28"),
        XmlPeriod("---07"),
        XmlPeriod("---09"),
        XmlPeriod("---25"),
        XmlPeriod("---11"),
        XmlPeriod("---06"),
    )


@dataclass
class NistschemaSvIvListGDayEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-gDay-enumeration-1-NS"

    value: Optional[NistschemaSvIvListGDayEnumeration1Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
