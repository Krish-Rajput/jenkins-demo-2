import pytest
from app import app, feedback_list

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear feedback list before each test to keep tests independent
        feedback_list.clear()
        yield client

def test_index_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Feedback System' in response.data

def test_feedback_submission(client):
    """Test submitting feedback via POST and seeing it rendered."""
    response = client.post('/', data={
        'name': 'Alice Smith',
        'course': 'DevOps Engineering',
        'feedback': 'Great application and setup!'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Alice Smith' in response.data
    assert b'DevOps Engineering' in response.data
    assert b'Great application and setup!' in response.data