import logging
from typing import Iterable, Union

logging.basicConfig(level="INFO")


class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price


class ProductBundle:
    def __init__(
        self,
        name: str,
        perc_discount: float,
        *products: Iterable[Union[Product, "ProductBundle"]],
    ) -> None:
        self._name = name
        self._perc_discount = perc_discount
        self._products = products

    @property
    def price(self) -> float:
        total = sum(p.price for p in self._products)  # type: ignore
        return total * (1 - self._perc_discount)


if __name__ == "__main__":
    p1 = Product("p1", 10)
    p2 = Product("p2", 20)
    p3 = Product("p3", 30)

    bundle1 = ProductBundle("bundle1", 0.1, p1, p2, p3)
    logging.info(bundle1.price)
