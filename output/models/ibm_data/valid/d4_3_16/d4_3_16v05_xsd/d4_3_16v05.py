from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v05"


class ElEnumerationAValue(Enum):
    VALUE_1999_01_01_T01_01_00_Z = XmlDateTime(1999, 1, 1, 1, 1, 0, 0, 0)
    VALUE_2000_01_01_T01_01_00_01_00 = XmlDateTime(2000, 1, 1, 1, 1, 0, 0, -60)
    VALUE_2001_01_01_T01_01_00_01_00 = XmlDateTime(2001, 1, 1, 1, 1, 0, 0, 60)
    VALUE_2002_01_01_T01_01_00 = XmlDateTime(2002, 1, 1, 1, 1, 0)


class ElEnumerationBValue(Enum):
    VALUE_2003_01_01_T01_01_00 = XmlDateTime(2003, 1, 1, 1, 1, 0)


class ElEnumerationCValue(Enum):
    VALUE_1994_01_01_T01_01_00_Z = XmlDateTime(1994, 1, 1, 1, 1, 0, 0, 0)
    VALUE_2005_01_01_T01_01_00_01_00 = XmlDateTime(2005, 1, 1, 1, 1, 0, 0, -60)
    VALUE_2006_01_01_T01_01_00_01_00 = XmlDateTime(2006, 1, 1, 1, 1, 0, 0, 60)


@dataclass
class ElEnumerationA:
    class Meta:
        name = "elEnumerationA"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional[ElEnumerationAValue] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ElEnumerationB:
    class Meta:
        name = "elEnumerationB"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional[ElEnumerationBValue] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ElEnumerationC:
    class Meta:
        name = "elEnumerationC"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional[ElEnumerationCValue] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    el_enumeration_a: List[ElEnumerationAValue] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationA",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    el_enumeration_b: List[ElEnumerationBValue] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationB",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    el_enumeration_c: List[ElEnumerationCValue] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationC",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
