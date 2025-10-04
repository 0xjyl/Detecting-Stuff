# Detecting-Stuff 

> **A centralized repository for Detection Engineers —** practical detections, validated scripts, and deep research designed to accelerate the creation, testing, and sharing of detection logic.

![Last Updated](https://img.shields.io/github/last-commit/0xjyl/Detecting-Stuff?label=Last%20Updated&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/0xjyl/Detecting-Stuff?style=for-the-badge)
![License](https://img.shields.io/github/license/0xjyl/Detecting-Stuff?style=for-the-badge)

---

## Table of Contents
1. [Project Overview](#-roject-overview)
2. [Motivation & Purpose](#motivation--purpose)
3. [Repository Structure](#repository-structure)
4. [How to Use](#how-to-use)
5. [Conributions](#contributions)

---

## Project Overview

**Detecting-Stuff** is an open-source resource built for and by **Detection Engineers** and **Cybersecurity Professionals**.   
It’s a centralized hub of ready-to-use detections, research, and practical scripts that bridge the gap between *theory* and *execution* in detection engineering, content/control validation, and purple teaming.

This project contains:
- **Custom queries** for major platforms like CrowdStrike and Splunk.  
- **Reusable atomic scripts** for testing and validation, that are a bit more custom to the OS. 
- **Manual detection guidance** for nuanced detection rules that have strict execution parameters. 
- **Research repositories** focused on OS-specific detection/behavioral investigations. 

---

## Motivation & Purpose

**Why this project exists:**
- Detection Engineering is scattered — valuable detections are buried in wikis, slides, and forums. 
- Many teams duplicate effort when building baselines or writing correlation rules. I hated that I had to build something that kind-of existed. 
- Community knowledge should be **shared, validated, and accessible** — not lost to private backlogs or internal runbooks...
    - I know this is a bit controversial but my personal theory is that attackers already have an advantage with tooling, resources, techniques, etc. Why not bolster our defenses together from individual contribution? Why hide this information?

**What problem this solves:**
- Centralizes detections from multiple ecosystems and knowledge bases (that aren't proprietary to any company internally). 
- Provides reusable logic for detection engineers, purple teamers, incident responders, etc.
- Encourages open collaboration for high-quality, tested detections.

---

## Repository Structure

| Directory | Description |
|------------|--------------|
| [**Manual/**](./Manual) | Niche items for specific attack processes/detection parameters. |
| [**Queries/**](./Queries) | Core of the repo — organized queries. |
| |-- [**CrowdStrike/**](./Queries/CrowdStrike) | CrowdStrike Query Language (CQL) detections. |
| |-- [**Splunk/**](./Queries/Splunk) | Splunk (SPL) detections for behavioral and event correlation. |
| |-- [**Misc/**](./Queries/Misc) | Custom detections for niche tools like Netography, Corelight, Sublime, etc. |
| [**Research/**](./Research) | Technical detection research |
| |-- [**Linux/**](./Research/Linux) | Linux stuff |
| |-- [**MacOS/**](./Research/MacOS) | MacOS stuff |
| |-- [**Windows/**](./Research/Windows) | Windows stuff |
| [**Scripts/**](./Scripts) | Various scripts for niche emulations/validations |
| |-- [**Atomics/**](./Scripts/Atomics) | Custom atomics relevant to the OS / TTP |

---

## How to Use

You can **browse**, **copy**, or **download** anything you find useful for your environment. 

**Support the Project**

If this repository saves you time or sharpens your detections — give it a ⭐ and share it with another professional. Every contribution strengthens the community.

---

## Contributions

Pull requests are welcomed — especially:

- Custom detections validated in production environments.
- Platform-specific research or TTP simulations.
- Enhancements to logic, queries, scripts, research, etc.

**Contribution Guidelines**

This isn't entirely strict but having some coordination will help the stability of this project:

- Follow folder structure and naming convention.
- Ensure detections are tested or reproducible.
- Include metadata headers and MITRE references.
    - Example Metadata Block:

        ```yaml
        # metadata:
        #   author: 0xjyl
        #   platform: CrowdStrike
        #   description: Detects process injection via CreateRemoteThread
        #   tags: [injection, defense-evasion, process]
        #   mitre_attack: T1055
        #   status: verified
