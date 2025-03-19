# Contributing to i18n Resources

Thank you for considering contributing to our i18n resources! This document provides guidelines and instructions for contributing translations.

## How to Contribute

1. **Fork the Repository**: Create a fork of this repository to your GitHub account.

2. **Clone Your Fork**: Clone your fork to your local machine.
   ```
   git clone https://github.com/YOUR-USERNAME/sno-ai-mirror.git
   cd sno-ai-mirror/i18n
   ```

3. **Create a Branch**: Create a branch for your changes.
   ```
   git checkout -b improve-translations
   ```

4. **Make Your Changes**: Update or add translation files as needed.

5. **Run the Helper Script** (Optional): If adding new keys, you can use the helper script to ensure consistency.
   ```
   python scripts/add-missing-json-fields.py
   ```

6. **Commit Your Changes**: Commit with a clear message.
   ```
   git commit -am "[docs]: add French translations for blog section"
   ```

7. **Push to Your Fork**: Push your changes to your fork.
   ```
   git push origin improve-translations
   ```

8. **Create a Pull Request**: Open a pull request from your fork to the main repository.

## Translation Guidelines

- Always maintain the same JSON structure as the English version
- Don't remove any keys from files
- If you're unsure about a translation, you can leave it in English and add a comment
- Maintain the same formatting (e.g., placeholders like `{username}`)
- Don't translate variables or placeholders

## File Structure

Each language has its own directory with JSON files for different sections:

```
res/
├── en/            # English (source/fallback)
│   ├── auth.json  # Authentication related texts
│   ├── blog.json  # Blog related texts
│   └── ...
├── fr/            # French
│   ├── auth.json
│   └── ...
└── ...
```

## JSON Format

Translation files use simple key-value pairs in JSON format:

```json
{
  "welcome": "Welcome to our application",
  "login": "Log in",
  "signup": "Sign up",
  "nested": {
    "key": "Nested translation"
  }
}
```

## Testing Your Translations

While we don't provide a direct way to test translations in this repository, you can verify:

1. Your JSON is valid (no syntax errors)
2. All keys from the English version are present
3. Placeholders are preserved

The easiest way to validate JSON is using tools like [JSONLint](https://jsonlint.com/).

## Questions?

If you have any questions or need assistance, please open an issue in the repository, and we'll be happy to help! 