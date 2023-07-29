from output.models.ms_data.wildcards.wild_i004_xsd.wild_i004 import Elt1
from output.models.ms_data.wildcards.wild_i004_xsd.wild_i004 import Elt2
from output.models.ms_data.wildcards.wild_i004_xsd.wild_i004 import Root


obj = Root(
    elt1=[
        Elt1(
            any_element=[
                Elt2(
                    value="name"
                ),
            ]
        ),
    ]
)
