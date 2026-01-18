from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vehicle.org"


@dataclass(kw_only=True)
class Person:
    class Meta:
        name = "person"
        namespace = "http://www.vehicle.org"

    car: list[Person.Car] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Car:
        reg_state: None | str = field(
            default=None,
            metadata={
                "name": "regState",
                "type": "Attribute",
            },
        )
        reg_plate: None | int = field(
            default=None,
            metadata={
                "name": "regPlate",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Vehicle:
    class Meta:
        name = "vehicle"
        namespace = "http://www.vehicle.org"

    plate_number: None | int = field(
        default=None,
        metadata={
            "name": "plateNumber",
            "type": "Attribute",
        },
    )
    state: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
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
