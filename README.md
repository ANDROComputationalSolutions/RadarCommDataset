# RadarCommDataset: Radar & Communication Signal and Modulation Classification Dataset
> **RadarCommDataset is a wireless signal dataset released for public use under the [Creative Commons Attribution - NonCommercial - ShareAlike 4.0 (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/)[Additional info can be found at the end] by MR Lab at ANDRO. The lack of existing multitask labelled datasets for machine learning for wireless communication is the prime motivation urging this release. RadarCommDataset is first of its kind multitask labelled dataset released to help research community to advance machine learning for wireless communication. The dataset contains radar and communication waveforms. This repository supplements helper scripts to visualize as well as extract the dataset. Please contact for any other license.**
## Download link
### Synthetic version
https://www.androcs.com/uploads/RadComDynamic.zip
### Over the air version
https://www.androcs.com/uploads/RadComOta2.45GHz.zip
## Contributors
* Anu Jagannath    - ajagannath@androcs.com - Marconi Rosenblatt AI/ML Innovation Lab
* Jithin Jagannath - jjagannath@androcs.com - Marconi Rosenblatt AI/ML Innovation Lab

## Format description
* Type - HDF5
* Key  - {modulation,signal,snr,sample}
* Tensor - 256 x 1 - {inphase of length 128, quadrature of length 128}
* Sampling rate - 10 MS/s
* Total snapshots per waveform - 700
* SNR range - -20 dB to 18 dB in steps of 2 dB
* Modulation Classes - Pulsed Continuous wave, Frequency modulated Continuous wave, BPSK, AM-DSB, AM-SSB, ASK
* Signal Classes -  Airborne detection radar, Airborne range radar, Air-Ground MTI radar, Ground mapping radar, Radar Altimeter, SATCOM, AM Radio, Short-range wireless

## Waveform Generation
* Platform - GNURadio Companion
* Dynamic effects - Dynamic channel model GRC block (gnuradio.channels.dynamic_channel_model) over range of SNRs. The parameters are shown below:
--------------------------------------------------------------------------------------
| Dynamic Parameters                                            |         Value        |
|---------------------------------------------------------------|:--------------------:|
| Carrier frequency offset standard deviation per sample        |       0.05 Hz      |
| Maximum carrier frequency offset                              |       250 Hz       |
| Sample rate offset standard deviation per sample              |       0.05 Hz      |
| Maximum sample rate offset                                    |        60 Hz       |
| Number of sinusoids used in frequency selective fading        |           5          |
| Maximum doppler frequency                                     |         2 Hz         |
| Rician K-factor                                               |           3          |
| Fractional sample delays comprising power delay profile (PDP) | [ 0.2, 0.3, 0.1] |
| Number of multipath taps                                      |           5          |
| List of magnitudes corresponding to each delay in PDP         |  [1, 0.5, 0.5 ]  |
## Helper Scripts Usage
* load_dataset.py - script to load the dataset
* visualize.py    - script to visualize specified waveform

## How to cite this dataset ? Please cite the original paper.
* **BibTeX** 
> >  @article{AjagannathCOMNET21,
title = {Dataset for modulation classification and signal type classification for multi-task and single task learning},
journal = {Computer Networks},
volume = {199},
pages = {108441},
year = {2021},
issn = {1389-1286},
doi = {https://doi.org/10.1016/j.comnet.2021.108441},
url = {https://www.sciencedirect.com/science/article/pii/S138912862100400X},
author = {Anu Jagannath and Jithin Jagannath},
keywords = {Multi-task learning, Machine learning, Deep learning, Modulation classification, signal classification, software defined radio, Radio frequency dataset}} </br >
> > @inproceedings{JagannathMTL, title={{Multi-task Learning Approach for Automatic Modulation and Wireless Signal Classification}}, author={Jagannath, Anu and Jagannath, Jithin}, booktitle = {Proc. of IEEE International Conference on Communications (ICC)}, address = {Montreal, Canada}, month = {June}, year = {2021} } </br >
* **Plain Text** 
> > A. Jagannath, J.Jagannath, "Dataset for Modulation Classification and Signal Type Classification for Multi-task and Single Task Learning", Computer Networks (Elsevier), vol. 199,108441, ISSN 1389-1286, 2021. </br >
> > A. Jagannath, J. Jagannath. "Multi-task Learning Approach for Automatic Modulation and Wireless Signal Classification", in Proc. of IEEE International Conference on Communications (ICC), Montreal, Canada, June 2021.</br >


## Additional License Info:
**You must include the following in (a) any copy or distribution of this dataset or portion of this dataset, (b) any Derivation (defined below) of this dataset or portion of this dataset, or (c) any new data set or work that extracts from or modifies this dataset or portion of this dataset in any way:**

**Ownership and License.** This dataset is owned by ANDRO Computational Solutions, LLC (https://www.androcs.com/) and is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) located at https://creativecommons.org/licenses/by-nc-sa/4.0/  (the “Creative Commons License”)

**Attribution.** You must prominently display ANDRO Computational Solutions, LLC and the ANDRO logo: ![ANDRO](https://github.com/ANDROComputationalSolutions/RadarCommDataset/blob/main/andro.png)
 
**Derivations.** “Derivations” means that you create a new work or new dataset that aggregates this data set or any portion of this dataset, uses this dataset or any portion of this for any calculations, and/or is derived from or is based on this dataset or any portion of this dataset.  


