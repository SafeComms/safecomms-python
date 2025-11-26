# SafeComms Python SDK

Official Python client for the SafeComms API.

## Installation

```bash
pip install safecomms
```

## Usage

```python
from safecomms import SafeCommsClient

client = SafeCommsClient(api_key="your-api-key")

# Moderate text
result = client.moderate_text(
    content="Some text to check",
    language="en",
    replace=True
)
print(result)

# Get usage
usage = client.get_usage()
print(usage)
```
