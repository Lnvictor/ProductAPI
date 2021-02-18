from models import Product
from base import conn


class ProductDoesNotExistsException(Exception):
    """
    Exception raised when a query for a given product
    doesn't has a successfully result
    """

    pass


class ProductController:
    """
    Product Controller is the responsible
    for all Product data handling about database
    persistence...
    """

    def __init__(self, connection):
        self.conn = connection

    def save(self, name: str, desc: str, value: float) -> Product:
        """
        Create an Product instance and storages in the database..

        :param name: Product name
        :param desc: Product string description
        :param value: Determined value for a given product

        :return: The instance created
        """

        p = Product(name=name, desc=desc, value=value)
        p.save()
        return p

    def get_by_name(self, name: str) -> Product:
        """
        returns Product instance given the name

        :param name: str
        :return: Product
        """
        p = Product.objects(name=name).first()
        if p is None:
            raise ProductDoesNotExistsException()
        return p

    def change(self, p_name: str, **kwargs) -> Product:
        """
        Update

        :param id: primary key for Product obj
        :param kwargs: optional Product fields to be updated

        :return: Product instance
        """
        for key in kwargs:
            value = kwargs[key]
            product = Product.objects(name=p_name).first()

            if key == "name" and value is not None:
                product.name = value
            elif key == "desc" and value is not None:
                product.desc = value
            elif key == "value" and value is not None:
                product.value = float(value)

            product.save()
            return product

    def get(self):
        """
        get all products

        :return: list
        """

        return list(Product.objects.all())

    def delete_by_name(self, name: str) -> Product:
        p = Product.objects(name=name).first()
        if p is None:
            raise ProductDoesNotExistsException()
        p.delete()
        return p


# Singleton
product_controller = ProductController(conn)
