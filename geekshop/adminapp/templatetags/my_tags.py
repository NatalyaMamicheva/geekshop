from django import template

register = template.Library()

URL_PREFIX = '/media/'


def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'
    
    new_string = "{}{}".format(URL_PREFIX, string)
    
    return new_string

    
@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.jpg'
    
    new_string = "{}{}".format(URL_PREFIX, string)
    
    return new_string


register.filter('media_folder_products', media_folder_products)
#register.filter('media_folder_users', media_folder_users)



if __name__ == '__main__':
    print(media_folder_products('products_images/product1.jpg'))
    print(media_folder_products(''))