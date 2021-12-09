import pytest

from httpx import AsyncClient
from asyncio import get_event_loop

from mastodon_api.app import app


@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="module")
def event_loop():
    loop = get_event_loop()
    yield loop


# Albums
@pytest.mark.asyncio
async def test_get_albums_code(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/albums/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_albums_response_size(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/albums/")
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_albums_with_right_id_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/1/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_albums_with_right_id_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/1/")
    assert response.json()['name'] == 'Remission'


@pytest.mark.asyncio
async def test_get_albums_with_wrong_id_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/0/")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_albums_with_wrong_id_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/0/")
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 1},
                'loc': ['path', 'id'],
                'msg': 'ensure this value is greater than or equal to 1',
                'type': 'value_error.number.not_ge'
            }
        ]
    }


@pytest.mark.asyncio
async def test_get_albums_by_valid_acronymous_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/?name=The")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_albums_by_valid_acronymous_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/albums/?name=The")
    assert len(response.json()) > 1


@pytest.mark.asyncio
async def test_get_albums_by_invalid_name_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=Powerslave")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_albums_by_invalid_name_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=Powerslave")
    assert response.json() == {'detail': 'Album not found.'}


@pytest.mark.asyncio
async def test_get_albums_with_a_right_long_word_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=Crack the Skye")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_albums_with_a_right_long_word_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=Crack the Skye")
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_get_albums_with_a_wrong_long_word_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=The Number of the Beast")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_albums_with_a_wrong_long_word_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/albums/?name=The Number of the Beast")
    assert response.json() == {'detail': 'Album not found.'}


# Members
@pytest.mark.asyncio
async def test_get_members_code(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/members/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_members_response_size(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/members/")
    assert len(response.json()) > 0


@pytest.mark.asyncio
async def test_get_members_with_right_id_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/1/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_members_with_right_id_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/1/")
    assert response.json()['name'] == 'Brent Hinds'


@pytest.mark.asyncio
async def test_get_members_with_wrong_id_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/0/")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_members_with_wrong_id_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/0/")
    assert response.json() == {
        'detail': [
            {
                'ctx': {'limit_value': 1},
                'loc': ['path', 'id'],
                'msg': 'ensure this value is greater than or equal to 1',
                'type': 'value_error.number.not_ge'
            }
        ]
    }


@pytest.mark.asyncio
async def test_get_members_by_valid_acronymous_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/?name=Bran")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_members_by_valid_acronymous_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get("/api/members/?name=Bre")
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_get_members_by_invalid_name_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Pery")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_members_by_invalid_name_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Pery")
    assert response.json() == {'detail': 'Member not found.'}


@pytest.mark.asyncio
async def test_get_members_with_a_right_long_word_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Brann Dailor")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_members_with_a_right_long_word_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Brann Dailor")
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_get_members_with_a_wrong_long_word_code(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Bruce Dickinson")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_members_with_a_wrong_long_word_response(
    async_client: AsyncClient
) -> None:
    response = await async_client.get(
        "/api/members/?name=Bruce Dickinson")
    assert response.json() == {'detail': 'Member not found.'}
