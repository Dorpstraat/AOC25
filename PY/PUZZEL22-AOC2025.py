import time

# Setup measuring cpu time
start_cpu   = time.process_time()
start_elaps = time.time()

import sys
from functools import lru_cache

def lees_input(bestandsnaam):
    graaf = {}
    with open(bestandsnaam) as f:
        for regel in f:
            regel = regel.strip()
            if not regel:
                continue
            apparaat, rest = regel.split(":")
            apparaat = apparaat.strip().upper()
            doelen = [d.upper() for d in rest.strip().split()]
            graaf[apparaat] = doelen
    return graaf

def tel_paden_memo(graaf):

    @lru_cache(maxsize=None)
    def dfs(knoop, heeft_dac, heeft_fft):
        # update flags
        if knoop == "DAC":
            heeft_dac = True
        if knoop == "FFT":
            heeft_fft = True

        # eindpunt
        if knoop == "OUT":
            return int(heeft_dac and heeft_fft)

        totaal = 0
        for volgende in graaf.get(knoop, []):
            totaal += dfs(volgende, heeft_dac, heeft_fft)

        return totaal

    return dfs("SVR", False, False)

if __name__ == "__main__":
    bestandsnaam = "INPUT11"      # TEST11B of INPUT11

    graaf = lees_input( bestandsnaam )
    resultaat = tel_paden_memo(graaf)
    print("Aantal paden SVR -> OUT met DAC én FFT:", resultaat)

    # Calculate cpu & elapsed time
    print('CPU time: {:.3f} secs'.format(time.process_time()-start_cpu))
    print('Elaped time: {:.3f} secs'.format(time.time()-start_elaps))
    
