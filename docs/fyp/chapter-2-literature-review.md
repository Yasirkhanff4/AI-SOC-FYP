# Chapter 2 — Literature Review

## 2.1 SIEM and SOC Operations

A SIEM centralizes security telemetry, applies correlation and detection logic, and presents alerts for investigation. A SOC adds people, processes, playbooks, escalation, evidence handling, and reporting around those technical capabilities.

## 2.2 Intrusion Detection

Signature and rule-based detection is transparent and useful for known patterns. Its limitations include rule maintenance and sensitivity to changing behavior. AI-SOC therefore treats deterministic rules as the primary explainable layer and machine learning as an assisting signal rather than an autonomous decision maker.

## 2.3 Machine Learning in Cybersecurity

Classification models can learn from labeled examples, while anomaly-detection methods identify deviations from a baseline. Security datasets are often imbalanced, environment-specific, and vulnerable to concept drift. Consequently, this project reports precision, recall, F1-score, confusion matrix, and limitations rather than relying on accuracy alone.

## 2.4 Threat Intelligence

Threat intelligence enriches indicators such as IP addresses, domains, URLs, and hashes with reputation or context. Provider availability, rate limits, privacy concerns, and API keys are operational constraints. AI-SOC uses a provider interface and a local mock provider so the demonstration remains available offline.

## 2.5 MITRE ATT&CK

MITRE ATT&CK provides a common vocabulary for adversary tactics and techniques. The system stores a technique ID, tactic, name, evidence, and confidence. It does not invent a technique when the event does not support a confident mapping.

## 2.6 AI-Assisted Investigation

Language models can summarize structured context and suggest investigative questions, but can also produce unsupported statements. AI-SOC limits the model context to a controlled alert object and separates evidence, inference, recommendation, and uncertainty. Schema validation and analyst approval remain required.

## 2.7 Research Gap and Proposed Contribution

The project contribution is an academic, modular integration of detection, ML scoring, controlled AI analysis, threat intelligence fallback, MITRE mapping, incident workflow, and report generation in one safe demonstrator. It is not presented as a replacement for an enterprise SOC.

## 2.8 Citation Plan

Before submission, add verified sources in the citation style required by the university. Recommended authoritative sources include official MITRE ATT&CK documentation, Wazuh documentation, NIST incident-response guidance, OWASP API guidance, and peer-reviewed ML/security research. Every citation must be read and verified by the team.
