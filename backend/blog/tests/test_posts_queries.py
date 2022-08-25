import json
import pytest

query_all_posts = '''
        query allPosts {
          posts {
            title
          }
        }
        '''

query_posts_by_tag = '''
        query postsByTagSlug($tagSlug: String) {
          posts(tagSlug: $tagSlug) {
            title
            tags {
              name
              slug
            }
          }
        }
        '''

query_posts_by_category = '''
        query postsByCategorySlug($categorySlug: String) {
          posts(categorySlug: $categorySlug) {
            title
            category {
              name
              slug
            }
          }
        }
        '''

query_posts_by_tag_and_category = '''
        query postsByTagAndCategorySlug($tagSlug: String, $categorySlug: String) {
          posts(tagSlug: $tagSlug, categorySlug: $categorySlug) {
            title
            category {
              slug
            }
            tags {
              name
              slug
            }
          }
        }
        '''


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_query_all_posts(client_query, posts):

    response = client_query(query_all_posts)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_all_posts = data.get('posts', None)
    assert data_all_posts is not None

    assert len(data_all_posts) == 2
    post1_title = data_all_posts[0].get('title', None)
    assert post1_title is not None
    assert post1_title == 'Test Post1'
    post2_title = data_all_posts[1].get('title', None)
    assert post2_title is not None
    assert post2_title == 'Test Post2'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_query_posts_by_category(client_query, posts):
    category_slug = {
        "categorySlug": "test_category2"
    }

    response = client_query(query_posts_by_category, variables=category_slug)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_posts = data.get('posts', None)
    assert data_posts is not None

    assert len(data_posts) == 1
    post_title = data_posts[0].get('title', None)
    assert post_title is not None
    assert post_title == 'Test Post2'
    post_category = data_posts[0].get('category', None)
    assert post_category is not None
    post_category_slug = post_category.get('slug', None)
    assert post_category_slug is not None
    assert post_category_slug == 'test_category2'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_query_posts_by_tag(client_query, posts, tags):
    tag_slug = {
        "tagSlug": "tag_2_slug",
    }

    response = client_query(query_posts_by_tag, variables=tag_slug)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_posts = data.get('posts', None)
    assert data_posts is not None

    assert len(data_posts) == 1
    post_title = data_posts[0].get('title', None)
    assert post_title is not None
    assert post_title == 'Test Post2'
    post_tags = data_posts[0].get('tags', None)
    assert post_tags is not None
    post_tag_slug = post_tags[0].get('slug', None)
    assert post_tag_slug is not None
    assert post_tag_slug == 'tag_2_slug'


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_query_posts_by_tag_and_category(client_query, posts, tags):
    slugs = {
        "tagSlug": "tag_2_slug",
        "categorySlug": "test_category2"
    }

    response = client_query(query_posts_by_tag_and_category, variables=slugs)

    content = json.loads(response.content)
    assert content is not None
    data = content.get('data', None)
    assert data is not None
    data_posts = data.get('posts', None)
    assert data_posts is not None

    assert len(data_posts) == 1
    post_title = data_posts[0].get('title', None)
    assert post_title is not None
    assert post_title == 'Test Post2'

    post_category = data_posts[0].get('category', None)
    assert post_category is not None
    post_category_slug = post_category.get('slug', None)
    assert post_category_slug is not None
    assert post_category_slug == 'test_category2'

    post_tags = data_posts[0].get('tags', None)
    assert post_tags is not None
    post_tag_slug = post_tags[0].get('slug', None)
    assert post_tag_slug is not None
    assert post_tag_slug == 'tag_2_slug'
