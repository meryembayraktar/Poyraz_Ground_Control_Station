import folium
import tempfile

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MapWidget(QWebEngineView):

    def __init__(self):
        super().__init__()

        self.update_position(
            -35.3633517,
            149.1652413
        )

    def update_position(
        self,
        latitude,
        longitude
    ):

        m = folium.Map(
            location=[latitude, longitude],
            zoom_start=16
        )

        folium.Marker(
            [latitude, longitude],
            popup="İHA",
            tooltip="İHA"
        ).add_to(m)

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".html"
        )

        m.save(temp_file.name)

        self.load(
            QUrl.fromLocalFile(
                temp_file.name
            )
        )