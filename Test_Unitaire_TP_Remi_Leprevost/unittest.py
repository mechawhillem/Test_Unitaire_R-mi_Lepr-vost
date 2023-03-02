import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestLieuxAPI(unittest.TestCase):
    def test_get_lieux(self):
        response = client.get("/lieux")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'donnees': {'lieux': ['Paris', 'Lyon', 'Marseille', 'Montpellier', 'Toulon', 'Lilles', 'Nantes']}})

    def test_post_lieu_existing(self):
        response = client.post("/lieux", json={"lieu": "Paris"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'donnees': {'lieux': ['Paris', 'Lyon', 'Marseille', 'Montpellier', 'Toulon', 'Lilles', 'Nantes']}, 'message': "l'emplacement existe déjà"})

    def test_post_lieu_new(self):
        response = client.post("/lieux", json={"lieu": "Bordeaux"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'donnees': {'lieux': ['Paris', 'Lyon', 'Marseille', 'Montpellier', 'Toulon', 'Lilles', 'Nantes', 'Bordeaux']}, 'message': "l'emplacement a été ajouté"})

    def test_delete_lieu_existing(self):
        response = client.delete("/lieux", json={"lieu": "Paris"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'data': {'lieux': ['Lyon', 'Marseille', 'Montpellier', 'Toulon', 'Lilles', 'Nantes', 'Bordeaux']}, 'message': 'le lieu est supprimé'})

    def test_delete_lieu_non_existing(self):
        response = client.delete("/lieux", json={"lieu": "Toulouse"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'data': {'lieux': ['Lyon', 'Marseille', 'Montpellier', 'Toulon', 'Lilles', 'Nantes', 'Bordeaux']}, 'message': 'le lieu n héxiste pas'})

