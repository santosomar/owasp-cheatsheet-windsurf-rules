```yaml
---
trigger: glob
globs: [c, cpp, h, hpp, cc, cxx, inl]
---
when:
  any:
    - pattern: 'assert\('
    - pattern-either:
        - pattern: '#\s*define\s+DEBUG'
        - pattern: '#\s*define\s+NDEBUG'
    - pattern-either:
        - pattern: '-DDEBUG'
        - pattern: '-DNDEBUG'
    - pattern: '-Wall'
    - pattern: '-fstack-protector-all'
    - pattern: '-fPIE'
    - pattern: '-pie'
    - pattern: '-z,noexecstack'
    - pattern: '-z,relro'
    - pattern: '-z,now'
    - pattern: '-mfunction-return=thunk'
    - pattern: '-mindirect-branch=thunk'
    - pattern: '_CRT_SECURE_NO_WARNINGS'
    - pattern: '_SCL_SECURE_NO_WARNINGS'
    - pattern: '-U_FORTIFY_SOURCE'
then:
  message: |
    ⚠️ **Build Configuration & Security Best Practices**

    1. **Maintain distinct Debug and Release builds:**
       - Debug: Use instrumentation (e.g., GCC `-O0 -g3 -ggdb`), define `DEBUG`, do **not** define `NDEBUG`.
       - Release: Optimize (e.g., GCC `-O2 -g2`), define `NDEBUG`, do **not** define `DEBUG`.
       - Optionally, use a Test build exposing internals for thorough testing.

    2. **Use assertions properly:**
       - Assert liberally for input validation and state checking.
       - Replace standard `assert()` abort behavior with custom handlers that trigger debugger traps (e.g., `SIGTRAP`) in Debug builds.
       - Disable assertions in Release builds (`NDEBUG` defined) to avoid crashes.

    3. **Enable comprehensive compiler and linker security flags:**
       - Enable warnings: `-Wall -Wextra -Wconversion -Wformat=2 -Wformat-security`.
       - Enable protections: `-fstack-protector-all`, `-fPIE -pie`, `-z,noexecstack`, `-z,relro`, `-z,now`.
       - Apply CPU mitigations as appropriate (`-mfunction-return=thunk`, `-mindirect-branch=thunk`).

    4. **Respect user and environment flags:**
       - When overriding build flags (Make/Autotools), merge user-provided flags carefully to not lose security hardening.
       - Avoid accidental mixing of Debug instrumentation in Release builds.

    5. **Integrate diagnostics and platform mitigations:**
       - Use sanitizers (AddressSanitizer, DMalloc) in Debug builds.
       - Enable OS mitigations (ASLR via PIE, DEP/NX).
       - Validate binary hardening with tools like `checksec` (Linux) or BinScope (Windows).

    6. **Manage 3rd-party libraries securely:**
       - Audit and configure dependencies securely (e.g., disable obsolete SSL versions in OpenSSL).
       - Avoid blind trust in default library build options.

    7. **Preprocessor macro discipline:**
       - Never define both `DEBUG` and `NDEBUG`.
       - Default to `NDEBUG` if neither is defined.
       - Avoid disabling security warnings via macros like `_CRT_SECURE_NO_WARNINGS`.

    8. **Proactive static and dynamic analysis:**
       - Leverage compiler warnings and static analyzers.
       - Enable runtime diagnostics (Xcode malloc guards, Visual Studio MDAs).

    9. **Suppress compiler warnings sparingly:**
       - Only suppress unavoidable warnings selectively.
       - Prefer explicit error handling and assertions over disabling warnings.

    10. **Runtime protections:**
        - Enable platform-specific runtime exploit mitigations and monitoring tools.

    **Summary:** Adopt and enforce distinct Debug and Release builds with strong compiler/linker security flags and custom asserts. Honor user build flags carefully, integrate diagnostics, avoid disabling warnings unsafely, and secure 3rd-party libraries to produce robust, self-debugging, and hardened software.
```