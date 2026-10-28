### 📊 Architectural Performance Benchmark (5001 x 5001)

| Environment / Architecture | Active Device | Processing Time | Execution Type |
| :--- | :--- | :--- | :--- |
| **Traditional Algorithmic Loops** | CPU | *Hours / Timeout* | Sequential $O(n^2)$ |
| **Vectorized NumPy Script** | CPU (Intel Xeon) | ~1.3869s | Vectorized Broadcasting |
| **PyTorch Tensor Framework** | CPU (Optimized) | 0.8488s | Parallelized Multi-Thread Core |
| **PyTorch + CUDA Execution** | GPU (NVIDIA T4) | *Natively Supported* | Massively Parallel $O(1)$ |
