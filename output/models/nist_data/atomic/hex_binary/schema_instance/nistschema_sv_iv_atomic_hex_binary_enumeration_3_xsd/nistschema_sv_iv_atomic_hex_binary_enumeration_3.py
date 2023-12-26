from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-3-NS"


class NistschemaSvIvAtomicHexBinaryEnumeration3Type(Enum):
    VALUE_66656A78736C737670696577636F6F7374736E666F716B6B6D70706372636670756376717174637271636F766174716877676C7677616B6B616B66686B796E6E = b"fejxslsvpiewcoostsnfoqkkmppcrcfpucvqqtcrqcovatqhwglvwakkakfhkynn"
    VALUE_716F6A676D716C6A7962627064746C6D6F6B = b"qojgmqljybbpdtlmok"
    VALUE_7869716779776174636276726362707274646F6672636874796C77716F796D67776463706664686D79727972696A6768686C746A706D776D67757266756373777278616D616D6A74 = b"xiqgywatcbvrcbprtdofrchtylwqoymgwdcpfdhmyryrijghhltjpmwmgurfucswrxamamjt"
    VALUE_687976636D666667656C66736A716C766D736A65786174746472716A6C6D6F6D7062746E756C6F70676F72696475716F716E676C6F6B6E646A72756E677662636A6C616A6E756C76 = b"hyvcmffgelfsjqlvmsjexattdrqjlmompbtnulopgoriduqoqnglokndjrungvbcjlajnulv"
    VALUE_6F6D6861766564716D69696172637775646C7068616C767770636963697972766D696E746C69796A70796E6479706E786D71736569616F65727377776E736C65676E6F70727567 = b"omhavedqmiiarcwudlphalvwpciciyrvmintliyjpyndypnxmqseiaoerswwnslegnoprug"
    VALUE_6B6A64797669616F6E68637177706F666A696A6464696C6864716D726B646461706D686B70747279666F70676D796D70736F6B62746D72746F75 = b"kjdyviaonhcqwpofjijddilhdqmrkddapmhkptryfopgmympsokbtmrtou"
    VALUE_697869686D6D726979716E736D6D6C716E61756F626C72656A6A6176696772737564787364757971736A7470617074766B797074736B6B6C7869656E656968616F6B63736778656975 = b"ixihmmriyqnsmmlqnauoblrejjavigrsudxsduyqsjtpaptvkyptskklxieneihaokcsgxeiu"
    VALUE_676365686B6F746A = b"gcehkotj"
    VALUE_736967716F73666C706F79716E68676764696378 = b"sigqosflpoyqnhggdicx"


@dataclass
class NistschemaSvIvAtomicHexBinaryEnumeration3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-enumeration-3-NS"

    value: Optional[NistschemaSvIvAtomicHexBinaryEnumeration3Type] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base16",
        },
    )
