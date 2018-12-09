package iotGateway.labs.module8;

import java.util.logging.Logger;
import iotGateway.labs.module8.MqttClientConnector;

public class TempSensorPublisherApp {
	private String _userName = "";
	private String _authToken = "A1E-gyEfBVN4xE7fdLLsY92xngiYHENTCN";
	private String _pemFileName ="/Users/stannis/Desktop/csye6530/ubidots.pem";
	private String _host = "things.ubidots.com";
	
	// static
	private static final Logger _Logger = Logger.getLogger(TempSensorPublisherApp.class.getName());
	private static TempSensorPublisherApp _App;
	
	// params
	private MqttClientConnector _mqttClient;
	
	/**
	 * 
	 */
	public TempSensorPublisherApp() {
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		_App = new TempSensorPublisherApp();
		try {
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void start() {
		
		_mqttClient = new MqttClientConnector(_host, _userName, _pemFileName, _authToken);
		_mqttClient.connect();
		String topicName = "/v1.6/devices/HomeIotGateway/tempsensor";
	    String payload = "28";
		_mqttClient.publishMessage(topicName, 0, payload.getBytes());
		_mqttClient.disconnect();
	}


}
