[![DOI](https://zenodo.org/badge/878193479.svg)](https://doi.org/10.5281/zenodo.14803005)


> [!WARNING]
> This is still in progress and subject to change, as additional requirements may arise.
# Metadata-Adoption-Quantify

This software extracts relevant data from SOMEF (Software Metadata Extraction Framework) results to answer specific research questions. The extracted insights are returned as structured JSON files, allowing easy integration and analysis.

## Table of Contents

- [Metadata-Adoption-Quantify](#metadata-adoption-quantify)
  - [Table of Contents](#table-of-contents)
  - [About the Software](#about-the-software)
  - [Research Questions](#research-questions)
  - [Features](#features)
  - [Installation](#installation)
  - [Output](#output)

## About the Software

This tool is designed to process metadata extracted using SOMEF, focusing on answering predefined research questions. It parses the data from SOMEF's output and generates JSON files with the information relevant to each research question (RQ) and generating calculations for each data requested.

## Research Questions

This software is tailored to answer the following research questions:

1. RQ1: How do communities describe Research Software metadata in their code repositories?
2. RQ2: What is the adoption of archival infrastructures across the disciplines?
3. RQ3: How do software projects adopt versioning?
4. RQ4: How comprehensive is the metadata provided in code repositories?
5. RQ5: What are the most common citation practices among the communities?

## Features
- Extract metadata from repositories using SOMEF.
- Extracts and processes metadata from SOMEF results.
- Filters information relevant to specific research questions.
- Outputs the results as structured JSON files for easy review and further analysis.

## Installation

1. Clone this repository:

   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/Anas-Elhounsri/Metadata-Adoption-Quantify.git
   cd Metadata-Adoption-Quantify
  
2. Install requirements
   ```bash
   pip install -r requirements.txt
   
## Usage

You can extract SOMEF output (Already extracted) with:

  ```bash
  python run_somef.py
  ```
In order to use, you can run every RQ individually using the `main.py`:

   ```bash
   python main.py
   ```
And it will prompt you the following:

  ```bash
=== Main Menu ===
1. Run RQ scripts
2. Calculate results
exit. Quit
Choose an option (1/2/exit): 
  ```
If you choose 1. you will be able to choose which research question you wish to answer:

  ```bash
Available RQ scripts:
1. rq1.py
2. rq2.py
3. rq3.py
4. rq4.py
5. rq5.py
Enter RQ number (1-5) or 'back': 
 ```
Once you choose an RQ, you will be prompted to put some input regarding the naming of the files, the directories etc... (You need to follow the same naming of the already existing files if you wish to use `count_results.py` to iterate through the results of analysis and calculate the final results, for example for rq1, you should name the output for envri `analysis_envri_rq1.json`, check the rest of the files to follow the naming convention)

If in the main menu you choose 2. you will be prompted to fill in the directory of the results, and the cluster you wish to calculate for:
  ```bash
Running results calculation...
Input the research question (rq1, rq2, rq3, rq4, rq5) or type 'exit' to quit: 
```
## Output
If you choose to get the somef results of RQ1 and input the prompts accordingly, you get this result for RQ1 from one cluster (This is ESCAPE)
```bash
{
    "citation.cff": {
        "count": 1
    },
    "readme_url": {
        "count": 17
    },
    "package": {
        "count": 7,
        "files": [
            "temp_analysis/escape2020/gammapy_gammapy/gammapy-1.2/setup.cfg",
            "temp_analysis/escape2020/cosimoNigro_agnpy/agnpy-master/setup.py",
            "temp_analysis/escape2020/IndexedConv_IndexedConv/IndexedConv-1.3.2/setup.py",
            "temp_analysis/escape2020/cds-astro_cds-moc-rust/cds-moc-rust-main/Cargo.toml",
            "temp_analysis/escape2020/cds-astro_mocpy/mocpy-0.15.0/Cargo.toml",
            "temp_analysis/escape2020/cds-astro_aladin-lite/aladin-lite-3.3.2/package.json",
            "temp_analysis/escape2020/escape2020_school2022/school2022-1.0/docs/themes/dream/package.json"
        ]
    },
    "authors": {
        "count": 2,
        "files": [
            "temp_analysis/escape2020/R3BRootGroup_R3BRoot/R3BRoot-jun24/AUTHORS",
            "temp_analysis/escape2020/FairRootGroup_FairMQ/FairMQ-master/AUTHORS"
        ]
    },
    "contributors": {
        "count": 3,
        "files": [
            "output_4.json",
            "output_11.json",
            "output_5.json"
        ]
    },
    "license": {
        "count": 17
    },
    "codemeta.json": {
        "count": 15,
        "files": [
            "temp_analysis/escape2020/gammapy_gammapy/gammapy-1.2/codemeta.json",
            "temp_analysis/escape2020/cosimoNigro_agnpy/agnpy-master/codemeta.json",
            "temp_analysis/escape2020/IndexedConv_IndexedConv/IndexedConv-1.3.2/codemeta.json",
            "temp_analysis/escape2020/cds-astro_cds-moc-rust/cds-moc-rust-main/codemeta.json",
            "temp_analysis/escape2020/aardk_jupyter-casa/jupyter-casa-master/codemeta.json",
            "temp_analysis/escape2020/cds-astro_tutorials/tutorials-1.0.3/codemeta.json",
            "temp_analysis/escape2020/R3BRootGroup_R3BRoot/R3BRoot-jun24/codemeta.json",
            "temp_analysis/escape2020/AMIGA-IAA_hcg-16/hcg-16-1.2.3/codemeta.json",
            "temp_analysis/escape2020/repo/eossr-master/codemeta.json",
            "temp_analysis/escape2020/JColl88_sdc1-solution-binder/sdc1-solution-binder-1.0.0/codemeta.json",
            "temp_analysis/escape2020/explore-platform_g-tomo/g-tomo-2/codemeta.json",
            "temp_analysis/escape2020/cds-astro_mocpy/mocpy-0.15.0/codemeta.json",
            "temp_analysis/escape2020/javierrico_gLike/gLike-master/codemeta.json",
            "temp_analysis/escape2020/cds-astro_aladin-lite/aladin-lite-3.3.2/codemeta.json",
            "temp_analysis/escape2020/FairRootGroup_FairMQ/FairMQ-master/codemeta.json"
        ]
    },
    "zenodo.json": {
        "count": 5,
        "files": [
            "temp_analysis/escape2020/cosimoNigro_agnpy/agnpy-master/.zenodo.json",
            "temp_analysis/escape2020/cds-astro_cds-moc-rust/cds-moc-rust-main/.zenodo.json",
            "temp_analysis/escape2020/aardk_jupyter-casa/jupyter-casa-master/.zenodo.json",
            "temp_analysis/escape2020/javierrico_gLike/gLike-master/.zenodo.json",
            "temp_analysis/escape2020/FairRootGroup_FairMQ/FairMQ-master/.zenodo.json"
        ]
    },
    "identifier_extract": {
        "count": 7,
        "extracted_values": [
            "10.5281/zenodo.3967385",
            "10.5281/zenodo.7544514",
            "https://zenodo.org/badge/latestdoi/224865065",
            "10.5281/zenodo.1689985",
            "10.5281/zenodo.3967385",
            "10.5281/zenodo.10405177",
            "10.5281/zenodo.4055175"
        ]
    },
    "None": {
        "count": 0
    }
}
```
> [!WARNING]
> Should be noted, that due to the large size of the files for `temp_analysis`, this directory is not be available on this repository, it is impossible to upload it on GitHub, you can extract using `SoMEF` (it automatically keeps the `temp_files`). From these results, we can answer all RQs.

If you choose to calculate the results of the cluster you will get the following output:

```bash
{
    "escape": {
        "cff": 5.88235294117647,
        "readme": 100.0,
        "package": 41.17647058823529,
        "authors": 11.76470588235294,
        "contributors": 17.647058823529413,
        "license": 100.0,
        "codemeta": 88.23529411764706,
        "zenodo": 29.411764705882355,
        "zenodo_doi": 41.17647058823529,
        "none": 0.0
    }
}
```

## Ackowlegement:
The authors acknowledge the OSCARS project, which has received funding from the European Commission's Horizon Europe Research and Innovation programme under grant agreement No. 101129751
<img src="logo.png" alt="logo"/>
