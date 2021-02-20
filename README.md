# HAT-ReactivityPredictor
### Demo of reactivity prediction of hydrogen atom transfer (HAT) reaction via machine learning

# Requirements
ase=3.18.0=pypi_0
bidict=0.18.3=pypi_0
dscribe=0.2.9=pypi_0
joblib=0.13.2=py36_0
matplotlib=3.1.2=pypi_0
molml=0.9.0=pypi_0
networkx=2.3=py_0
numpy=1.19.2=pypi_0
openbabel=3.0.0=py36h1360c68_0
pandas=0.25.0=py36hb3f55d8_0
pathlib=1.0.1=pypi_0
pickleshare=0.7.5=py36_0
pytorch=1.1.0=py3.6_cuda10.0.130_cudnn7.5.1_0
rdkit=2019.03.2=py36hb31dc5d_1
scikit-learn=0.22=pypi_0
scipy=1.2.1=pypi_0
seaborn=0.9.0=pypi_0
torch-cluster=1.4.2=pypi_0
torch-geometric=1.3.0=pypi_0
torch-scatter=1.3.1=pypi_0
torch-sparse=0.4.0=pypi_0
xgboost=0.90=pypi_0

# How to use the model
## Step 1: Optimization of the structures of reactant and product molecules (substrates and HAT catalysts) and calculation of their property features

**1. Get stable structure to do the feature calculation:** use quantum chemical software, such as Gaussian or Orca, to obtain optimized structures at the level of ***B3LYP/6-31+G(d,p)***. The C atoms to be considered for HAT reactivity can be numbered sequentially starting at 1 to facilitate the **3. Feature collection** step.

**2. Feature calculation:** Perform single point energy calculation at the level of ***M06-2X/def2-TZVPP*** with natural bond orbital (NBO) calculations to get FMO energies, atomic charge and bond order. As for BDE, solvation energy correction of MeCN need to be evaluated using SMD model with ***M06-2X/6-31G(d)***. Buried volume features can be calculated using **SpaceDes.ipynb**. The script **getDescriptors.py** and **gen3-sp.py** may be helpful in transforming the output files (.log) of structure optimization into the input files of feature calculation.

**3. Feature collection:** Calculate the BDE from reaction enthalpy(***Thermal Correction to Enthalpy+Electronic Energy (EE)***) and other features. The script **CatchDescriptors.ipynb** can help read the data used to calculate the FMO energy, atomic charge and bond order features. Besides, an integrated script is on progress.

## Step 2: Load the model and predict the reactivity of desired reactions

**1. Model load:** Load the model **HAT-ReactivityPredictor.pkl**. Related codes are shown in **HAT-ReactivityPredictor.ipynb**.

**2. Test set preparation:** Test set should contain 56 features with specific order which is shown in **SampleTest-ExpCH.csv**.

**3. Reactivity prediction:** Load the test set file (.csv) and get ML-predicted HAT barriers. Related codes are shown in **HAT-ReactivityPredictor.ipynb**.

writing...


# Contact Us
Email: hxchem@zju.edu.cn; yanglicheng@zju.edu.cn 
