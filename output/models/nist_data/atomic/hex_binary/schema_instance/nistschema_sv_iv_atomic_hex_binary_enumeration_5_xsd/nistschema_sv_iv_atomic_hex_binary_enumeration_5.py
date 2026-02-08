from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-5-NS"


class NistschemaSvIvAtomicHexBinaryEnumeration5Type(Enum):
    VALUE_6D6F63686E7463706A67747172716B75656966746273697579687666706C6C72726E69706F6B67716D766F626B6C757171777363796B646E666468736F6F6B696464 = b"mochntcpjgtqrqkueiftbsiuyhvfpllrrnipokgqmvobkluqqwscykdnfdhsookidd"
    VALUE_666A6272766176786B6C69636D76686E6D68697968746A6264796C74656C6F78796C616973 = b"fjbrvavxklicmvhnmhiyhtjbdylteloxylais"
    VALUE_6761737571766C716873746D72 = b"gasuqvlqhstmr"
    VALUE_657575657662737270776A626A70716D6878796E77627878647167786C6862657867796576686D6C63696567787261666D = b"euuevbsrpwjbjpqmhxynwbxxdqgxlhbexgyevhmlciegxrafm"
    VALUE_6F6B66687469687477677775706A61 = b"okfhtihtwgwupja"
    VALUE_646F76676367746C6E6D636663696670796A6F616E6862676B656C786275666975616472687463706D77 = b"dovgcgtlnmcfcifpyjoanhbgkelxbufiuadrhtcpmw"
    VALUE_6B696767676C64707177726B77777865796D63656B6B6369626A66646D6D72676877707162786765757471706C75796C6B75676B6561756B6579706C647269696C766E = b"kigggldpqwrkwwxeymcekkcibjfdmmrghwpqbxgeutqpluylkugkeaukeypldriilvn"
    VALUE_776F64796E716C686D78776666626C6F = b"wodynqlhmxwffblo"
    VALUE_726565637367796B6D77696D66716C6E6A63757375716D6568676179667674757561766A686E6C7161756664676271676C626F63656C626C7261767168796C747265786B = b"reecsgykmwimfqlnjcusuqmehgayfvtuuavjhnlqaufdgbqglbocelblravqhyltrexk"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryEnumeration5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-5-NS"

    value: NistschemaSvIvAtomicHexBinaryEnumeration5Type = field(
        metadata={
            "format": "base16",
        }
    )
