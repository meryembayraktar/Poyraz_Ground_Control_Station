from PyQt5.QtCore import QThread, pyqtSignal
from pymavlink import mavutil


class TelemetryWorker(QThread):

    telemetry_received = pyqtSignal(
        float,
        float,
        float,
        float,
        str,
        int
    )
    connection_status = pyqtSignal(bool)
    def run(self):

        master = mavutil.mavlink_connection(
            "tcp:127.0.0.1:5762"
        )

        master.wait_heartbeat()
        self.connection_status.emit(True)

        while True:
           
            msg = master.recv_match(
                type="GLOBAL_POSITION_INT",
                blocking=True
            )

            if msg:

                latitude = msg.lat / 1e7
                longitude = msg.lon / 1e7
                altitude = msg.alt / 1000
                speed = msg.vx / 100
                mode = master.flightmode
                battery_msg = master.recv_match(
                     type="SYS_STATUS",
                     blocking=False
                )


                battery = -1

                if battery_msg:
                     battery = battery_msg.battery_remaining
                
                self.telemetry_received.emit(
                     latitude,
                     longitude,
                     altitude,
                     speed,
                     mode,
                     battery
                )