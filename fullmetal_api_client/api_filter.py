from fullmetal_api_client.api_exception import ApiException
from jsonrpc2_base.plugins.client.client_plugin_base import ClientPluginBase


class ApiFilter(ClientPluginBase):
    def exceptionCatch(self, exception):

        if exception.getCode() >= 0:
            raise ApiException(exception.getMessage(), exception.getCode())
        else:
            raise exception
