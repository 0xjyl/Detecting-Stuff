# Detecting-Stuff
> A curated, evolving repository for **Cybersecurity Professional** — custom queries, validated scripts, and practical research to make detection building faster, and collaborative.

---

##  Navigation

| Category | Description |
|-----------|--------------|
| [**Manual**](./Manual) | Manual detections and validation logic (e.g., parent-child process verification). |
| [**Queries**](./Queries) | Detection queries for major platforms. |
| - [**CrowdStrike**](./Queries/CrowdStrike) | CrowdStrike Query Language (CQL) detections. |
| - [**Splunk**](./Queries/Splunk) | Splunk SPL content for behavioral and event-based detection. |
| - [**Misc**](./Queries/Misc) | Some niche tools have custom query languages, I'll try to source these and put them here for a central reference. I've also used niche tools like Netography, Corelight, Sublime, etc that all have their own query language. |
| [**Research**](./Research) | Ongoing technical research and detection-related investigations. |
| - [**Linux**](./Research/Linux) | Linux-specific. |
| - [**MacOS**](./Research/MacOS) | macOS-specific. |
| - [**Windows**](./Research/Windows) | Windows-specific. |
| [**Scripts**](./Scripts) | Mostly custom atomics that aren't parsed and are a PITA to remove the test cases. Don't duplicate work just use these. |
| - [**Atomics**](./Scripts/Atomics) | Custom atomic scripts for controlled TTP simulation. |

---

## Contribution Guidelines

Pull requests are welcomed — especially:

- Custom detections validated in production environments.
- Platform-specific research or TTP simulations.

Guidelines:

- Follow folder structure and naming convention.
- Include metadata headers and MITRE references.
    - metadata headers:

        ```yaml
        # metadata:
        #   author: 0xjyl
        #   platform: CrowdStrike
        #   description: Detects process injection via CreateRemoteThread
        #   tags: [injection, defense-evasion, process]
        #   mitre_attack: T1055
        #   status: verified

- Ensure detections are tested or reproducible.

---

## Support the Project

If this repository saves you time or sharpens your detections — give it a ⭐ and share it with another defender. Every contribution strengthens the community.