# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)

# ---- Funciones a implementar ----

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    tdescuento = apply_discount(subtotal, discount_pct)
    timpuesto = apply_tax(tdescuento, tax_pct)
    return round(timpuesto, 2)
    
    """
    Calcula el precio final de una compra.
    Debe USAR las funciones apply_discount y apply_tax.

    Pasos:
      1. Calcular el subtotal (price * quantity).
      2. Aplicar el descuento al subtotal usando apply_discount.
      3. Aplicar el impuesto al resultado usando apply_tax.
      4. Retornar el resultado redondeado a 2 decimales usando round().
    """
final_price()

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    producta = final_price(price_a, qty_a, disc_a, tax_pct)
    productb = final_price(price_b, qty_b, disc_b, tax_pct)
    if producta == productb:
        return "A"
    elif producta > productb:
        return "B"
    elif producta < productb:
        return "A"
    
    """
    Dados dos productos A y B (cada uno con su precio, cantidad y descuento)
    y un porcentaje de impuesto común, retorna el string "A" o "B"
    según cuál tenga el menor precio final.
    Si son iguales, retorna "A".
    Debe USAR la función final_price para resolver el ejercicio.
    """