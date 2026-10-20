# Typosquatting Detection in Software-Supply-Chains

![GitHub License](https://img.shields.io/github/license/minh-tg/nss2024-typosquatting-mitigation-and-detection)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14907785.svg)](https://doi.org/10.5281/zenodo.14907785)

This repository contains the dataset and supplementary materials used in the paper:

**You Can’t Touch This: Detecting Typosquatting Packages for Enhanced Malware Prevention in Software Supply Chains**  
Minh Tien Truong, Nils Gruschka, Luigi Lo Iacono

Published in *NSS 2024: 18th International Conference on Network and System Security*, 20th November 2024

DOI: [10.1007/978-981-96-3531-3_8](https://doi.org/10.1007/978-981-96-3531-3_8)

## Abstract

In recent years, typosquatting has become a significant threat to software supply chain systems, where malicious packages deceptively mimic legitimate ones. 
Attackers register these fraudulent packages with names strikingly similar to those of legitimate packages. 
As a result, developers can mistakenly download these malicious packages by mistyping
the intended package name or selecting a package based on its convincing yet deceptive name.
In this paper, we assess the effectiveness of string-matching algorithms in identifying potential typosquatting candidates. 
We construct an open dataset comprising 394 typosquatting packages and evaluate the performance of these algorithms based on their ability to detect typosquatting packages. 
In addition, we introduce a novel string-matching algorithm, an extension of the Damerau-Levenshtein distance, demonstrating a notably higher true-positive rate than existing methods. 
Since our dataset contains features not previously considered, we also investigate how these new features affect the assignment accuracy of ML-based classifiers. 
Our results show an overall accuracy rate of 98.4% on our datasets and 96.0% and 93.5% accuracy on evaluating two other open datasets. 
These results provide valuable insights for researchers, package manager vendors, and developers to improve their understanding of malicious typosquatting packages and improve mediation strategies and technologies.

---

## Dataset Overview

`Packages/` contains real malicious npm packages. Do not install or execute them; handle them only in an isolated environment.

This repository includes the following datasets:

- **Own Dataset**: A collection of 406 (397 with source code, 394 after removing 3 obfuscated packages) typosquatting packages we have collected based on Sonatype, Phylum.io and Snyk listings. 
- **Backstabbers Knife Collection**: A snapshot of Backstabbers Knife Collection during our analysis for reproduction purposes
- **MalOSS**: A snapshot of the MalOSS dataset during our analysis for reproduction purposes. 

The programs and our own dataset are licensed under the MIT License. For the Backstabber and MalOSS datasets please look up their corresponding licensing. 
Please make sure to reference us, if you find this dataset helpful:

```
@InProceedings{truong2025typosquatting,
  author    = {Truong, Minh Tien and Gruschka, Nils and Lo Iacono, Luigi},
  editor    = {Song, Houbing Herbert and Di Pietro, Roberto and Alrabaee, Saed and Tubishat, Mohammad and Al-kfairy, Mousa and Alfandi, Omar},
  title     = {You Can't Touch This: Detecting Typosquatting Packages for Enhanced Malware Prevention in Software Supply Chains},
  booktitle = {Network and System Security},
  series    = {Lecture Notes in Computer Science},
  year      = {2025},
  publisher = {Springer Nature Singapore},
  address   = {Singapore},
  pages     = {147--166},
  doi       = {10.1007/978-981-96-3531-3_8}
}
```
To cite the dataset and code, use the Zenodo DOI [10.5281/zenodo.14907785](https://doi.org/10.5281/zenodo.14907785).

If you choose to use the Backstabbers Knife Collection or the MalOSS dataset, please make sure to cite the original authors in your research.
Access to their package collection can be requested by the provided link.

**Backstabber Knife Collection**: [Backstabbers Knife Collection](https://dasfreak.github.io/Backstabbers-Knife-Collection/) <br>
**MalOSS Dataset**: [MalOSS Dataset](https://github.com/osssanitizer/maloss?tab=readme-ov-file)



### Data Format

| Filename                   | Format       | Description                                                                                                                                                                   |
|----------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Packages`                 | Folder       | Contains all malicious and benign samples used during our research                                                                                                            |
| `String Matching`          | Folder       | Contains the metadata of our dataset and the code for the Extended Damerau-Levenshtein Distance. <br>Note: For the other string metrics we used the jellyfish python library. |
| `File Extraction.ipynb`    | Jupyter-File | A small code snippet to help you unzipping all files.                                                                                                                         |
| `Feature Extraction.ipynb` | Jupyter-File | A series of code cells to extract features from packages explained in the paper.                                                                                              |
| `Machine Learning.ipynb`   | Jupyter-File | The model trained on our dataset and tested on various different datasets                                                                                                     |

`String Matching/EDL.py` was replaced in v1.1.0. The version in v1.0.0 did not follow the rules in Sec. 5.2 of the paper (two of its examples gave different values). The updated version implements those rules; call it as `distance(target, candidate)` with the legitimate package name first.

---

## Usage Instructions

1. **Cloning the Repository**

   To clone the repository, use the following command:
   ```bash
   git clone https://github.com/minh-tg/nss2024-typosquatting-mitigation-and-detection.git
   ```
2. Use the `File Extraction.ipynb` Notebook to extract all packages   
3. Get access to MalOSS and Backstabber Knife-Collection datasets
4. Extract their npm packages in the corresponding folder paths.
5. Use the `Feature Extraction.ipynb` Notebook to extract the defined features from all the packages
6. Execute the code cells in the `Machine Learning.ipynb` to execute the model

## How was the dataset gathered?

The dataset consists of two types of information:
1. **Metadata** of the packages.
2. **Source code** of the packages.

We collected data from Sonatype, Phylum, and Snyk listings for typosquatting packages up until early 2023 has been added to the datasets. 
A package was included in the dataset if:
1. It was identified as a **typosquatting package**.
2. A **target package** for the typosquatting attack was provided.

### Preprocessing Steps
1. **Duplicate removal**: We checked for and removed duplicate entries.
2. **Error checking**: We identified and removed legitimate packages that were mistakenly listed (e.g., cases where a typo had been corrected).
3. **Existence check**: We verified whether the package has been or is existing. Even unpublished packages remained listed without metadata.
4. **Obfuscated package removal** We removed packages that deliberately make their code hard to read, beyond simple minification.

In the end 394 typosquatting package source code remained.

### Metadata Collection

The metadata was sourced directly from npm. In cases where npm replaced the package information with placeholders, we still accessed the available metadata. However, for packages that were **unpublished**, no metadata could be retrieved.

### Source Code Collection

The source code was gathered from npm mirrors, archived articles, or repositories.
