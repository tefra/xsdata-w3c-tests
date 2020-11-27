from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-enumeration-4-NS"


class NistschemaSvIvAtomicDoubleEnumeration4Type(Enum):
    VALUE_4_9_E_324 = Decimal('4.9E-324')
    VALUE_1_9543492578327128_E_234 = Decimal('1.9543492578327128E-234')
    VALUE_4_6337466732941437_E_144 = Decimal('4.6337466732941437E-144')
    VALUE_4_2180257301126178_E_54 = Decimal('4.2180257301126178E-54')
    VALUE_2_0744434746534796_E36 = Decimal('2.0744434746534796E+36')
    VALUE_4_3411284761058989_E126 = Decimal('4.3411284761058989E+126')
    VALUE_3_4043189586904751_E216 = Decimal('3.4043189586904751E+216')
    VALUE_1_7976931348623157_E308 = Decimal('1.7976931348623157E+308')


@dataclass
class NistschemaSvIvAtomicDoubleEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-double-enumeration-4-NS"

    value: Optional[NistschemaSvIvAtomicDoubleEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
