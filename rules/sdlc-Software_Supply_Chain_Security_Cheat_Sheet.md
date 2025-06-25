```yaml
---
trigger: glob
globs: [yaml,yml,json,gradle,maven,pom.xml,js,ts,py,go,java,cs,dockerfile,sh,bash,batch,ps1]
---

id: ssc-001
title: Secure Software Supply Chain Best Practices
description: |
  Ensure your software supply chain remains secure by following these core practices across source code, dependencies, build, and deployment environments.
severity: warning
labels: [security, supply-chain, best-practices]

rules:
  - id: ssc-001-01
    message: >
      Enforce strong access controls with least privilege, use MFA, rotate credentials regularly,
      and never store secrets or credentials in code or plaintext files.
    languages: [all]
    pattern: ''
    negated: false
    action: advice

  - id: ssc-001-02
    message: |
      Perform peer code reviews before merging to detect vulnerabilities or malicious changes.  
      Protect branches and enforce merge policies in your version control system.
    languages: [all]
    pattern: ''
    action: advice

  - id: ssc-001-03
    message: >
      Vet third-party dependencies for active maintenance, security posture, and license compatibility.
      Use lockfiles or version pinning to fix dependency versions and prevent unintended upgrades.
    languages: [json, yaml, yml, gradle, maven, pom.xml, js, ts, py, go, java, cs]
    pattern: ''
    action: advice

  - id: ssc-001-04
    message: >
      Maintain an up-to-date inventory of all dependencies and run automated vulnerability scans frequently,
      but verify scan results manually to reduce false positives and false negatives.
    languages: [json, yaml, yml, gradle, maven, pom.xml, js, ts, py, go, java, cs]
    pattern: ''
    action: advice

  - id: ssc-001-05
    message: >
      Harden build environments by isolating build tools, using ephemeral containers or VMs,
      disabling unused services, and enforcing code signing with secured infrastructure.
    languages: [sh, bash, batch, ps1, dockerfile, yaml, yml]
    pattern: ''
    action: advice

  - id: ssc-001-06
    message: >
      Use private artifact repositories to control binary sources and prevent bypass of repository policies.
      Keep build scripts and configurations under version control for audit and traceability.
    languages: [yaml, yml, sh, bash, groovy, gradle, maven, pom.xml, dockerfile]
    pattern: ''
    action: advice

  - id: ssc-001-07
    message: >
      Generate and verify provenance metadata (e.g., SLSA 1.0) for build artifacts to ensure integrity
      and traceability throughout your supply chain.
    languages: [json, yaml, yml]
    pattern: ''
    action: advice

  - id: ssc-001-08
    message: >
      Limit user-controlled parameters during builds to reduce injection and poisoning attack surfaces.
    languages: [sh, bash, batch, ps1, yaml, yml]
    pattern: ''
    action: advice

  - id: ssc-001-09
    message: >
      Before deployment, run binary composition analysis to detect secrets, unauthorized content,
      or signs of tampering in final artifacts.
    languages: [all]
    pattern: ''
    action: advice

  - id: ssc-001-10
    message: >
      Continuously monitor deployed software and its dependencies for vulnerabilities and configuration drift,
      and maintain accurate live inventories.
    languages: [all]
    pattern: ''
    action: advice
```
