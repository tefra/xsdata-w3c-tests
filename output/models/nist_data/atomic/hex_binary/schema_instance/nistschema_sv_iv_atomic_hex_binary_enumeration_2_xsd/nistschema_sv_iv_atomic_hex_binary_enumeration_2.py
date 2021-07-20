from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-2-NS"


class NistschemaSvIvAtomicHexBinaryEnumeration2Type(Enum):
    VALUE_696B70746C7777656B6B686B786961737561746A6A666262646161666E617376626B6D70796C6F72786D66786D70657267706971746966636F = b"ikptlwwekkhkxiasuatjjfbbdaafnasvbkmpylorxmfxmpergpiqtifco"
    VALUE_70796171746777756779647270757175746F6177636A77647766786E6E626A6C6474796C656F666874 = b"pyaqtgwugydrpuqutoawcjwdwfxnnbjldtyleofht"
    VALUE_6E = b"n"
    VALUE_687873626A6373726F7171677270677771676C6566746B687268797867736D62716763736D6B746474686B696A7772686167676671766A6A676E6869667670796A667078726368 = b"hxsbjcsroqqgrpgwqgleftkhrhyxgsmbqgcsmktdthkijwrhaggfqvjjgnhifvpyjfpxrch"
    VALUE_71746474 = b"qtdt"
    VALUE_78787167726D70666773646363637167666A76716C746D65746265786F68666E706B6972696F7071776E626975656C767661636E756A6A6962617261 = b"xxqgrmpfgsdcccqgfjvqltmetbexohfnpkiriopqwnbiuelvvacnujjibara"
    VALUE_6B68796C66626A647371616E797170636E636D6973736677706272676A746B = b"khylfbjdsqanyqpcncmissfwpbrgjtk"
    VALUE_776A6B6E6C796261626E627468767771716577787967636C706C6166 = b"wjknlybabnbthvwqqewxygclplaf"


@dataclass
class NistschemaSvIvAtomicHexBinaryEnumeration2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-2-NS"

    value: Optional[NistschemaSvIvAtomicHexBinaryEnumeration2Type] = field(
        default=None,
        metadata={
            "format": "base16",
        }
    )
