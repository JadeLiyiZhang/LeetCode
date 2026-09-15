class ProductOfNumbers:

    def __init__(self):
        self.pre_product = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.pre_product.append(num * self.pre_product[-1])
        else:
            self.pre_product = [1]

    def getProduct(self, k: int) -> int:
        if k >= len(self.pre_product):
            return 0
        else:
            product = self.pre_product[-1] // self.pre_product[-k - 1]
            return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)