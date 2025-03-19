# i18n Resources

This directory contains translation resources for the Sno.ai project. We welcome contributions to improve translations or add new languages.

## Structure

1. Each language has its own directory (e.g., `en`, `zh`, `ja`, `ko`, etc.) inside the `res` folder
2. Each language directory has individual JSON files for different sections of the application
3. If any translation key is not found in a non-English language, it will fallback to English (`en`)

## Contributing

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute to translations.

## Supported Languages

- English (`en`) - Default/fallback language
- German (`de`)
- Spanish (`es`)
- French (`fr`)
- Chinese Traditional (`zh-Hant`)
- Chinese Simplified (`zh`)
- Japanese (`ja`)
- Korean (`ko`)
- Russian (`ru`)

## Helper Scripts

- `scripts/add-missing-json-fields.py` - Script to add missing translation keys from English to other languages 