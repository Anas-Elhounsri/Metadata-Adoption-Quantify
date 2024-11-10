# FAIR-Quantify

This software extracts relevant data from SOMEF (Software Metadata Extraction Framework) results to answer specific research questions. The extracted insights are returned as structured JSON files, allowing easy integration and analysis.

## Table of Contents

- [About the Software](#about-the-software)
- [Research Questions](#research-questions)
- [Installation](#installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [Contributing](#contributing)
- [License](#license)

## About the Software

This tool is designed to process metadata extracted using SOMEF, focusing on answering predefined research questions. It parses the data from SOMEF's output and generates JSON files with the information relevant to each research question (RQ).

## Research Questions

This software is tailored to answer the following research questions:

1. RQ1: How do communities describe Research Software metadata in their code repositories?
2. RQ2: What is the adoption of archival infrastructures across the disciplines?
3. RQ3: How do software projects adopt versioning?
4. RQ4: How comprehensive is the metadata provided in code repositories?
5. RQ5: What are the most common citation practices among the communities?

## Features

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
In order to use, you can run every RQ individually with an example:

   ```bash
   python rq1.py
   ```

## Output

This is an output example of RQ1 from one cluster:
```bash
{
    "citation.cff": {
        "count": 1
    },
    "readme_url": {
        "count": 17
    },
    "package": {
        "count": 13,
        "files": [
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\package.json",
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\src\\core\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\src\\core\\al-api\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\src\\core\\al-core\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\src\\core\\al-task-exec\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_cds-moc-rust\\cds-moc-rust-main\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_cds-moc-rust\\cds-moc-rust-main\\crates\\cli\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_cds-moc-rust\\cds-moc-rust-main\\crates\\set\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_cds-moc-rust\\cds-moc-rust-main\\crates\\wasm\\Cargo.toml",
            "temp_analysis/escape2020\\cds-astro_mocpy\\mocpy-0.15.0\\Cargo.toml",
            "temp_analysis/escape2020\\escape2020_school2022\\school2022-1.0\\docs\\themes\\dream\\package.json",
            "temp_analysis/escape2020\\escape2020_school2022\\school2022-1.0\\testing\\fibonacci\\setup.cfg",
            "temp_analysis/escape2020\\gammapy_gammapy\\gammapy-1.2\\setup.cfg"
        ]
    },
    "authors": {
        "count": 2,
        "files": [
            "temp_analysis/escape2020\\FairRootGroup_FairMQ\\FairMQ-master\\AUTHORS",
            "temp_analysis/escape2020\\R3BRootGroup_R3BRoot\\R3BRoot-jun24\\AUTHORS"
        ]
    },
    "contributors": {
        "count": 3
    },
    "license": {
        "count": 17
    },
    "codemeta.json": {
        "count": 16,
        "files": [
            "temp_analysis/escape2020\\aardk_jupyter-casa\\jupyter-casa-master\\codemeta.json",
            "temp_analysis/escape2020\\AMIGA-IAA_hcg-16\\hcg-16-1.2.3\\codemeta.json",
            "temp_analysis/escape2020\\cds-astro_aladin-lite\\aladin-lite-3.3.2\\codemeta.json",
            "temp_analysis/escape2020\\cds-astro_cds-moc-rust\\cds-moc-rust-main\\codemeta.json",
            "temp_analysis/escape2020\\cds-astro_mocpy\\mocpy-0.15.0\\codemeta.json",
            "temp_analysis/escape2020\\cds-astro_tutorials\\tutorials-1.0.3\\codemeta.json",
            "temp_analysis/escape2020\\cosimoNigro_agnpy\\agnpy-master\\codemeta.json",
            "temp_analysis/escape2020\\explore-platform_g-tomo\\g-tomo-2\\codemeta.json",
            "temp_analysis/escape2020\\FairRootGroup_FairMQ\\FairMQ-master\\codemeta.json",
            "temp_analysis/escape2020\\gammapy_gammapy\\gammapy-1.2\\codemeta.json",
            "temp_analysis/escape2020\\IndexedConv_IndexedConv\\IndexedConv-1.3.2\\codemeta.json",
            "temp_analysis/escape2020\\javierrico_gLike\\gLike-master\\codemeta.json",
            "temp_analysis/escape2020\\JColl88_sdc1-solution-binder\\sdc1-solution-binder-1.0.0\\codemeta.json",
            "temp_analysis/escape2020\\R3BRootGroup_R3BRoot\\R3BRoot-jun24\\codemeta.json",
            "temp_analysis/escape2020\\repo\\eossr-master\\codemeta.json",
            "temp_analysis/escape2020\\repo\\eossr-master\\eossr\\metadata\\schema\\codemeta.json"
        ]
    },
    "zenodo.json": {
        "count": 0,
        "files": []
    },
    "identifier_extract": {
        "count": 6,
        "extracted_values": [
            "10.5281/zenodo.1689985",
            "10.5281/zenodo.4055175",
            "10.5281/zenodo.3967385",
            "10.5281/zenodo.3967385",
            "10.5281/zenodo.10405177",
            "10.5281/zenodo.7544514"
        ]
    },
    "None": {
        "count": 0
    }
}
```

Should be noted, the "files" section is not be available due to the size of each repositories, it is impossible to upload it on GitHub, they are extracted from SOMEF. From these results, we can answer RQ1.





