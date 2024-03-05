import pytest
import threading
import time

from kivy.tests.common import GraphicUnitTest
from kivy.clock import Clock
from kivy.base import stopTouchApp

from ayaapp import parentApp  # Assurez-vous de remplacer "votre_application" par le nom réel de votre fichier

class TestApp(GraphicUnitTest):
    def run_app(self):
        app = parentApp()
        app.run()

    def test_app(self):
        # Lancez l'application Kivy dans un thread distinct
        threading.Thread(target=self.run_app).start()

        # Attendez que l'application démarre
        time.sleep(2)  # Vous devrez peut-être ajuster le délai en fonction de la vitesse de démarrage de votre application

        # Fournissez des actions de test ici
        # Par exemple, vous pouvez simuler des clics sur le bouton et vérifier la sortie console
        # Assurez-vous d'adapter cela à votre logique spécifique

        # Arrêtez l'application Kivy
        stopTouchApp()

if __name__ == '__main__':
    pytest.main(['-vs', 'test_app.py'])
