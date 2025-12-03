# Setting Up Task 4 on Another Machine

## Quick Setup Guide

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd weather-mcp-server-main
```

### 2. Install Dependencies

**On Linux/macOS:**
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

**On Windows:**
```powershell
# Install uv if not already installed
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install dependencies
uv sync
```

### 3. Run the Script

```bash
# Linux/macOS
uv run python bert_dist.py

# Windows PowerShell
$env:Path = "$HOME\.local\bin;$env:Path"
uv run python bert_dist.py
```

## What Gets Downloaded Automatically

The script will automatically download:
- **SQuAD dataset** (~16MB) - first run only
- **BERT-base tokenizer** (~700KB) - first run only  
- **BERT-base model** (~440MB) - first run only
- **BERT-large teacher model** (~1.34GB) - first run only

**Total download**: ~1.8GB on first run

## Faster Testing (Optional)

If you want to test faster before full training, you can temporarily reduce:

**In `bert_dist.py`, modify Config class:**
```python
class Config:
    # ... other settings ...
    batch_size = 16  # Increase if you have more GPU memory
    epochs = 1  # Reduce from 2 to 1 for faster testing
    # ... other settings ...
```

**Or reduce dataset size (in main function):**
```python
train_set = raw["train"].select(range(1000))  # Instead of 10000
val_set = raw["validation"].select(range(10))  # Instead of 50
```

## GPU Acceleration

If the other machine has a GPU:
- PyTorch will automatically detect and use CUDA
- Training will be **much faster** (5-15 minutes vs 7+ hours on CPU)
- No code changes needed - it's automatic!

## Expected Runtime

- **CPU**: 5-10 hours for full training (10K samples, 2 epochs)
- **GPU**: 10-30 minutes for full training
- **First run**: Add 5-10 minutes for model downloads

## Output Files

After training completes, you'll see:
- Training loss values printed to console
- Evaluation metrics (F1, Exact Match) printed to console
- **Screenshot these for Deliverable 2!**

No checkpoint files are saved (they're in `.gitignore`), but you can capture the console output.

## Troubleshooting

### PyTorch CUDA Issues
If GPU isn't detected:
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

Should print `True` if GPU is available.

### Memory Issues
If you get "out of memory" errors:
- Reduce `batch_size` from 8 to 4 or 2
- Reduce training samples from 10000 to 5000

### Windows Visual C++ Error
If you see DLL errors on Windows:
```powershell
winget install Microsoft.VCRedist.2015+.x64 --silent --accept-package-agreements --accept-source-agreements
```

