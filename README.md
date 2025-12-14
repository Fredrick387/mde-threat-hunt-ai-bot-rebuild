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
