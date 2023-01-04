# How many orders do we have?
    > result = Order.objects.aggregate(Count('id'))

# How many units of product 1 have we sold?
    > result = OrderItem.objects.filter(product_id=1).aggregate(sold_first_prod=Sum('quantity'))

# How many orders has customer 1 placed?
    > result = Order.objects.filter(customer_id=1).aggregate(orders_customer_first=Count('id'))

# What is the min, max and average price of the products in collection 3?
    > result = Product.objects.select_related('collection').filter(collection__id=3).aggregate(min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))