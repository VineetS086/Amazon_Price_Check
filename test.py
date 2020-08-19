from call_product import *
from call_product import run


def test_0():
    url = 'https://www.amazon.in/Apple-MWP22HN-A-AirPods-Pro/dp/B07ZRXF7M8/ref=pd_rhf_gw_s_pd_crcd_0_1/259-0790228-7263300?_encoding=UTF8&pd_rd_i=B07ZRXF7M8&pd_rd_r=2253b510-408e-4e15-ad59-a70669424dba&pd_rd_w=yQOPu&pd_rd_wg=Ds4OO&pf_rd_p=decc33e5-9bac-4f5a-9e32-c8b613fff04e&pf_rd_r=QPNYPXBW0HYVPSSZTHGF&psc=1&refRID=QPNYPXBW0HYVPSSZTHGF'
    run(url)
    print(1)
    
def test_1():
    url = 'https://www.amazon.in/Apple-MWP22HN-A-AirPods-Pro/dp/B07ZRXF7M8/ref=pd_rhf_gw_s_pd_crcd_0_1/259-0790228-7263300?_encoding=UTF8&pd_rd_i=B07ZRXF7M8&pd_rd_r=2253b510-408e-4e15-ad59-a70669424dba&pd_rd_w=yQOPu&pd_rd_wg=Ds4OO&pf_rd_p=decc33e5-9bac-4f5a-9e32-c8b613fff04e&pf_rd_r=QPNYPXBW0HYVPSSZTHGF&psc=1&refRID=QPNYPXBW0HYVPSSZTHGF'
    run(url)
    print(1)
    url = 'https://www.amazon.in/gp/product/B07T81554H/ref=s9_acss_bw_cg_INele1_1b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=ASMGBFY88GZPH299JVFX&pf_rd_t=101&pf_rd_p=61344d7d-e9e2-4f34-993e-b8308f5b009c&pf_rd_i=976419031'
    run(url)
    print(2)
    url = 'https://www.amazon.in/All-new-Echo-Dot-3rd-Gen/dp/B07PFFMP9P/ref=sr_1_1?dchild=1&keywords=alexa&qid=1597472639&sr=8-1'
    run(url)
    print(3)
    url = 'https://www.amazon.in/dp/B07HGJJ58K/ref=pc_mcnc_merchandised-search-12_?pf_rd_s=merchandised-search-12&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=6G8RS9HMBFKDS3G8XDY7&pf_rd_p=ba08629f-24c9-4adb-9f6b-0e543e0ca95a'
    run(url)
    print(4)
    url = 'https://www.amazon.in/Fitbit-FB507BKBK-Smartwatch-Tracking-Included/dp/B07TWFVDWT/ref=pd_di_sccai_4/259-0790228-7263300?_encoding=UTF8&pd_rd_i=B07TWFVDWT&pd_rd_r=82f30d62-edde-4d39-9a71-bd1b903df77f&pd_rd_w=jYo0u&pd_rd_wg=vm98V&pf_rd_p=a1f3aa5a-f05d-4e2d-b84b-6ef88e21fb7e&pf_rd_r=VP8KJ2HHP57CBXK3N53J&psc=1&refRID=VP8KJ2HHP57CBXK3N53J'
    run(url)
    print(5)
    url = 'https://www.amazon.in/Fitbit-FB503CPBU-Ionic-Smartwatch-Orange/dp/B074VNDGND/ref=psdc_5605728031_t2_B07TWFVDWT'
    run(url)
    print(6)

def test_2():
    del_all_product()

#test_0()
test_1()
#del_history()
#test_1()
#del_all_product()
#update_all_product()
