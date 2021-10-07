import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate","Granizado", "Limon", "Dulce de Leche"], "quantity":[3,10,0,5]})

def is_product_available(product_name, quantity):
    '''Retornamos 3 valores:\n
    bool > indica si existe el producto\n
    bool > indica si hay en existencia el stock solicitado\n
    int > indica la cantidad restante de stock'''
    
    exist = True
    available = True
    stock = 0
    
    if product_name not in _PRODUCT_DF.product_name.values:
        exist = False
        available = False
    else:
        _PRODUCT_DF.set_index("product_name",inplace=True)
        value = _PRODUCT_DF.loc[product_name]
        stock = value["quantity"]
        if quantity > stock:
            available = False
    
    return exist, available, stock


print(is_product_available("Chocolate",2))