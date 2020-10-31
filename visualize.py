import h5py
import sys
import argparse
import matplotlib.pyplot as plt

def parse_args():
    "Parse the command line arguments"
    parser = argparse.ArgumentParser()
    parser.add_argument("-num", type=int,default="0",
                        help="Which sample to pick. 0 to 699")
    parser.add_argument("-snr", type=int,default="10",
                        help="SNR: -20 to 18 in 2 step increments")
    parser.add_argument("-mod",default="pulsed",
                        help="Modulation options: pulsed,fmcw,bpsk,amdsb,amssb,ask")
    parser.add_argument("-sig",default="Airborne-detection",
                        help="Signal type options: Airborne-detection,Airborne-range,Air-Ground-MTI,Ground mapping,Radar-Altimeter,Satcom,AM radio,short-range")
    return parser.parse_args()


def main():
    args = parse_args()
    with h5py.File('RadComDynamic.hdf5', 'r') as f:
        key = args.mod,args.sig,args.snr,args.num 
        waveform = f[str(key)][:]
        real = waveform[0:128]
        imag = waveform[128:]
    f.close()
    
    # Plot and visualize the selected sample
    plt.figure(figsize=[8, 6])
    plt.plot(real,'-go')
    plt.plot(imag,'-bo')
    plt.title(str(key), fontsize=16)
    plt.show()

if __name__ == "__main__":
    sys.exit(not main())
