from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel
)

from mavlink.telemetry_worker import TelemetryWorker
from map.map_widget import MapWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QMainWindow {
              background-color: #1e1e1e;
             }

             QWidget {
              background-color: #1e1e1e;
              color: white;
            }

            QLabel {
              color: white;
           }
    """)

        self.setWindowTitle("POYRAZ YKI")
        self.resize(1000, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title_label = QLabel(
            "POYRAZ YER KONTROL İSTASYONU"
        )

        title_label.setStyleSheet(
             """
             font-size: 20px;
             font-weight: bold;
             padding: 10px;
            """
        )

        layout.addWidget(title_label)

        self.connection_label = QLabel(
             "🟡 BAĞLANIYOR..."
        )

        self.connection_label.setStyleSheet(
            """
            color: green;
            font-size: 16px;
            font-weight: bold;
            """
        )

        layout.addWidget(self.connection_label)

        self.altitude_label = QLabel("İrtifa : Bekleniyor...")
        self.speed_label = QLabel("Hız : Bekleniyor...")
        self.mode_label = QLabel("Mod : Bekleniyor...")
        self.battery_label = QLabel("Batarya : Bekleniyor...")

        gps_title = QLabel("GPS KOORDİNATLARI")

        gps_title.setStyleSheet("""
            color:#4FC3F7;
            font-size:14px;
            font-weight:bold;
        """)

        layout.addWidget(gps_title)   

        self.map_widget = MapWidget()
        self.map_widget.setMinimumHeight(450)
        self.latitude_label = QLabel("Enlem : ---")
        self.longitude_label = QLabel("Boylam : ---")
        for label in [
            self.altitude_label,
            self.speed_label,
            self.mode_label,
            self.battery_label,
            self.latitude_label,
            self.longitude_label
        ]:
             label.setStyleSheet(
                 """
                 font-size:14px;
                 padding:5px;
                 """
            )

        grid = QGridLayout()

        for label in [
             self.altitude_label,
             self.speed_label,
             self.mode_label,
             self.battery_label
        ]:
             label.setStyleSheet("""
                 background-color:#2d2d2d;
                 border:1px solid #404040;
                 border-radius:8px;
                 padding:8px;
                 font-size:14px;
                 font-weight:bold;
            """)

        grid.addWidget(self.altitude_label, 0, 0)
        grid.addWidget(self.speed_label, 0, 1)
        grid.addWidget(self.mode_label, 1, 0)
        grid.addWidget(self.battery_label, 1, 1)

        layout.addLayout(grid)


        layout.addWidget(
            self.map_widget,
            stretch=1
        )
        layout.addWidget(self.latitude_label)
        layout.addWidget(self.longitude_label)

        central_widget.setLayout(layout)

        self.worker = TelemetryWorker()

        self.worker.telemetry_received.connect(
            self.update_telemetry
        )

        self.worker.connection_status.connect(
            self.update_connection_status
        )

        self.worker.start()

    def update_telemetry(
        self,
        latitude,
        longitude,
        altitude,
        speed,
        mode,
        battery
    ):
        
        self.altitude_label.setText(
            f"İrtifa : {altitude:.2f} m"
        )
        self.speed_label.setText(
             f"Hız : {speed:.2f} m/s"
        )
        self.mode_label.setText(
            f"Mod : {mode}"
        )
        self.latitude_label.setText(
            f"Enlem : {latitude:.7f}"
        )

        self.longitude_label.setText(
             f"Boylam : {longitude:.7f}"
        )
        self.map_widget.update_position(
            latitude,
            longitude
        )
        if battery >= 0:
            self.battery_label.setText(
                 f"Batarya : %{battery}"
        )
            
    def update_connection_status(
        self,
         connected
    ):
        if connected:
             self.connection_label.setText(
            "🟢 MAVLINK BAĞLI"
        )
        else:
             self.connection_label.setText(
            "🔴 MAVLINK BAĞLI DEĞİL"
        )