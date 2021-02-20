# HAT-ReactivityPredictor
### Demo of reactivity prediction of hydrogen atom transfer (HAT) reaction via machine learning

# Requirements

# How to use the model
## Step 1: Optimization of the structures of reactant and product molecules (substrates and HAT catalysts) and calculation of their property features

**1. Get stable structure to do the feature calculation:** use quantum chemical software, such as Gaussian or Orca, to obtain optimized structures at the level of ***B3LYP/6-31+G(d,p)***. The C atoms to be considered for HAT reactivity can be numbered sequentially starting at 1 to facilitate the **3. Feature collection** step.

**2. Feature calculation:** Perform single point energy calculation at the level of ***M06-2X/def2-TZVPP*** with natural bond orbital (NBO) calculations to get FMO energies, atomic charge and bond order. As for BDE, solvation energy correction of MeCN need to be evaluated using SMD model with ***M06-2X/6-31G(d)***. Buried volume features can be calculated using **SpaceDes.ipynb**. The script **getDescriptors.py** and **gen3-sp.py** may be helpful in transforming the output files (.log) of structure optimization into the input files of feature calculation.

**3. Feature collection:** 

writing...


# Contact Us
Email: hxchem@zju.edu.cn; yanglicheng@zju.edu.cn 
