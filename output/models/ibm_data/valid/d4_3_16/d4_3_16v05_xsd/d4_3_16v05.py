from enum import Enum
from dataclasses import dataclass, field
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

    value: Optional["ElEnumerationA.Type"] = field(
        default=None,
    )

    class Type(Enum):
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

    value: Optional["ElEnumerationB.Type"] = field(
        default=None,
    )

    class Type(Enum):
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

    value: Optional["ElEnumerationC.Type"] = field(
        default=None,
    )

    class Type(Enum):
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

    el_enumeration_a: List[ElEnumerationA] = field(
        default_factory=list,
        metadata=dict(
            name="elEnumerationA",
            type="Element",
            min_occurs=1,
            max_occurs=4
        )
    )
    el_enumeration_b: List[ElEnumerationB] = field(
        default_factory=list,
        metadata=dict(
            name="elEnumerationB",
            type="Element",
            min_occurs=1,
            max_occurs=3
        )
    )
    el_enumeration_c: List[ElEnumerationC] = field(
        default_factory=list,
        metadata=dict(
            name="elEnumerationC",
            type="Element",
            min_occurs=1,
            max_occurs=3
        )
    )