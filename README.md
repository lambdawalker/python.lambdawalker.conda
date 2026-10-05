# lambdawalker-conda

Conda environment interface utilities for LambdaWalker.

## Installation

```bash
pip install lambdawalker-conda
```

## Usage

```python
from lambdawalker.conda.interface import get_conda_env_location
assert get_conda_env_location is not None
print("conda OK")
```
