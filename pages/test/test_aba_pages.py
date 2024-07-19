from django.urls import reverse
import pytest
from pages.models import Page
from mysite.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def pages(db):
    return baker.make(Page, 2)


@pytest.fixture
def resp(client, pages):
    resp = client.get(reverse('familytree:familytree_index'))
    return resp


def test_titulos_pages(resp, pages):
    for page in pages:
        assert_contains(resp, page.titulo)


def test_links_pages(resp, pages):
    for page in pages:
        assert_contains(resp, page.get_absolute_url())
