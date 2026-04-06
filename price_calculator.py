# ---- Funciones provistas (NO modificar) ----

def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)
#apply_discount()
def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)
#apply_tax()
# ---- Funciones a implementar ----

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    tdescuento = apply_discount(subtotal, discount_pct)
    timpuesto = apply_tax(tdescuento, tax_pct)
    return round(timpuesto, 2)
#final_price()

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    producta = final_price(price_a, qty_a, disc_a, tax_pct)
    productb = final_price(price_b, qty_b, disc_b, tax_pct)
    if producta == productb:
        return "A"
    elif producta > productb:
        return "B"
    elif producta < productb:
        return "A"
#best_deal()