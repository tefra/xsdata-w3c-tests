from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v05"


@dataclass
class ElEnumerationA:
    """
    :ivar value:
    """
    class Meta:
        name = "elEnumerationA"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional["ElEnumerationA.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE_1999_01_01_T01_01_00_Z:
        :cvar VALUE_2000_01_01_T01_01_00_01_00:
        :cvar VALUE_2001_01_01_T01_01_00_01_00:
        :cvar VALUE_2002_01_01_T01_01_00:
        """
        VALUE_1999_01_01_T01_01_00_Z = "1999-01-01T01:01:00Z"
        VALUE_2000_01_01_T01_01_00_01_00 = "2000-01-01T01:01:00-01:00"
        VALUE_2001_01_01_T01_01_00_01_00 = "2001-01-01T01:01:00+01:00"
        VALUE_2002_01_01_T01_01_00 = "2002-01-01T01:01:00"


@dataclass
class ElEnumerationB:
    """
    :ivar value:
    """
    class Meta:
        name = "elEnumerationB"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional["ElEnumerationB.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE_2003_01_01_T01_01_00:
        """
        VALUE_2003_01_01_T01_01_00 = "2003-01-01T01:01:00"


@dataclass
class ElEnumerationC:
    """
    :ivar value:
    """
    class Meta:
        name = "elEnumerationC"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    value: Optional["ElEnumerationC.Value"] = field(
        default=None,
    )

    class Value(Enum):
        """
        :cvar VALUE_1994_01_01_T01_01_00_Z:
        :cvar VALUE_2005_01_01_T01_01_00_01_00:
        :cvar VALUE_2006_01_01_T01_01_00_01_00:
        """
        VALUE_1994_01_01_T01_01_00_Z = "1994-01-01T01:01:00Z"
        VALUE_2005_01_01_T01_01_00_01_00 = "2005-01-01T01:01:00-01:00"
        VALUE_2006_01_01_T01_01_00_01_00 = "2006-01-01T01:01:00+01:00"


@dataclass
class Root:
    """
    :ivar el_enumeration_a:
    :ivar el_enumeration_b:
    :ivar el_enumeration_c:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v05"

    el_enumeration_a: List["Root.Value"] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationA",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    el_enumeration_b: List["Root.Value"] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationB",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    el_enumeration_c: List["Root.Value"] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationC",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )

    class Value(Enum):
        """
        :cvar VALUE_1999_01_01_T01_01_00_Z:
        :cvar VALUE_2000_01_01_T01_01_00_01_00:
        :cvar VALUE_2001_01_01_T01_01_00_01_00:
        :cvar VALUE_2002_01_01_T01_01_00:
        """
        VALUE_1999_01_01_T01_01_00_Z = "1999-01-01T01:01:00Z"
        VALUE_2000_01_01_T01_01_00_01_00 = "2000-01-01T01:01:00-01:00"
        VALUE_2001_01_01_T01_01_00_01_00 = "2001-01-01T01:01:00+01:00"
        VALUE_2002_01_01_T01_01_00 = "2002-01-01T01:01:00"
