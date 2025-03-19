# Sno.ai Public Resources Mirror

This repository contains public resources for Sno.ai projects.

## Structure

- `i18n/` - Internationalization resources
  - Language directories (en, zh, ja, etc.)
  - Translation files in JSON format organized by feature
  - Each language follows the same structure for consistency

## Repository Setup

### For Contributors

To contribute to the translations:

1. Clone the repository:

```bash
git clone https://github.com/snoai/sno-ai-mirror-pub.git
cd sno-ai-mirror-pub
```

2.Create a new branch for your changes:

```bash
git checkout -b feature/update-translations
```

## Working with Translations

### Directory Structure

Each language has its own directory with JSON files:

```
i18n/
├── en/
│   ├── about.json
│   ├── auth.json
│   └── ...
├── zh/
│   ├── about.json
│   ├── auth.json
│   └── ...
└── ...
```

### Making Changes

1. Find the appropriate language directory
2. Locate or create the relevant JSON file
3. Make your changes following the existing format
4. Test your changes if possible
5. Commit using conventional commit format:

```bash
git commit -m "[update]/(i18n): update translations for feature X"
```

### Contributing Guidelines

1. Maintain consistent JSON structure across all languages
2. Keep translations professional and culturally appropriate
3. Test changes in the context of the application if possible
4. Follow the existing file naming conventions
5. Use UTF-8 encoding for all files

## For Projects Using This as a Submodule

### Updating the Submodule

When new translations are available:

```bash
# Navigate to the submodule directory
cd i18n/res

# Pull the latest changes
git pull origin main

# Go back to main project
cd ../..

# Update the submodule reference
git add i18n/res
git commit -m "[update]/(i18n): update i18n submodule"
```

### Making Changes Through Submodule

1. Navigate to the submodule directory:

```bash
cd i18n/res
```

2. Make your changes and commit:

```bash
git add .
git commit -m "[update]/(i18n): your change description"
git push origin main
```

3. Update the main repository:

```bash
cd ../..
git add i18n/res
git commit -m "[update]/(i18n): update i18n submodule"
git push origin main
```

## License

This project is licensed under the MIT License - see the LICENSE file for details
