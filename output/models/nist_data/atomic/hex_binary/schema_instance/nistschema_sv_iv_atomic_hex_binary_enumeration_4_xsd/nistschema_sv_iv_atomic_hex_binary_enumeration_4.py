from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-4-NS"


class NistschemaSvIvAtomicHexBinaryEnumeration4Type(Enum):
    VALUE_6A75666C716D666B72696C706E6173787067617568747268616A6166637973716A716E72766A62616864706A73616F6E686873666465716D726F64 = b"juflqmfkrilpnasxpgauhtrhajafcysqjqnrvjbahdpjsaonhhsfdeqmrod"
    VALUE_64756572756677727068687376727365796679757174776B6C67686B656F67657570797976 = b"duerufwrphhsvrseyfyuqtwklghkeogeupyyv"
    VALUE_656B6472646F6A6163776E71 = b"ekdrdojacwnq"
    VALUE_6B64636963626276647477686F706770756A7068776870696C62746A63786F6B6E6A746672626C63637376776C6B73786E6B7372616266616875646175646F6167656F636E63697274 = b"kdcicbbvdtwhopgpujphwhpilbtjcxoknjtfrblccsvwlksxnksrabfahudaudoageocncirt"
    VALUE_64616C6A716D72626B76796479706871726C7461716F67767362667264776F67 = (
        b"daljqmrbkvydyphqrltaqogvsbfrdwog"
    )
    VALUE_6873616774666A696269777162716F78766863727777797765656F74 = (
        b"hsagtfjibiwqbqoxvhcrwwyweeot"
    )
    VALUE_63696877766E6A636270666F696C72686A = b"cihwvnjcbpfoilrhj"
    VALUE_7561656B6979666475666E726D737662746C626D776A77766978676563646C6A6C6B6A7977716B686C7062616A6B716367 = b"uaekiyfdufnrmsvbtlbmwjwvixgecdljlkjywqkhlpbajkqcg"
    VALUE_6B70686A6C6F676E626A61626565697378796D6D70756C7274627270776E6F7272776F646C = b"kphjlognbjabeeisxymmpulrtbrpwnorrwodl"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicHexBinaryEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-4"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-4-NS"

    value: NistschemaSvIvAtomicHexBinaryEnumeration4Type = field(
        metadata={
            "required": True,
            "format": "base16",
        }
    )
