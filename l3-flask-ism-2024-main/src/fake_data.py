products = [
    {
        "id":1,
        "title": "toto",
        "img_url": [
            "https://www.bugatti-fashion.com/media/bug_magazin_ratgeber_slim-jeans2280x1200.jpg",
            "https://cdn.thewirecutter.com/wp-content/media/2023/10/womensjeans-2048px-04346.jpg?auto=webp&quality=75&width=1024"
            "https://www.realmenrealstyle.com/wp-content/uploads/2021/07/mens-jeans.jpg",
            "https://images.boardriders.com/global/dcshoes-products/all/default/large/adydp03056_dcshoes,f_bsnw_frt1.jpg"
            ],
        "price": 100,
        "stock": 2
    },
    {
        "id":2,
        "title": "titi",
        "img_url": ["https://www.bugatti-fashion.com/media/bug_magazin_ratgeber_slim-jeans2280x1200.jpg","img2"],
        "price": 24,
        "stock": 12
    },
    {
        "id":3,
        "title": "tutu",
        "img_url": ["https://www.bugatti-fashion.com/media/bug_magazin_ratgeber_slim-jeans2280x1200.jpg","img2"],
        "price": 4,
        "stock": 4
    }
]

def getAll():
    return products


def findProductById(id_product):
    for p in products:
        if p["id"] == id_product:
            return p
    return None