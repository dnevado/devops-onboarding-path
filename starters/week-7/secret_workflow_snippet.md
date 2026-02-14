# Secrets Best Practice Snippet

Example workflow snippet safely referencing a secret:

```yaml
env:
  MY_API_KEY: ${{ secrets.MY_API_KEY }}

steps:
  - name: Use secret
    run: |
      # never echo the secret
      python -c "import os; print('has secret:', 'MY_API_KEY' in os.environ)"
```

Notes:
- Do not print secrets to logs.
- Use least privilege for tokens.
- Consider short-lived credentials or vault integrations for production.
