# HAT-ReactivityPredictor
### Demo of reactivity prediction of hydrogen atom transfer (HAT) reaction via machine learning

# Requirements
    matplotlib=3.3.1
    numpy=1.19.2=pypi_0
    Orange=3.25.1
    pandas=1.1.1
    scipy=1.5.2=pypi_0
    seaborn=0.9.0
    sklearn=0.22.1
    xgboost=1.3.3=pypi_0

  - It is recommended to execute this project in a linux environment

# How to use the model
## Step 1: Optimization of the structures of reactant and product molecules (substrates and HAT radicals) and calculation of their property features

**1. Get stable structure to do the feature calculation:** use quantum chemical software, such as Gaussian or Orca, to obtain optimized structures at the level of ***B3LYP/6-31+G(d,p)***. The C atoms to be considered for HAT reactivity may be numbered sequentially starting at 1 to facilitate the **3. Feature collection** step.

**2. Feature calculation:** Perform single point energy calculation at the level of ***M06-2X/def2-TZVPP*** with natural bond orbital (NBO) calculations to get FMO energies, atomic charge and bond order. As for BDE, solvation energy correction of MeCN need to be evaluated using SMD model with ***M06-2X/6-31G(d)***. Buried volume features can be calculated using **SpaceDes.ipynb**. The script **getDescriptors.py** and **gen3-sp.py** may be helpful in transforming the output files (.log) of structure optimization into the input files of feature calculation.

**3. Feature collection:** Calculate the BDE from reaction enthalpy(***Thermal Correction to Enthalpy+Electronic Energy (EE)***) and other features. The script **CatchDescriptors.ipynb** can help read the data used to calculate the FMO energy, atomic charge and bond order features. Besides, an integrated script is on progress.

## Step 2: Load the model and predict the reactivity of desired reactions

**1. Model load:** Load the model **HAT-ReactivityPredictor.pkl**. Related codes are shown in **HAT-ReactivityPredictor.ipynb**.

**2. Test set preparation:** Test set should contain 56 features with specific order which is shown in **SampleTest-ExpCH.csv**.

**3. Reactivity prediction:** Load the test set file (.csv) and get ML-predicted HAT barriers. Related codes are shown in **HAT-ReactivityPredictor.ipynb**.


# Contact Us
Email: hxchem@zju.edu.cn; yanglicheng@zju.edu.cn 
