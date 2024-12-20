from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-enumeration-4-NS"


class NistschemaSvIvListIntEnumeration4Type(Enum):
    VALUE_575112_2278_948_4928225_9740_61188137_852 = (
        -575112,
        2278,
        948,
        -4928225,
        9740,
        -61188137,
        852,
    )
    VALUE_507_982_47962_307_51603_863544_74_97657059_28_2147483648 = (
        507,
        -982,
        47962,
        307,
        -51603,
        863544,
        -74,
        -97657059,
        28,
        -2147483648,
    )
    VALUE_648158327_357_17248_7636424_418707616_59649879_86479_5303 = (
        -648158327,
        -357,
        -17248,
        7636424,
        418707616,
        -59649879,
        -86479,
        -5303,
    )
    VALUE_914500000_67859870_572451_4305728_8426_61838 = (
        -914500000,
        67859870,
        -572451,
        -4305728,
        -8426,
        -61838,
    )
    VALUE_508_68683_530_17746_150_2447 = (
        508,
        68683,
        530,
        17746,
        150,
        -2447,
    )
    VALUE_71303988_2147483648_44263_86309977_4049268_76607623_22829_1270874 = (
        71303988,
        -2147483648,
        44263,
        86309977,
        -4049268,
        -76607623,
        22829,
        1270874,
    )
    VALUE_5_2381666_38132_9178_47_39_12_9688869_59608108 = (
        -5,
        -2381666,
        -38132,
        -9178,
        47,
        -39,
        -12,
        9688869,
        59608108,
    )


@dataclass
class NistschemaSvIvListIntEnumeration4:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-enumeration-4"
        namespace = "NISTSchema-SV-IV-list-int-enumeration-4-NS"

    value: Optional[NistschemaSvIvListIntEnumeration4Type] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
