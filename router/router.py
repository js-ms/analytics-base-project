from fastapi import APIRouter, HTTPException
from use_cases.crypto_use_cases import GetAllCryptocurrenciesUseCase, GetCryptocurrencyBySymbolUseCase

router = APIRouter(prefix="/crypto", tags=["cryptocurrency"])

@router.get("/")
def get_all_cryptocurrencies():
    try:
        return GetAllCryptocurrenciesUseCase.execute()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{symbol}")
def get_cryptocurrency(symbol: str):
    try:
        crypto = GetCryptocurrencyBySymbolUseCase.execute(symbol)
        if not crypto:
            raise HTTPException(status_code=404, detail="Cryptocurrency not found")
        return crypto
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
