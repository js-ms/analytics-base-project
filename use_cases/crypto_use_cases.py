from repositories.crypto_repository import CryptoRepository

class GetAllCryptocurrenciesUseCase:
    @staticmethod
    def execute():
        repo = CryptoRepository()
        return repo.get_all_cryptocurrencies()

class GetCryptocurrencyBySymbolUseCase:
    @staticmethod
    def execute(symbol: str):
        repo = CryptoRepository()
        return repo.get_cryptocurrency_by_symbol(symbol)
