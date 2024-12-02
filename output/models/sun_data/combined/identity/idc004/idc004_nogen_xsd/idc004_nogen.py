from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vehicle.org"


@dataclass
class Person:
    class Meta:
        name = "person"
        namespace = "http://www.vehicle.org"

    car: list["Person.Car"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Car:
        reg_state: Optional[str] = field(
            default=None,
            metadata={
                "name": "regState",
                "type": "Attribute",
            },
        )
        reg_plate: Optional[int] = field(
            default=None,
            metadata={
                "name": "regPlate",
                "type": "Attribute",
            },
        )


@dataclass
class Vehicle:
    class Meta:
        name = "vehicle"
        namespace = "http://www.vehicle.org"

    plate_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "plateNumber",
            "type": "Attribute",
        },
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class State:
    class Meta:
        name = "state"
        namespace = "http://www.vehicle.org"

    code: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    vehicle: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    person: list[Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.vehicle.org"

    state: list[State] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
