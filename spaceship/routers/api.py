from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get("/matmul")
def matmul():
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    product = a @ b          # or np.matmul(a, b)
    return {
        "matrix_a": a.tolist(),
        "matrix_b": b.tolist(),
        "product":  product.tolist(),
    }

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}
