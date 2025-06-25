---
trigger: glob
globs: [yaml,yml,json,gradle,maven,pom.xml,js,ts,py,go,java,cs,dockerfile,sh,bash,batch,ps1]
---


  Ensure your software supply chain remains secure by following these core practices across source code, dependencies, build, and deployment environments.

labels: [security, supply-chain, best-practices]



    
      Enforce strong access controls with least privilege, use MFA, rotate credentials regularly,
      and never store secrets or credentials in code or plaintext files.
    languages: [all]
    pattern: ''
    negated: false
    action: advice


    
      Perform peer code reviews before merging to detect vulnerabilities or malicious changes.  
      Protect branches and enforce merge policies in your version control system.
    languages: [all]
    pattern: ''
    action: advice

    
      Vet third-party dependencies for active maintenance, security posture, and license compatibility.
      Use lockfiles or version pinning to fix dependency versions and prevent unintended upgrades.
    languages: [json, yaml, yml, gradle, maven, pom.xml, js, ts, py, go, java, cs]
    pattern: ''
    action: advice

    
      Maintain an up-to-date inventory of all dependencies and run automated vulnerability scans frequently,
      but verify scan results manually to reduce false positives and false negatives.
    languages: [json, yaml, yml, gradle, maven, pom.xml, js, ts, py, go, java, cs]
    pattern: ''
    action: advice


    
      Harden build environments by isolating build tools, using ephemeral containers or VMs,
      disabling unused services, and enforcing code signing with secured infrastructure.
    languages: [sh, bash, batch, ps1, dockerfile, yaml, yml]
    pattern: ''
    action: advice

    
      Use private artifact repositories to control binary sources and prevent bypass of repository policies.
      Keep build scripts and configurations under version control for audit and traceability.
    languages: [yaml, yml, sh, bash, groovy, gradle, maven, pom.xml, dockerfile]
    pattern: ''
    action: advice

    
      Generate and verify provenance metadata (e.g., SLSA 1.0) for build artifacts to ensure integrity
      and traceability throughout your supply chain.
    languages: [json, yaml, yml]
    pattern: ''
    action: advice


    
      Limit user-controlled parameters during builds to reduce injection and poisoning attack surfaces.
    languages: [sh, bash, batch, ps1, yaml, yml]
    pattern: ''
    action: advice


    
      Before deployment, run binary composition analysis to detect secrets, unauthorized content,
      or signs of tampering in final artifacts.
    languages: [all]
    pattern: ''
    action: advice


    
      Continuously monitor deployed software and its dependencies for vulnerabilities and configuration drift,
      and maintain accurate live inventories.
    languages: [all]
    pattern: ''
    action: advice
```
