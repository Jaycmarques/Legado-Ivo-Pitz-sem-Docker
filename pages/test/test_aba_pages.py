from django.urls import reverse
import pytest
from pages.models import Page
from mysite.django_assertions import assert_contains
from model_bakery import baker
from typing import List


@pytest.fixture
def pages(db):
    return baker.make(Page, 2)


@pytest.fixture
def resp(client, pages: List[Page]):
    resp = client.get(reverse('pages:detalhe'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


# def test_titulos_pages(resp, pages: List[Page]):
#     for page in pages:
#         assert_contains(resp, page.titulo)


# def test_links_pages(resp, pages: List[Page]):
#     for page in pages:
#         assert_contains(resp, page.get_absolute_url())
