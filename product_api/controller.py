from models import Product
from product_api.base import conn


# TODO: implement controller methods
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

        pass

    def get_by_name(self, name: str) -> Product:
        """

        :param name:
        :return:
        """
        pass

    def change(self, **kwargs) -> bool:
        """

        :param kwargs:
        :return:
        """
        pass

    def delete_by_name(self, name: str) -> bool:
        """

        :param name:
        :return:
        """
        pass


# Singleton
product_controller = ProductController(conn)
