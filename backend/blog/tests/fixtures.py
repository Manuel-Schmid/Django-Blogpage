import pytest

from blog.models import Post, Category


@pytest.fixture
def categories():
    Category.objects.create(name="testcategory")
    return Category.objects.all()