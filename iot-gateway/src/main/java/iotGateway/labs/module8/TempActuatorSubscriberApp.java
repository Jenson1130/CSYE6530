package iotGateway.labs.module8;

import java.util.logging.Logger;
import iotGateway.labs.module8.MqttClientConnector
;
public class TempActuatorSubscriberApp {
	private String _userName = "";
	private String _authToken = "";
	private String _pemFileName = "/Users/stannis/Desktop/csye6530/ubidots.pem";
	private String _host = "things.ubidots.com";

	
	// static
	private static final Logger _Logger = Logger.getLogger(TempActuatorSubscriberApp.class.getName());
	private static TempActuatorSubscriberApp _App;
	
	// params
	private MqttClientConnector _mqttClient;

	public static void main(String[] args) {
		_App = new TempActuatorSubscriberApp();
		try {
			_App.start();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Default.
	 */

	public TempActuatorSubscriberApp() {
		super();
	}
	
	/**
	 * Connect to the MQTT client, then: 1) If this is the subscribe app, subscribe
	 * to the given topic 2) If this is the publish app, publish a test message to
	 * the given topic
	 */
	public void start() {
		_mqttClient = new MqttClientConnector(_host, _userName, _pemFileName, _authToken);
		_mqttClient.connect();
		String topicName = "/v1.6/devices/homeiotgateway/tempactuator";
		_mqttClient.subscribeToTopic(topicName);
	}


}
