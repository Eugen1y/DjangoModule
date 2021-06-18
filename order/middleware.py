"""
Purchase Application Middlewares
================================

"""

from order.models import Cart


class ProductCartMiddleware(object):
    """Product cart middleware implementation"""

    def __init__(self, get_response):
        """Constructor"""

        self.get_response = get_response

    def __call__(self, *args, **kwargs):
        """Middleware call handler"""

        response = self.get_response(*args, **kwargs)

        return response

    # noinspection PyMethodMayBeStatic
    def process_template_response(self, request, response):
        """Process template response"""

        if not request.user.is_authenticated or request.user.is_staff:
            return response

        customer = request.user
        try:
            cart = Cart.objects.get(customer=customer, purchased=False)
        except Cart.DoesNotExist:
            return response

        response.context_data["cart_entities_count"] = cart.get_entities_count()

        return response
