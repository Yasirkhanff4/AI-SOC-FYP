# Viva Questions and Short Answers

1. **Why is SIEM useful?** It centralizes telemetry, correlation, search, and alert workflows.
2. **What is a SOC?** A people-process-technology function for monitoring, investigation, and response.
3. **Why Wazuh?** It provides an accessible educational HIDS/SIEM ecosystem and agent-based collection.
4. **Why FastAPI?** It provides typed validation, automatic OpenAPI documentation, and good Python integration.
5. **Why React?** It supports modular, stateful analyst interfaces.
6. **Why PostgreSQL?** It provides relational integrity, indexing, and production suitability.
7. **Why SQLite fallback?** It simplifies local development and offline demonstrations.
8. **What is an event?** A normalized observation from a host, application, or security source.
9. **What is an alert?** A detection result that requires analyst review.
10. **What is an incident?** A tracked investigation that may contain related alerts, evidence, notes, and actions.
11. **What is an IOC?** An observable such as an IP, domain, URL, hash, or account indicator.
12. **What is MITRE ATT&CK?** A knowledge base of adversary tactics and techniques.
13. **Why map T1110?** Repeated credential attempts support the Brute Force technique.
14. **Why map T1046?** Multiple service probes support Network Service Discovery.
15. **What is rule-based detection?** Explicit conditions that are transparent and testable.
16. **What is anomaly detection?** Identifying behavior that differs from a learned baseline.
17. **Why use Random Forest?** It is a strong, interpretable tabular baseline with limited preprocessing.
18. **Why use Isolation Forest?** It can assist when labels are limited, although it is not required for every experiment.
19. **Why not claim perfect accuracy?** Synthetic data can be easier than real telemetry and does not represent production prevalence.
20. **Why precision?** It describes how many predicted positives were relevant.
21. **Why recall?** It describes how many relevant positives were found.
22. **Why F1-score?** It balances precision and recall.
23. **What is a false positive?** A benign event incorrectly flagged as suspicious.
24. **What is a false negative?** A suspicious event missed by the detector.
25. **What is risk scoring?** A transparent combination of severity, confidence, reputation, and correlation factors.
26. **Can AI determine severity alone?** No; the deterministic score and analyst review constrain it.
27. **How is hallucination reduced?** Controlled structured context, schema validation, evidence separation, and uncertainty fields.
28. **Does AI have database access?** No; it receives a bounded alert context.
29. **What happens without an LLM key?** Deterministic demo analysis keeps the workflow available.
30. **What happens without threat-intel APIs?** The local mock provider is used and labeled.
31. **How are passwords protected?** They are stored as bcrypt hashes, never plaintext.
32. **What is JWT?** A signed token carrying authenticated claims and expiration.
33. **What is RBAC?** Permission decisions based on user role.
34. **What can a Viewer do?** View permitted dashboards, alerts, and reports without modifying incidents.
35. **Why audit logging?** It supports accountability and investigation history.
36. **Why environment variables?** They keep credentials out of source code and frontend bundles.
37. **What is normalization?** Converting different log formats into common fields.
38. **Why use synthetic data?** It is safe, reproducible, and appropriate for a controlled FYP demo.
39. **Does synthetic data prove production performance?** No.
40. **What is Wazuh's role?** Collection and security monitoring integration in the lab.
41. **What is safe automation?** Recommendations or simulated actions requiring analyst approval.
42. **Why not automatically block IPs?** Destructive or disruptive decisions require policy and human approval.
43. **How is SQL injection reduced?** Pydantic validation and SQLAlchemy parameterized queries.
44. **How is XSS reduced?** React escaping and avoiding unsafe HTML rendering.
45. **Why PostgreSQL indexes?** They improve lookup performance for frequently queried fields.
46. **How does incident closure work?** An analyst verifies evidence, records resolution, and changes status to CLOSED.
47. **What belongs in the PDF report?** Timeline, severity, evidence, analysis, mappings, actions, notes, and resolution.
48. **What is RAG?** Retrieval-augmented generation grounded in selected knowledge documents.
49. **What are major limitations?** Synthetic data, limited integrations, mock providers, and advisory AI.
50. **How could it scale?** Queue-based ingestion, partitioned events, caching, model serving, and horizontally scaled APIs.
51. **Why separate frontend and backend?** It improves modularity, testing, and deployment flexibility.
52. **How is the model versioned?** Store the artifact, feature definition, metrics, and training configuration together.
53. **What is concept drift?** A change in normal behavior that reduces model relevance.
54. **How would you validate Wazuh integration?** Ingest a controlled event and trace it through normalization and alert creation.
55. **What is the main contribution?** A safe, explainable, end-to-end SOC workflow suitable for academic demonstration.
