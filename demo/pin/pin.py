import os
import numpy as np
import matplotlib.pyplot as plt

tmpl = """TTL *Pin cell example
TFU={} TMO={} BOR={}   *Statepoint parameters
FUE 1 10.1/3.2            *Fuel density/enrichment
PIC .49 .55 .81           *Pin cell radii
PDE 30
STA                       *Start execution
END                       *End of input
"""

TFU=293.0
TMO=293.0
BOR=0.0

TFUs = np.arange(300., 1201., 50)
KINFs = np.zeros_like(TFUs)
for i in range(len(TFUs)):
    TFU = TFUs[i]

    ifname = 'pin_TFU_{}_TMO_{}_BOR_{}.inp'.format(TFU, TMO, BOR)
    f = open(ifname, 'w')
    f.write(tmpl.format(TFU, TMO, BOR))
    f.close()

    os.system('casmo4 -k ' + ifname)

    ofname = ifname.replace('inp', 'log')
    KINFs[i] = float(open(ofname, 'r').readlines()[38].split()[7])
    print(KINFs[i])
plt.plot(TFUs, KINFs)
plt.show()



