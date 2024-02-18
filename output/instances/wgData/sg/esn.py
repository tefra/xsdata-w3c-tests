from output.models.wg_data.sg.negsn_xsd.negsn import E
from output.models.wg_data.sg.negsn_xsd.negsn import N
from output.models.wg_data.sg.negsn_xsd.negsn import S
from output.models.wg_data.sg.negsn_xsd.negsn import Test


obj = Test(
    any_element=E(
        value='Test case for interaction of substitution groups and \n   #definedSibling.'
    ),
    s1_or_s=S(

    ),
    n=N(

    )
)
