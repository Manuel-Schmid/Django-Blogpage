import pytest



from blog.models import Post, Category


# def get_category_count():
#     return Category.objects.all().count()


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_post(categories):
    pres_category_count = len(categories)
    print(pres_category_count)
    assert pres_category_count == 7

