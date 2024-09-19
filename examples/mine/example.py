from tapsdk import TapSDK, TapInputMode
tap_device = TapSDK()

#블루투스 연결

#input 모드 설정
tap_device.set_input_mode(TapInputMode("raw")) #, sensitivity=[0,0,0]

#이벤트 수신 등록
    #기기가 연결됐을 때
def on_connect(identifier, name, fw):
    print(identifier + " - connected. Name: " + str(name), " FW Version: ", fw)

tap_device.register_connection_events(on_connect)

    #기기가 연결 해제됐을 때
def on_disconnect(identifier):
    print(identifier + " - disconnected")

tap_device.register_disconnection_events(on_disconnect)

    #원시 데이터 수신할 때 
def on_raw_sensor_data(identifier, raw_sensor_data):
    print(identifier + " - raw data received: " + str(raw_sensor_data))

tap_device.register_raw_data_events(on_raw_sensor_data)