import pprint
from scapy.all import *

pkt = (
        Ether(src="0:1:2:3:4:5", dst="5:4:3:2:1:0") /
        IP(src="1.2.3.4", dst="4.3.2.1", flags=["DF", "MF"]) /
        UDP(sport=1234, dport=4321, chksum=True)
)
pkt.show()
pkt.show2()

result = pkt.__class__(raw(pkt)).to_list()
# result = pkt.to_list()

pprint.pprint(result)

print("Iterator")
pkt.explicit = True
for v in pkt:
    print(f"{v}\n")
# for p in pkt.layers():
#     assert isinstance(p, Packet)
#     print(str(p))
#     for f in p.fields_desc:
#         print(str(f))
#         print(f.)
