from output.models.wg_data.sg.negsn_xsd.negsn import N
from output.models.wg_data.sg.negsn_xsd.negsn import N1
from output.models.wg_data.sg.negsn_xsd.negsn import S
from output.models.wg_data.sg.negsn_xsd.negsn import Test


obj = Test(
    any_element=N1(
        value='Test case for interaction of substitution groups and \n   #definedSibling.'
    ),
    s1_or_s=S(

    ),
    n=N(

    )
)
