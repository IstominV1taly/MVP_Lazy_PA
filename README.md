# MVP Lazy PA
![Lazy_PA_logo](design/resize.png)
## Overview

**MVP_Lazy_PA** is my first Python project and my first attempt at building a simple product analytics workflow.

The goal of this project is not to create a perfect production-ready system from the start, but to build a working prototype step by step, improve the project structure, and practice both programming fundamentals and analytical thinking.

This repository is intentionally simple. It is an early MVP that I use to learn, experiment, and gradually turn separate ideas into a structured workflow.

---

## Project goal

The main goal of the project is to build a small but clear analytical pipeline that can:

1. load raw data,
2. process and clean it,
3. analyze key patterns,
4. interpret the results,
5. prepare final conclusions.

At this stage, the project focuses more on building a solid structure than on implementing complex business logic.

---

## Current status

At the moment, the project already includes:

- a basic package structure,
- a Jupyter notebook interface for experiments,
- separate modules for future processing and analysis steps,
- configuration and dependency files,
- a synthetic dataset for testing the workflow,
- first steps toward cleaner project organization.

The analytical logic is still under development.

---

## Planned workflow

The expected workflow of the project is:

1. **Load raw data**
2. **Process and clean data**
3. **Analyze patterns and metrics**
4. **Interpret results**
5. **Prepare conclusions and recommendations**

---

## Project structure

```text
MVP_Lazy_PA/
├── app/
│   ├── config.py
│   ├── data_processing.py
│   ├── analysis.py
│   ├── interpretation.py
│   └── conclusions.py
├── bumper/
├── design/
├── input/
│   └── sintetic_raw_dataset.csv
├── tests/
├── interface.ipynb
├── resize.png
├── README.md
├── pyproject.toml
└── requirements.txt