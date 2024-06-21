def total_carrito(request):
    total = 0
    for key, value in request.session.get('carrito', {}).items():
        total += int(value.get("acumulado", 0))
    return {"total_carrito": total}