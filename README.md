# OWASP Cheatsheet Windsurf Rules

In this repository, we will implement the OWASP Cheatsheets as Windsurf IDE Rules. Users can explicitly define their own rules for Cascade (the Windsurf IDE Agent) to follow.

Rules can be defined at either the global level or the workspace level.

`global_rules.md` - rules applied across all workspaces

`.windsurf/rules` - workspace level repo containing rules that are tied to globs or natural language descriptions.

This repository has a script that converts the OWASP Cheatsheets into Windsurf Rules at the workspace level and stored in the `.windsurf/rules` directory.