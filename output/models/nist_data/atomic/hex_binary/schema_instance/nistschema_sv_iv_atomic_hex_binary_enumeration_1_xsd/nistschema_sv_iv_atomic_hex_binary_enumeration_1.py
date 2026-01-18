from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-1-NS"


class NistschemaSvIvAtomicHexBinaryEnumeration1Type(Enum):
    VALUE_727172736A736B646368616575787074747667686C72746869626667767662746A76636D64786B62646A646E797068617567697063706A776674796B = b"rqrsjskdchaeuxpttvghlrthibfgvvbtjvcmdxkbdjdnyphaugipcpjwftyk"
    VALUE_696A66756D766E = b"ijfumvn"
    VALUE_786C6C716971787963 = b"xllqiqxyc"
    VALUE_7772796B687870626E75736E68796966656372706B6373657064726E65706170766177716E61746263727777747361706577 = b"wrykhxpbnusnhyifecrpkcsepdrnepapvawqnatbcrwwtsapew"
    VALUE_7871646D6161686F6A747877697365686C67616D616171 = (
        b"xqdmaahojtxwisehlgamaaq"
    )
    VALUE_6762736C6268707277727578686B75736D6B6873656E736970687664776D786576786D62637465716D79 = b"gbslbhprwruxhkusmkhsensiphvdwmxevxmbcteqmy"
    VALUE_747879637369666C796970646E6B6E616C65777064646D687967716D6E726C6E7064676B6E6871686F65616F6C676B7379696C6E7578766B646C7678756E62 = b"txycsiflyipdnknalewpddmhygqmnrlnpdgknhqhoeaolgksyilnuxvkdlvxunb"
    VALUE_636B6B686471656B6D656166616975717369656464636571786969636F6A747765617364706F7667666164727071766E67717771796B647274796F7771716F7373666E = b"ckkhdqekmeafaiuqsieddceqxiicojtweasdpovgfadrpqvngqwqykdrtyowqqossfn"
    VALUE_6E74696B776161 = b"ntikwaa"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryEnumeration1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-1-NS"

    value: NistschemaSvIvAtomicHexBinaryEnumeration1Type = field(
        metadata={
            "required": True,
            "format": "base16",
        }
    )
