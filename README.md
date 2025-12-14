# AI-Powered Threat Hunting Bot for Microsoft Defender & Azure

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)](https://platform.openai.com/)
[![Azure](https://img.shields.io/badge/Azure-Log%20Analytics-blue)](https://azure.microsoft.com/en-us/services/monitor/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**An intelligent threat hunting assistant** that combines natural language processing (OpenAI GPT) with real-time log analysis from Microsoft Defender for Endpoint and Azure AD — rebuilt from scratch to deepen understanding of AI-driven security operations.

This project was rebuilt during my cybersecurity internship as a hands-on learning exercise: taking a working AI SOC analyst bot and reconstructing it module-by-module to master the integration of LLMs, Azure Log Analytics, function calling, and threat intelligence workflows.

## Why I Rebuilt This Bot

I was given access to a fully functional AI threat hunting system, but I wanted to truly **own** the knowledge. Instead of just using or tweaking it, I decided to rebuild it from the ground up. This allowed me to:

- Understand how LLMs interpret natural language hunting queries
- Master OpenAI function calling for structured query planning
- Learn secure integration with Azure Log Analytics using KQL
- Implement MITRE ATT&CK mapping and IOC extraction
- Build professional-grade prompt engineering for threat detection
- Practice secure development (secrets management, input validation, guardrails)

## How It Works (High-Level Architecture)

```text
User Input (Natural Language)
       ↓
GPT decides: Table + Fields + Filters (via Function Calling)
       ↓
Query Azure Log Analytics Workspace (Real MDE & Azure AD logs)
       ↓
Returned logs → GPT Threat Analysis Engine
       ↓
Structured Findings: Title, MITRE Mapping, Confidence, IOCs, Recommendations
       ↓
Color-coded display + Saved to _threats.jsonl
```

## Key Features

- Natural language threat hunting ("Check for brute force on windows-target-1")
- Intelligent table/field selection using OpenAI function calling
- Real-time querying of Defender for Endpoint and SigninLogs
- Automated MITRE ATT&CK technique mapping
- Confidence scoring and actionable recommendations
- Secure design: API keys never committed

## Project Rebuild Journey (My Learning Path)

I rebuilt this system in phases to ensure each component worked perfectly before moving on:

| Phase | Goal                  | Key Learnings                                                                 |
|-------|-----------------------|-------------------------------------------------------------------------------|
| 1     | Setup & Auth          | Azure DefaultAzureCredential, secure key management                           |
| 2     | Query Planning        | OpenAI function calling, structured outputs                                   |
| 3     | Log Retrieval         | KQL construction, pandas for data handling                                    |
| 4     | Threat Analysis       | Prompt engineering, JSON schema enforcement                                   |
| 5     | Output & Logging      | Colorama formatting, JSONL append mode                                        |
| 6     | Guardrails & Polish   | Validation, model selection, error handling, token estimation, rate limit awareness |

## Demo Example

**User asks:**  
> "Any suspicious logon attempts against administrator accounts in the last 48 hours?"

**Bot responds with:**
- Detected brute-force attempts from multiple external IPs
- Mapped to MITRE T1110.001 (Password Guessing)
- High confidence findings
- IOCs extracted (IP addresses, usernames)
- Recommendations: block IPs, review lockout policies

## Setup Instructions (For Reviewers/Evaluators)

> **Note**: This project requires access to an Azure Log Analytics workspace with Microsoft Defender and Azure AD logs, plus an OpenAI API key.

### 1. Project folder and GitHub repo created
- Repository URL: <FILL IN YOUR REPO URL>
- Local folder: <FILL IN PATH>

### 2. Git initialized and first commit pushed
- `.gitignore` created with venv/, _keys.py, etc.
- Initial commit message: <FILL IN>

### 3. Virtual environment created and activated
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


### #. Title Here
- Description: Info
- Description: Info

### 2. Git initialized and first commit pushed
- Description: Info
- Description: Info

### 3. Virtual environment created and activated
- Description: Info
- Description: Info



## Future Improvements (Planned)

- [ ] Streamlit web interface
- [ ] Support for more MDE tables (Process, Network, File events)
- [ ] Automated incident creation via Microsoft Graph
- [ ] Chunking for large log sets
- [ ] Unit tests and CI/CD pipeline

## Acknowledgments

Built during my cybersecurity internship. Special thanks to my team for providing access to real logs and a production-grade starting system — this rebuild was my way of going deeper.

**Rebuilt from scratch to learn, not just to use.**
