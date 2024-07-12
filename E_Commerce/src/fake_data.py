
produits=[
    {
        "id":1,
        "title":"toto",
        "img_url" : [
            "https://images.pexels.com/photos/821651/pexels-photo-821651.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://images.pexels.com/photos/14200837/pexels-photo-14200837.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "https://images.pexels.com/photos/8617981/pexels-photo-8617981.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            ],
        "price":100,
        "stock":12 
    },
    {
        "id":2,
        "title":"titi",
        "img_url" : [
            "https://images.pexels.com/photos/3373736/pexels-photo-3373736.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://images.pexels.com/photos/14200837/pexels-photo-14200837.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "https://images.pexels.com/photos/8617981/pexels-photo-8617981.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            ],
        "price":120,
        "stock":24 
    },
    {
        "id":3,
        "title":"tutu",
        "img_url" : [
            "https://images.pexels.com/photos/2697787/pexels-photo-2697787.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "https://images.pexels.com/photos/8617981/pexels-photo-8617981.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "https://images.pexels.com/photos/14200837/pexels-photo-14200837.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            ],
        "price":200,
        "stock":15 
    },
]

def getAll():
    return produits

def findProductById(id_product):
    for p in produits:
        if p["id"] == id_product:
            return p
    return None