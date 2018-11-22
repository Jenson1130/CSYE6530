package iotGateway.labs.module6;

import java.util.logging.Logger;

public class MqttPubClientTestApp {
	// static
		private static final Logger _Logger = Logger.getLogger(MqttPubClientTestApp.class.getName());
		private static MqttPubClientTestApp _App;
		
		// params
		private MqttClientConnector _mqttClient;
		
		/**
		 * 
		 */
		public MqttPubClientTestApp() {
		}

		/**
		 * @param args
		 */
		public static void main(String[] args) {
			_App = new MqttPubClientTestApp();
			try {
				_App.start();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		/**
		 * Connect to the MQTT client, then: 1) If this is the subscribe app, subscribe
		 * to the given topic 2) If this is the publish app, publish a test message to
		 * the given topic
		 */
		public void start() {
			
			_mqttClient = new MqttClientConnector("test.mosquitto.org","tcp",1883);
			_mqttClient.connect();
			String topicName = "test";
			String payload = "A test.";
			// only for publishing...
			_mqttClient.publishMessage(topicName, 2, payload.getBytes());
			_mqttClient.disconnect();
		}

	}



