# Chapter 5 — Testing and Results

## 5.1 Functional Tests

Record pass/fail evidence for:

| ID | Test | Expected result | Result |
|---|---|---|---|
| T-01 | Valid login | Access token returned | [TO BE MEASURED] |
| T-02 | Invalid login | 401 response | [TO BE MEASURED] |
| T-03 | Event ingestion | Event persisted | [TO BE MEASURED] |
| T-04 | Brute-force detection | Alert generated | [TO BE MEASURED] |
| T-05 | AI analysis | Schema-valid response | [TO BE MEASURED] |
| T-06 | MITRE lookup | Supported technique returned | [TO BE MEASURED] |
| T-07 | Incident closure | Status becomes CLOSED | [TO BE MEASURED] |
| T-08 | PDF generation | Report file created | [TO BE MEASURED] |

## 5.2 Security Tests

Test authorization on every modifying route, invalid and expired tokens, input validation, SQL injection-safe ORM queries, XSS-safe rendering, rate limits, CORS configuration, and secret exclusion. Record the exact command, environment, date, and result.

## 5.3 ML Results

Populate this table only from `ml/models/metrics.json`:

| Metric | Baseline | Advanced | Selected |
|---|---:|---:|---:|
| Accuracy | [MEASURED] | [MEASURED] | [MEASURED] |
| Precision | [MEASURED] | [MEASURED] | [MEASURED] |
| Recall | [MEASURED] | [MEASURED] | [MEASURED] |
| F1-score | [MEASURED] | [MEASURED] | [MEASURED] |
| ROC-AUC | [MEASURED] | [MEASURED] | [MEASURED] |

Explain false positives and false negatives using actual test records. Do not generalize synthetic-data results to production environments.

## 5.4 Performance Results

Measure API response time, event processing time, alert generation time, dashboard load time, and AI response time. Record hardware, container configuration, number of records, and measurement method.

| Operation | Samples | Median | P95 | Environment |
|---|---:|---:|---:|---|
| Health endpoint | [MEASURED] | [MEASURED] | [MEASURED] | [MEASURED] |
| Event ingestion | [MEASURED] | [MEASURED] | [MEASURED] | [MEASURED] |
| Alert creation | [MEASURED] | [MEASURED] | [MEASURED] | [MEASURED] |

## 5.5 Limitations

The dataset is synthetic, provider responses may be mocked, the AI output is advisory, Wazuh integration depends on the lab environment, and the implementation is not validated as an enterprise production SOC. These limitations must appear in the defense.
