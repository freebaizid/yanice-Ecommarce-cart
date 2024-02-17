from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ShoppingCart
import json
@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            product_data = data.get('product')
            quantity = int(data.get('quantity', 1))

            if not session_id or not product_data:
                return JsonResponse({'error': 'Session ID and product data are required'}, status=400)

            cart =ShoppingCart.objects.create(product=product_data, quantity = quantity , session_id=session_id )
           
            cart.save()

            return JsonResponse({'message': 'Product added to cart successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

from django.http import JsonResponse
from .models import ShoppingCart
def view_cart(request):
    if request.method == 'GET':
        session_id = request.GET.get('session_id')
        
        if not session_id:
            return JsonResponse({'error': 'Session ID is required'}, status=400)

        carts = ShoppingCart.objects.filter(session_id=session_id)

        if not carts.exists():
            return JsonResponse({'error': 'Shopping cart not found'}, status=404)

        cart_items = {
            'items': [],
            'total_quantity': 0,
        }

        for cart in carts:
            # Append product and quantity to cart_items for each cart
            cart_items['items'].append({
                'product': cart.product,
                'quantity': cart.quantity,
                'cart_id': cart.id,

            })
            cart_items['total_quantity'] += cart.quantity
            
        return JsonResponse(cart_items, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)




@csrf_exempt
def delete_cart(request):
    if request.method == 'POST':
        cart_id = request.GET.get('id')
        
        if not cart_id:
            return JsonResponse({'error': 'Cart ID is required'}, status=400)

        try:
            cart = ShoppingCart.objects.get(id=cart_id)
            cart.delete()
            return JsonResponse({'message': 'Cart deleted successfully'}, status=200)
        except ShoppingCart.DoesNotExist:
            return JsonResponse({'error': 'Shopping cart not found'}, status=404)





def show_session_id(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.save()
        session_id = request.session.session_key
    
    return JsonResponse({"session_id": session_id})








def view_cart_count(request):
    if request.method == 'GET':
        session_id = request.GET.get('session_id')
        
        if not session_id:
            return JsonResponse({'error': 'Session ID is required'}, status=400)

        carts = ShoppingCart.objects.filter(session_id=session_id)

        if not carts.exists():
            return JsonResponse({'error': 'Shopping cart not found'}, status=404)

        cart_items = {
            'items': [],
            'total_quantity': 0,
        }

        for cart in carts:
            # Append product and quantity to cart_items for each cart
            cart_items['items'].append({
              
                'cart_id': cart.id,

            })
            cart_items['total_quantity'] += cart.quantity
            
        return JsonResponse(cart_items, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)





