## Examples

Below are end-to-end examples demonstrating common scenarios. Replace placeholder names with your actual package and modules once available.

### Example: Initialize and run a job

```python
from myapp import Client

client = Client(api_key="test_key")
result = client.run_job(params={"size": 10})
print(result)
```

### Example: Handling errors

```python
from myapp import Client, MyAppError

client = Client(api_key="test_key")
try:
    client.run_job(params={"size": -1})
except MyAppError as exc:
    print(f"Failed to run job: {exc}")
```
