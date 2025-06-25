---
trigger: glob
globs: .c, .cpp, .h, .hpp, .cc, .cxx, .inl, .mk, CMakeLists.txt
---

As a C/C++ developer, the security of your compiled application depends heavily on the options you pass to your compiler and linker. Modern toolchains provide a powerful set of features to harden your binaries against common exploitation techniques.

### 1. Compiler Flags for Hardening

These flags should be a standard part of your release build configuration.

*   **Enable All Warnings:** Warnings often point to latent bugs. Start with a strong baseline.
    *   **GCC/Clang:** `-Wall -Wextra -Wconversion`
*   **Stack Smashing Protection:** This adds a "canary" to the stack to detect buffer overflows before they can be exploited.
    *   **GCC/Clang:** `-fstack-protector-all`
*   **Position-Independent Executables (PIE):** This allows the operating system to load the application at a random memory address (ASLR), making it much harder for attackers to predict memory layouts.
    *   **Compiler:** `-fPIE`
    *   **Linker:** `-pie`
*   **Fortify Source:** This adds checks to common library functions (like `strcpy`, `printf`) to prevent buffer overflows.
    *   **GCC/Clang:** `-D_FORTIFY_SOURCE=2` (Note: requires optimization `-O1` or higher).

### 2. Linker Flags for Hardening

These flags control how your final executable is constructed.

*   **Relocation Read-Only (RELRO):** This makes parts of the binary read-only after the dynamic linker has done its work, preventing certain exploitation techniques like GOT overwrites.
    *   **GCC/Clang Linker:** `-Wl,-z,relro,-z,now`
*   **Non-Executable Stack (NX):** This prevents code from being executed from the stack, a hallmark of many exploits.
    *   **GCC/Clang Linker:** `-Wl,-z,noexecstack`

### 3. Build Configurations: Debug vs. Release

Maintain separate, distinct build configurations for development and production.

*   **Debug Builds:**
    *   Disable optimizations (`-O0`) and enable full debugging information (`-g3`).
    *   Define the `DEBUG` macro (`-DDEBUG`) and do **not** define `NDEBUG`.
    *   Use sanitizers to detect memory errors at runtime (e.g., `-fsanitize=address,undefined`).
*   **Release Builds:**
    *   Enable optimizations (e.g., `-O2`).
    *   Define the `NDEBUG` macro (`-DNDEBUG`) to disable assertions and debugging code. Do **not** define `DEBUG`.
    *   Include all the hardening flags mentioned above.

### 4. Using Assertions Effectively

Assertions are a powerful tool for catching bugs early.

*   **Best Practice:** Use `assert()` liberally in your code to check for pre-conditions, post-conditions, and invariants. Assertions are automatically disabled in release builds (when `NDEBUG` is defined), so they have no performance impact on your production code.

    ```c
    void process_data(char *data, size_t len) {
        assert(data != NULL && "Data pointer cannot be null!");
        // ...
    }
    ```

### 5. Verifying Your Binary

Don't just trust that the flags worked. Use a tool to check the security properties of your final executable.

*   **Linux:** Use the `checksec` tool.
*   **Windows:** Use Microsoft's BinScope.

By integrating these toolchain hardening practices into your CI/CD pipeline, you can significantly raise the bar for attackers and build more resilient and secure C/C++ applications.