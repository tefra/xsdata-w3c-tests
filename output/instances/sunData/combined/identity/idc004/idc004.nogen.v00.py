from output.models.sun_data.combined.identity.idc004.idc004_nogen_xsd.idc004_nogen import Person
from output.models.sun_data.combined.identity.idc004.idc004_nogen_xsd.idc004_nogen import Root
from output.models.sun_data.combined.identity.idc004.idc004_nogen_xsd.idc004_nogen import State
from output.models.sun_data.combined.identity.idc004.idc004_nogen_xsd.idc004_nogen import Vehicle


obj = Root(
    state=[
        State(
            code=[
                "CA",
            ],
            vehicle=[
                Vehicle(
                    plate_number=123,
                    state="CA"
                ),
                Vehicle(
                    plate_number=456,
                    state="CA"
                ),
            ],
            person=[
                Person(
                    car=[
                        Person.Car(
                            reg_state="CA",
                            reg_plate=123
                        ),
                        Person.Car(
                            reg_state="NY",
                            reg_plate=123
                        ),
                    ]
                ),
            ]
        ),
        State(
            code=[
                "NY",
            ],
            vehicle=[
                Vehicle(
                    plate_number=123,
                    state="NY"
                ),
            ]
        ),
    ]
)
