from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-2-NS"


class NistschemaSvIvAtomicDoubleEnumeration2Type(Enum):
    VALUE_4_9_E_324 = Decimal('4.9E-324')
    VALUE_4_8523411539849754_E_234 = Decimal('4.8523411539849754E-234')
    VALUE_2_8869019830516350_E_144 = Decimal('2.8869019830516350E-144')
    VALUE_3_3925700348046903_E_54 = Decimal('3.3925700348046903E-54')
    VALUE_2_7311892445441031_E36 = Decimal('2.7311892445441031E+36')
    VALUE_2_9181385291440688_E126 = Decimal('2.9181385291440688E+126')
    VALUE_2_4983147023924484_E216 = Decimal('2.4983147023924484E+216')
    VALUE_1_7976931348623157_E308 = Decimal('1.7976931348623157E+308')


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration2Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
