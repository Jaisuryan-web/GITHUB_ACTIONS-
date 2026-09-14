# SImple Billing System in Python with GitHub Actions CI

A Python billing calculation system with automated unit testing via GitHub Actions.

## Project Structure
- `billing.py`: Core billing engine and line-item handling.
- `test_billing.py`: Test suite verifying calculations, discounts, and validation constraints.
- `.github/workflows/ci.yml`: GitHub Actions CI pipeline executing tests on push and pull requests.
- `requirements.txt`: Python package dependencies.

## How to Test Locally
```bash
pip install -r requirements.txt
pytest test_billing.py -v
```

## How to Test on GitHub Actions
1. Push this folder to a GitHub repository main branch.
2. Observe the green checkmark under the **Actions** tab (Case 1: Success).
3. Alter `billing.py` to produce a faulty calculation and push to see the workflow fail with a red cross (Case 2: Error).
